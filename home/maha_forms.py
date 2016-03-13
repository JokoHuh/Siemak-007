from django import forms
from db.models import Mahasiswa

class MahasiswaForm(forms.ModelForm):

    class Meta:
        model = Mahasiswa
        fields = ('idx', 'nim', 'nama', 'angkatan', 'sks', 'catatan', 'konversi', 'pts', 'prodi', 'status')

