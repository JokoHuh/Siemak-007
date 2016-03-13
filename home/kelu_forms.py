from django import forms
from db.models import Kelulusan

class KelulusanForm(forms.ModelForm):

    class Meta:
        model = Kelulusan
        fields = ('idx', 'mahasiswa', 'nr_transkrip', 'judul1', 'judul2', 'ipk', 'tgl_yudisium', 'wisuda', 'catatan')

