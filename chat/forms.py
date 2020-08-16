from django import forms
from .models import Review

class ComposeForm(forms.Form):
    message = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
                )
            )


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['review_message']

    
    