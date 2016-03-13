from django import forms
from db.models import Prodi
from db.models import Pts
 
class ProdiForm(forms.ModelForm):
	def __init__(self, idx, *args, **kwargs):
		idx = idx
		super(ProdiForm, self).__init__(*args, **kwargs)
		self.fields['pts'].queryset=Pts.objects.filter(idx=idx)

	class Meta:
		model = Prodi
		fields = ('idx', 'nama', 'pts')
		
