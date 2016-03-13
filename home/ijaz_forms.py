from django import forms
from db.models import Ijazah

class IjazahForm(forms.ModelForm):

    class Meta:
        model = Ijazah
        fields = ('idx', 'nomor', 'nr_seri', 'catatan', 'status', 'mahasiswa')

