from django.shortcuts import render

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from sendemail.forms import ContactForm


class SuccessView(TemplateView):
    template_name = "sendemail/success.html"

class ContactView(FormView):
    form_class = ContactForm
    template_name = "sendemail/contact.html"
    success_url = reverse_lazy("sendemail:success")
    



    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        

        full_message = f"""
            Received message below from {name} {email}, {subject}
            ________________________


            {message}
            """
            
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
        )
        return super(ContactView, self).form_valid(form)
