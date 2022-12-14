from django.urls import path
from .views import monthly_challenge_str, monthly_challenge_int, index

urlpatterns = [
    path("",index, name="challenges_index"),
    path("<int:month>", monthly_challenge_int, name="int_month"),
    path("<str:month>", monthly_challenge_str, name="string_month"),
]