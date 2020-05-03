from django import forms

from grievance import models


class GrievanceForm(forms.ModelForm):
    class Meta:
        fields = ("title","description","against")
        model = models.Grievance

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
