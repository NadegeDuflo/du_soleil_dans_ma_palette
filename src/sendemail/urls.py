from django.urls import path

from sendemail.views import SuccessView, ContactView

app_name = "sendemail"

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("success/", SuccessView.as_view(), name="success"),
]