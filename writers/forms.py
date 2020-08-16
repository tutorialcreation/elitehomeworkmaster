from django import forms

from .models import WritersJoin,Document

class JoinWritersForm(forms.ModelForm):
    class Meta:
        model=WritersJoin
        fields='__all__'


class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=('description','document')
        