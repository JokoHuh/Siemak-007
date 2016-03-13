from django import forms
from db.models import Krs

class KrsForm(forms.ModelForm):

	class Meta:
		model = Krs
		fields = ('idx', 'takrs', 'mahasiswa', 'kelompok', 'tanggal')

