from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile

class TechnologyForm(forms.Form):
    # max_upload_limit = 2 * 1024 * 1024
    # max_upload_limit_text = naturalsize(max_upload_limit)


    project = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':"Project"}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder':"Product Description", "rows":5}))
    picture = forms.FileField(required=False)
    upload_field_name = 'picture'