from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# Create your views here.

monthly_challenges_dict = {
    "january": "the challenge for jan",
    "february": "the challenge for feb",
    "march": "the challenge for mar",
    "april": "the challenge for apr",
    "may": "the challenge for may",
    "june": "the challenge for jun",
    "july": "the challenge for jul",
    "august": "the challenge for aug",
    "september": "the challenge for sep",
    "october": "the challenge for oct",
    "november": "the challenge for nov",
    "december": "the challenge for dec",
}
month_list = list(monthly_challenges_dict.keys())

def index(request):
    return HttpResponse(month_list)

def monthly_challenge_int(request, month):
    if month > 0 and month <=12:
        return HttpResponseRedirect(reverse("string_month", args=[month_list[month-1]]))
    else:
        return HttpResponseNotFound("not a month")

def monthly_challenge_str(request, month):
    if month in month_list:
        response_data = monthly_challenges_dict[month]
        data = {
            "month" : month,
            "task" : response_data,
        }
        return render(request, "challenges/challenge.html", data)
    else:
        return HttpResponseNotFound("not a month")
