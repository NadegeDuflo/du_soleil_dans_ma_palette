from django import forms

#from django_recaptcha.fields import ReCaptchaField
#from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder":"Votre nom et prénom"})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"placeholder": "Votre e-mail"})
    )
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Sujet"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Votre message"})
    )
    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())