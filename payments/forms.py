from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
# from .models import Membership
from assignments.models import Assignment
from django import forms

class QuoteForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=['price','task']

