from django import forms
from db.models import Sk

class SkForm(forms.ModelForm):

    class Meta:
        model = Sk
        fields = ('idx', 'nr_sk', 'nr_kk', 'judul', 'tanggal', 'catatan', 'pegawai', 'status')

