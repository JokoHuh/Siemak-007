from django import forms
from db.models import Pts

class PtsForm(forms.ModelForm):

    class Meta:
        model = Pts
        fields = ('idx', 'nama', 'namapanjang', 'catatan', 'pt')
