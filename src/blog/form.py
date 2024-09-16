from django import forms

from blog.models import Comment, CommentAnswer

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class CommentForm(forms.ModelForm):
    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    class Meta:
        model = Comment
        fields = [
            "author_comment",
            "content_comment",
            ]
        labels = {"author_comment": "Votre nom",
                  "content_comment": "Votre commentaire"}
        widgets = {
            "content_comment": forms.Textarea(attrs={
                #'class' : 'ma-class'
                'row': 4,
                'cols': 70,
                'placeholder': 'Laisser votre commentaire...',
            })
        }

class AnswerForm(forms.ModelForm):
    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    class Meta:
        model = CommentAnswer
        fields = [
            "comment",
            "author_answer",
            "content_answer",
        ]
        labels = {"comment": "A qui ?",
                  "author_answer": "Votre nom",
                  "content_answer": "Votre réponse"
        }

        widgets = {
            "content_answer": forms.Textarea(attrs={
                # 'class' : 'ma-class'
                'row': 2,
                'cols': 30,
                'placeholder': 'Répondez...',
            })
        }





