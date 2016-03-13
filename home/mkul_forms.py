from django import forms
from db.models import Matakuliah

class MatakuliahForm(forms.ModelForm):

    class Meta:
        model = Matakuliah
        fields = ('idx', 'kode', 'nama', 't', 'p', 'k', 'pts', 'semester')

