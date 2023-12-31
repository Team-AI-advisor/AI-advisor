from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    upload = forms.FileField(
        label="첨부 파일", required=True, widget=forms.FileInput(attrs={"class": "form"})
    )

    class Meta:
        model = Document
        exclude = ["attached"]
