from django import forms
from db.models import Pembayaran

class PembayaranForm(forms.ModelForm):

    class Meta:
        model = Pembayaran
        fields = ('idx', 'tanggal', 'jenis', 'nr_validasi', 'mahasiswa')

