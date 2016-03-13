from django import forms
from db.models import Takrs
from db.models import Pts

class TakrsForm(forms.ModelForm):
	def __init__(self, idx, *args, **kwargs):
		idx = idx
		super(TakrsForm, self).__init__(*args, **kwargs)
		self.fields['pts'].queryset=Pts.objects.filter(idx=idx)

	class Meta:
		model = Takrs
		fields = ('idx', 'tahunakademik', 'tgldaftarA', 'tgldaftarB', 'tglubahA', 'tglubahB', 'tglkuliahA', 'tglkuliahB', 'pts')

