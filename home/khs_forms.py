from django import forms
from db.models import Khs

class KhsForm(forms.ModelForm):

    class Meta:
        model = Khs
        fields = ('idx', 'krs', 'tanggal', 'ip')

