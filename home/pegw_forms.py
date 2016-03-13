from django import forms
from db.models import Pegawai
from db.models import Pts

class PegawaiForm(forms.ModelForm):
	def __init__(self, idx, *args, **kwargs):
		idx = idx
		super(PegawaiForm, self).__init__(*args, **kwargs)
		self.fields['pts'].queryset=Pts.objects.filter(idx=idx)

	class Meta:
		model = Pegawai
		fields = ('idx', 'nama', 'nip', 'nidn', 'tanggal', 'na_titel', 'na_titel_setara', 'catatan', 'golpgw', 'grppgw', 'japgw', 'pts', 'status')

