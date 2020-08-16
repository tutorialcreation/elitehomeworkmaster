from django import forms
from .models import Assignment

class AssignmentDocumentForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('level','types','description','document','deadline','more_info')

class AssignmentEditForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('level','types','description','document','deadline')


class UploadAssignmentForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('writer_document',)

class AssignWriterForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('solution_format','writers_deadline','status','writers_amount')


        def __init__(self, *args, **kwargs):
            super(AssignWriterForm, self).__init__(*args, **kwargs)
