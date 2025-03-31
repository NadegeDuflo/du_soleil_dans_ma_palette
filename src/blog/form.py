from django import forms

from blog.models import Comment, Reply



class CommentForm(forms.ModelForm):
    #edit_comment = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Comment
        fields = [
            "author_comment",
            "content_comment",
            ]
        labels = {"author_comment": "",
                  "content_comment": ""}
        widgets = {
            "content_comment": forms.Textarea(attrs={
                #'class' : 'ma-class'
                'rows': 4,
                'cols': 70,
                'placeholder': 'Laisser votre commentaire...',
            })
        }

class ReplyForm(forms.ModelForm):
    #edit_comment_answer = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Reply
        fields = [
            #"comment",
            "author_answer",
            "content_answer",
        ]
        labels = {"comment": "",
                  "author_answer": "",
                  "content_answer": ""
        }

        widgets = {
            "comment": forms.Select(attrs={
                #'value' : "{{comment.id}}"
                }),
            "author_answer": forms.TextInput(attrs={
                'placeholder': "Votre Nom",
            }),
            "content_answer": forms.Textarea(attrs={
                # 'class' : 'ma-class'
                'rows': 2,
                'cols': 50,
                'placeholder': 'Répondez...',
            })
        }





