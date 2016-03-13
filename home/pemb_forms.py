from django import forms
from db.models import Pembimbing

class PembimbingForm(forms.ModelForm):

    class Meta:
        model = Pembimbing
        fields = ('idx', 'mahasiswa', 'tanggal', 'dosen', 'status')

