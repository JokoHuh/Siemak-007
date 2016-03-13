from django import forms
from db.models import Tugasmengajar

class TugasmengajarForm(forms.ModelForm):

    class Meta:
        model = Tugasmengajar
        fields = ('idx', 'sks', 'tahunakademik', 'dayatampung', 'dosen', 'kelompok', 'matakuliah')

