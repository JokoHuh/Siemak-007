from django import forms
from db.models import Pt

class PtForm(forms.ModelForm):

    class Meta:
        model = Pt
        fields = ('idx', 'nama', 'alamat')

