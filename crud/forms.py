from dataclasses import fields
from django.forms import ModelForm
from .models import  Detail


class Detailform(ModelForm):
    class Meta:
        model=Detail
        fields=['accname','age']