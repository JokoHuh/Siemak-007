from django.shortcuts import render, get_object_or_404
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def index(request):
	return render(request, 'home/index.html', {})

def logout_user(request):
	if request.POST:
		logout(request)	
	return render(request, 'home/index.html', {})

def login_user(request):
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
	return render_to_response('home/login_user.html', context_instance=RequestContext(request))

def taek(request):
	return render(request, 'home/taek.html', {})

def pts_id(request):
	user = request.user
	idx=0 #semua
	if user.groups.filter(name='pts01').count():
		idx=1 #stisipol
	elif user.groups.filter(name='pts02').count():
		idx=2 #stiper
	elif user.groups.filter(name='pts03').count():
		idx=3 #akper
	elif user.groups.filter(name='pts04').count():
		idx=4 #stkip
	elif user.groups.filter(name='pts05').count():
		idx=5 #stmik
	return idx

#KELEMBAGAAN
# ------------------------------------------------------------ Pt
from .pt_forms import PtForm
from db.models import Pt

def pt_list(request):
	if request.user.has_perm('db.change_pt') is False:
		return render(request, 'home/taek.html', {})
	pt = Pt.objects.all().order_by('idx')
	return render(request, 'home/pt_list.html', {'pt': pt})

def pt_detail(request, pk):
	pt = get_object_or_404(Pt, pk=pk)
	return render(request, 'home/pt_detail.html', {'pt': pt})

def pt_new(request):
	if request.user.has_perm('db.add_pt') is False:
		return render(request, 'home/taek.html', {})
	if request.method == "POST":
		form = PtForm(request.POST)
		if form.is_valid():
			pt = form.save(commit=False)
			pt.idx = request.POST['idx']
			pt.nama = request.POST['nama']
			pt.alamat = request.POST['alamat']
			pt.save()
			return redirect('pt_detail', pk=pt.pk)
	else:
		form = PtForm()
	return render(request, 'home/pt_edit.html', {'form': form})

def pt_edit(request, pk):
	pt = get_object_or_404(Pt, pk=pk)
	if request.method == "POST":
		form = PtForm(request.POST, instance=pt)
		if form.is_valid():
			pt = form.save(commit=False)
			pt.idx = request.POST['idx']
			pt.nama = request.POST['nama']
			pt.alamat = request.POST['alamat']
			pt.save()
			return redirect('pt_detail', pk=pt.pk)
	else:
		form = PtForm(instance=pt)
	return render(request, 'home/pt_edit.html', {'form': form})

# ----------------------------------------------------------- Pts
from .pts_forms import PtsForm
from db.models import Pts

def pts_list(request):
	if request.user.has_perm('db.change_pts') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if( idx == 0):
		ps = Pts.objects.all().order_by('idx')
	else:	
		ps = Pts.objects.filter(idx=idx).order_by('idx')
	return render(request, 'home/pts_list.html', {'ps': ps})

def pts_detail(request, pk):
	ps = get_object_or_404(Pts, pk=pk)
	return render(request, 'home/pts_detail.html', {'ps': ps})

def pts_new(request):
	if request.user.has_perm('db.add_pts') is False:
		return render(request, 'home/taek.html', {})
	if request.method == "POST":
		form = PtsForm(request.POST)
		if form.is_valid():
			ps = form.save(commit=False)
			ps.idx = request.POST['idx']
			ps.nama = request.POST['nama']
			ps.namapanjang = request.POST['namapanjang']
			ps.catatan = request.POST['catatan']
			ps.pt_id = request.POST['pt']
			ps.save()
			return redirect('pts_detail', pk=ps.pk)
	else:
		form = PtsForm()
	return render(request, 'home/pts_edit.html', {'form': form})

def pts_edit(request, pk):
	ps = get_object_or_404(Pts, pk=pk)
	if request.method == "POST":
		form = PtsForm(request.POST, instance=ps)
		if form.is_valid():
			ps = form.save(commit=False)
			ps.idx = request.POST['idx']
			ps.nama = request.POST['nama']
			ps.namapanjang = request.POST['namapanjang']
			ps.catatan = request.POST['catatan']
			ps.pt_id = request.POST['pt']
			pts.save()
			return redirect('pts_detail', pk=ps.pk)
	else:
		form = PtsForm(instance=ps)
	return render(request, 'home/pts_edit.html', {'form': form})

# --------------------------------------------------------- Prodi
from .prod_forms import ProdiForm
from db.models import Prodi

def prod_list(request):
	if request.user.has_perm('db.change_prodi') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if( idx == 0):
		pr = Prodi.objects.all().order_by('idx')
	else:	
		pr = Prodi.objects.filter(pts_id=idx).order_by('idx')
	return render(request, 'home/prod_list.html', {'pr': pr})

def prod_detail(request, pk):
	pr = get_object_or_404(Prodi, pk=pk)
	return render(request, 'home/prod_detail.html', {'pr': pr})

def prod_new(request):
	if request.user.has_perm('db.add_prodi') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if request.method == "POST":
		form = ProdiForm(idx, request.POST)
		if form.is_valid():
			pr = form.save(commit=False)
			pr.idx = request.POST['idx']
			pr.nama = request.POST['nama']
			pr.pts_id = request.POST['pts']
			pr.save()
			return redirect('prod_detail', pk=pr.pk)
	else:
		form = ProdiForm(idx,)
	return render(request, 'home/prod_edit.html', {'form': form})

def prod_edit(request, pk):
	pr = get_object_or_404(Prodi, pk=pk)
	idx=pts_id(request)
	if request.method == "POST":
		form = ProdiForm(idx, request.POST, instance=pr)
		if form.is_valid():
			pr = form.save(commit=False)
			pr.idx = request.POST['idx']
			pr.nama = request.POST['nama']
			pr.pts_id = request.POST['pts']
			pr.save()
			return redirect('prod_detail', pk=pr.pk)
	else:
		form = ProdiForm(idx, instance=pr)
	return render(request, 'home/prod_edit.html', {'form': form})

#KEPEGAWAIAN
# ------------------------------------------------------- Pegawai
from .pegw_forms import PegawaiForm
from db.models import Pegawai

def pegw_list(request):
	if request.user.has_perm('db.change_pegawai') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if( idx == 0):
		pg = Pegawai.objects.all().order_by('idx')
	else:
		pg = Pegawai.objects.filter(pts_id=idx).order_by('idx')
	return render(request, 'home/pegw_list.html', {'pg': pg})

def pegw_detail(request, pk):
	pg = get_object_or_404(Pegawai, pk=pk)
	return render(request, 'home/pegw_detail.html', {'pg': pg})

def pegw_new(request):
	if request.user.has_perm('db.add_pegawai') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if request.method == "POST":
		form = PegawaiForm(idx, request.POST)
		if form.is_valid():
			pg = form.save(commit=False)
			pg.nama = request.POST['nama']
			pg.nip = request.POST['nip']
			pg.nidn = request.POST['nidn']
			pg.tanggal = request.POST['tanggal']
			pg.na_titel = request.POST['na_titel']
			pg.na_titel_setara = request.POST['na_titel_setara']
			pg.catatan = request.POST['catatan']
			pg.golpgw_id = request.POST['golpgw']
			pg.grppgw_id = request.POST['grppgw']
			pg.japgw_id = request.POST['japgw']
			pg.pts_id = request.POST['pts']
			pg.status_id = request.POST['status']
			pg.save()
			return redirect('pegw_detail', pk=pg.pk)
	else:
		form = PegawaiForm(idx,)
	return render(request, 'home/pegw_edit.html', {'form': form})

def pegw_edit(request, pk):
	pg = get_object_or_404(Pegawai, pk=pk)
	idx=pts_id(request)
	if request.method == "POST":
		form = PegawaiForm(idx, request.POST, instance=pg)
		if form.is_valid():
			pg = form.save(commit=False)
			pg.nama = request.POST['nama']
			pg.nip = request.POST['nip']
			pg.nidn = request.POST['nidn']
			pg.tanggal = request.POST['tanggal']
			pg.na_titel = request.POST['na_titel']
			pg.na_titel_setara = request.POST['na_titel_setara']
			pg.catatan = request.POST['catatan']
			pg.golpgw_id = request.POST['golpgw']
			pg.grppgw_id = request.POST['grppgw']
			pg.japgw_id = request.POST['japgw']
			pg.pts_id = request.POST['pts']
			pg.status_id = request.POST['status']
			pg.save()
			return redirect('pegw_detail', pk=pg.pk)
	else:
		form = PegawaiForm(idx, instance=pg)
	return render(request, 'home/pegw_edit.html', {'form': form})

# ------------------------------------------------------------ Sk
from .sk_forms import SkForm
from db.models import Sk

def sk_list(request):
	if request.user.has_perm('db.change_sk') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if( idx == 0):
		sk = Sk.objects.all().order_by('idx')
	else:
		idpgw=Pegawai.objects.raw('SELECT idx FROM db_pegawai WHERE pts_id = ' + str(ptsid))
		sk = Sk.objects.filter(pegawai_id__in=idpgw).order_by('idx')
	return render(request, 'home/sk_list.html', {'sk': sk})

def sk_detail(request, pk):
	sk = get_object_or_404(Sk, pk=pk)
	return render(request, 'home/sk_detail.html', {'sk': sk})

def sk_new(request):
	if request.user.has_perm('db.add_sk') is False:
		return render(request, 'home/taek.html', {})
	if request.method == "POST":
		form = SkForm(request.POST)
		if form.is_valid():
			sk = form.save(commit=False)
			sk.nr_sk = request.POST['nr_sk']
			sk.nr_kk = request.POST['nr_kk']
			sk.judul = request.POST['judul']
			sk.tanggal = request.POST['tanggal'] 
			sk.catatan = request.POST['catatan'] 
			sk.pegawai_id = request.POST['pegawai'] 
			sk.status_id = request.POST['status']
			sk.save()
			return redirect('pt_detail', pk=sk.pk)
	else:
		form = SkForm()
	return render(request, 'home/sk_edit.html', {'form': form})

def sk_edit(request, pk):
	sk = get_object_or_404(Sk, pk=pk)
	if request.method == "POST":
		form = SkForm(request.POST, instance=sk)
		if form.is_valid():
			sk = form.save(commit=False)
			sk.nr_sk = request.POST['nr_sk']
			sk.nr_kk = request.POST['nr_kk']
			sk.judul = request.POST['judul']
			sk.tanggal = request.POST['tanggal'] 
			sk.catatan = request.POST['catatan'] 
			sk.pegawai_id = request.POST['pegawai'] 
			sk.status_id = request.POST['status']
			sk.save()
			return redirect('sk_detail', pk=sk.pk)
	else:
		form = SkForm(instance=sk)
	return render(request, 'home/sk_edit.html', {'form': form})

#KEAKADEMIAN
# --------------------------------------------------------- Takrs
from .tkrs_forms import TakrsForm
from db.models import Takrs

def tkrs_list(request):
	if request.user.has_perm('db.change_takrs') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if( idx == 0):
		tk = Takrs.objects.all().order_by('idx')
	else:
		tk = Takrs.objects.filter(pts_id=idx).order_by('idx')
	return render(request, 'home/tkrs_list.html', {'tk': tk})

def tkrs_detail(request, pk):
	tk = get_object_or_404(Takrs, pk=pk)
	return render(request, 'home/tkrs_detail.html', {'tk': tk})

def tkrs_new(request):
	if request.user.has_perm('db.add_takrs') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if request.method == "POST":
		form = TakrsForm(idx, request.POST)
		if form.is_valid():
			tk = form.save(commit=False)
			tk.tahunakademik = request.POST['tahunakademik'] 
			tk.tgldaftarA = request.POST['tgldaftarA']
			tk.tgldaftarB = request.POST['tgldaftarB']
			tk.tglubahA = request.POST['tglubahA']
			tk.tglubahB = request.POST['tglubahB']
			tk.tglkuliahA = request.POST['tglkuliahA']
			tk.tglkuliahB = request.POST['tglkuliahB']
			tk.pts_id = request.POST['pts']
			tk.save()
			return redirect('tkrs_detail', pk=tk.pk)
	else:
		form = TakrsForm(idx,)
	return render(request, 'home/tkrs_edit.html', {'form': form})

def tkrs_edit(request, pk):
	tk = get_object_or_404(Takrs, pk=pk)
	idx=pts_id(request)
	if request.method == "POST":
		form = TakrsForm(idx, request.POST, instance=tk)
		if form.is_valid():
			tk = form.save(commit=False)
			tk.tahunakademik = request.POST['tahunakademik'] 
			tk.tgldaftarA = request.POST['tgldaftarA']
			tk.tgldaftarB = request.POST['tgldaftarB']
			tk.tglubahA = request.POST['tglubahA']
			tk.tglubahB = request.POST['tglubahB']
			tk.tglkuliahA = request.POST['tglkuliahA']
			tk.tglkuliahB = request.POST['tglkuliahB']
			tk.pts_id = request.POST['pts']
			tk.save()
			return redirect('tkrs_detail', pk=tk.pk)
	else:
		form = TakrsForm(idx, instance=tk)
	return render(request, 'home/tkrs_edit.html', {'form': form})

# ---------------------------------------------------- Matakuliah
from .mkul_forms import MatakuliahForm
from db.models import Matakuliah

def mkul_list(request):
	if request.user.has_perm('db.change_matakuliah') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if( idx == 0):
		mk = Matakuliah.objects.all().order_by('idx')
	else:
		mk = Matakuliah.objects.filter(pts_id=idx).order_by('idx')
	return render(request, 'home/mkul_list.html', {'mk': mk})

def mkul_detail(request, pk):
	mk = get_object_or_404(Matakuliah, pk=pk)
	return render(request, 'home/mkul_detail.html', {'mk': mk})

def mkul_new(request):
	if request.user.has_perm('db.add_matakuliah') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if request.method == "POST":
		form = MatakuliahForm(idx, request.POST)
		if form.is_valid():
			mk = form.save(commit=False)
			mk.kode = request.POST['kode']
			mk.nama = request.POST['nama']
			mk.t_id = request.POST['t']
			mk.p_id = request.POST['p']
			mk.k_id = request.POST['k']
			mk.pts_id = request.POST['pts']
			mk.semester_id = request.POST['semester']
			mk.save()
			return redirect('mkul_detail', pk=mk.pk)
	else:
		form = MatakuliahForm(idx,)
	return render(request, 'home/mkul_edit.html', {'form': form})

def mkul_edit(request, pk):
	mk = get_object_or_404(Matakuliah, pk=pk)
	idx=pts_id(request)
	if request.method == "POST":
		form = MatakuliahForm(idx, request.POST, instance=mk)
		if form.is_valid():
			mk = form.save(commit=False)
			mk.kode = request.POST['kode']
			mk.nama = request.POST['nama']
			mk.t_id = request.POST['t']
			mk.p_id = request.POST['p']
			mk.k_id = request.POST['k']
			mk.pts_id = request.POST['pts']
			mk.semester_id = request.POST['semester']
			mk.save()
			return redirect('mkul_detail', pk=mk.pk)
	else:
		form = MatakuliahForm(idx, instance=mk)
	return render(request, 'home/mkul_edit.html', {'form': form})

# ------------------------------------------------- Tugasmengajar
from .tugm_forms import TugasmengajarForm
from db.models import Tugasmengajar

def tugm_list(request):
	if request.user.has_perm('db.change_tugasmengajar') is False:
		return render(request, 'home/taek.html', {})
	tg = Tugasmengajar.objects.all().order_by('idx')
	return render(request, 'home/tugm_list.html', {'tg': tg})

def tugm_detail(request, pk):
	tg = get_object_or_404(Tugasmengajar, pk=pk)
	return render(request, 'home/tugm_detail.html', {'tg': tg})

def tugm_new(request):
	if request.user.has_perm('db.add_tugasmengajar') is False:
		return render(request, 'home/taek.html', {})
	if request.method == "POST":
		form = TugasmengajarForm(request.POST)
		if form.is_valid():
			tg = form.save(commit=False)
			tg.sks = request.POST['sks'] 
			tg.tahunakademik = request.POST['tahunakademik']
			tg.dayatampung = request.POST['dayatampung']
			tg.dosen_id = request.POST['dosen']
			tg.kelompok_id = request.POST['kelompok']
			tg.matakuliah_id = request.POST['matakuliah']
			tg.save()
			return redirect('tugm_detail', pk=tg.pk)
	else:
		form = TugasmengajarForm()
	return render(request, 'home/tugm_edit.html', {'form': form})

def tugm_edit(request, pk):
	tg = get_object_or_404(Tugasmengajar, pk=pk)
	if request.method == "POST":
		form = TugasmengajarForm(request.POST, instance=tg)
		if form.is_valid():
			tg = form.save(commit=False)
			tg.sks = request.POST['sks'] 
			tg.tahunakademik = request.POST['tahunakademik']
			tg.dayatampung = request.POST['dayatampung']
			tg.dosen_id = request.POST['dosen']
			tg.kelompok_id = request.POST['kelompok']
			tg.matakuliah_id = request.POST['matakuliah']
			tg.save()
			return redirect('tugm_detail', pk=tg.pk)
	else:
		form = TugasmengajarForm(instance=tg)
	return render(request, 'home/tugm_edit.html', {'form': form})

# ---------------------------------------------------- Pembimbing
from .pemb_forms import PembimbingForm
from db.models import Pembimbing

def pemb_list(request):
	if request.user.has_perm('db.change_pembimbing') is False:
		return render(request, 'home/taek.html', {})
	pe = Pembimbing.objects.all().order_by('idx')
	return render(request, 'home/pemb_list.html', {'pe': pe})

def pemb_detail(request, pk):
	pe = get_object_or_404(Pembimbing, pk=pk)
	return render(request, 'home/pemb_detail.html', {'pe': pe})

def pemb_new(request):
	if request.user.has_perm('db.add_pembimbing') is False:
		return render(request, 'home/taek.html', {})
	if request.method == "POST":
		form = PembimbingForm(request.POST)
		if form.is_valid():
			pe = form.save(commit=False)
			pe.tanggal = request.POST['tanggal'] 
			pe.dosen_id = request.POST['dosen'] 
			pe.mahasiswa_id = request.POST['mahasiswa']
			pe.status_id = request.POST['status']
			pe.save()
			return redirect('pemb_detail', pk=pe.pk)
	else:
		form = PembimbingForm()
	return render(request, 'home/pemb_edit.html', {'form': form})

def pemb_edit(request, pk):
	pe = get_object_or_404(Pembimbing, pk=pk)
	if request.method == "POST":
		form = PembimbingForm(request.POST, instance=pe)
		if form.is_valid():
			pe = form.save(commit=False)
			pe.tanggal = request.POST['tanggal'] 
			pe.dosen_id = request.POST['dosen'] 
			pe.mahasiswa_id = request.POST['mahasiswa']
			pe.status_id = request.POST['status']
			pe.save()
			return redirect('pemb_detail', pk=pe.pk)
	else:
		form = PembimbingForm(instance=pe)
	return render(request, 'home/pemb_edit.html', {'form': form})

# ----------------------------------------------------- Kelulusan
from .kelu_forms import KelulusanForm
from db.models import Kelulusan

def kelu_list(request):
	if request.user.has_perm('db.change_kelulusan') is False:
		return render(request, 'home/taek.html', {})
	ke = Kelulusan.objects.all().order_by('idx')
	return render(request, 'home/kelu_list.html', {'ke': ke})

def kelu_detail(request, pk):
	ke = get_object_or_404(Kelulusan, pk=pk)
	return render(request, 'home/kelu_detail.html', {'ke': ke})

def kelu_new(request):
	if request.user.has_perm('db.add_kelulusan') is False:
		return render(request, 'home/taek.html', {})
	if request.method == "POST":
		form = KelulusanForm(request.POST)
		if form.is_valid():
			ke = form.save(commit=False)
			ke.mahasiswa_id = request.POST['mahasiswa']
			ke.nr_transkrip = request.POST['nr_transkrip']
			ke.judul1 = request.POST['judul1']
			ke.judul2 = request.POST['judul2']
			ke.ipk = request.POST['ipk']
			ke.tgl_yudisium = request.POST['tgl_yudisium']
			ke.wisuda_id = request.POST['wisuda']
			ke.catatan = request.POST['catatan']
			ke.save()
			return redirect('kelu_detail', pk=ke.pk)
	else:
		form = KelulusanForm()
	return render(request, 'home/kelu_edit.html', {'form': form})

def kelu_edit(request, pk):
	ke = get_object_or_404(Kelulusan, pk=pk)
	if request.method == "POST":
		form = KelulusanForm(request.POST, instance=ke)
		if form.is_valid():
			ke = form.save(commit=False)
			ke.mahasiswa_id = request.POST['mahasiswa']
			ke.nr_transkrip = request.POST['nr_transkrip']
			ke.judul1 = request.POST['judul1']
			ke.judul2 = request.POST['judul2']
			ke.ipk = request.POST['ipk']
			ke.tgl_yudisium = request.POST['tgl_yudisium']
			ke.wisuda_id = request.POST['wisuda']
			ke.catatan = request.POST['catatan']
			ke.save()
			return redirect('kelu_detail', pk=ke.pk)
	else:
		form = KelulusanForm(instance=ke)
	return render(request, 'home/kelu_edit.html', {'form': form})

# ----------------------------------------------------------- KHS
from .khs_forms import KhsForm
from db.models import Khs

def khs_list(request):
	if request.user.has_perm('db.change_khs') is False:
		return render(request, 'home/taek.html', {})
	kh = Khs.objects.all().order_by('idx')
	return render(request, 'home/khs_list.html', {'kh': kh})

def khs_detail(request, pk):
	kh = get_object_or_404(Khs, pk=pk)
	return render(request, 'home/khs_detail.html', {'kh': kh})

def khs_new(request):
	if request.user.has_perm('db.add_khs') is False:
		return render(request, 'home/taek.html', {})
	if request.method == "POST":
		form = KhsForm(request.POST)
		if form.is_valid():
			kh = form.save(commit=False)
			kh.krs_id = request.POST['krs']
			kh.tanggal = request.POST['tanggal']
			kh.ip = request.POST['ip']
			kh.save()
			return redirect('khs_detail', pk=kh.pk)
	else:
		form = KhsForm()
	return render(request, 'home/khs_edit.html', {'form': form})

def khs_edit(request, pk):
	kh = get_object_or_404(Khs, pk=pk)
	if request.method == "POST":
		form = KhsForm(request.POST, instance=kh)
		if form.is_valid():
			kh = form.save(commit=False)
			kh.krs_id = request.POST['krs']
			kh.tanggal = request.POST['tanggal']
			kh.ip = request.POST['ip']
			kh.save()
			return redirect('kelu_detail', pk=kh.pk)
	else:
		form = KhsForm(instance=kh)
	return render(request, 'home/khs_edit.html', {'form': form})

# -------------------------------------------------------- Ijazah
from .ijaz_forms import IjazahForm
from db.models import Ijazah

def ijaz_list(request):
	if request.user.has_perm('db.change_ijazah') is False:
		return render(request, 'home/taek.html', {})
	ij = Ijazah.objects.all().order_by('idx')
	return render(request, 'home/ijaz_list.html', {'ij': ij})

def ijaz_detail(request, pk):
	ij = get_object_or_404(Ijazah, pk=pk)
	return render(request, 'home/ijaz_detail.html', {'ij': ij})

def ijaz_new(request):
	if request.user.has_perm('db.add_ijazah') is False:
		return render(request, 'home/taek.html', {})
	if request.method == "POST":
		form = IjazahForm(request.POST)
		if form.is_valid():
			ij = form.save(commit=False)
			ij.mahasiswa_id = request.POST['mahasiswa']
			ij.nomor = request.POST['nomor']
			ij.nr_seri = request.POST['nr_seri']
			ij.status_id = request.POST['status']
			ij.catatan = request.POST['catatan']
			ij.ijazah_id = request.POST['ijazah']
			ij.save()
			return redirect('ijaz_detail', pk=ij.pk)
	else:
		form = IjazahForm()
	return render(request, 'home/ijaz_edit.html', {'form': form})

def ijaz_edit(request, pk):
	ij = get_object_or_404(Ijazah, pk=pk)
	if request.method == "POST":
		form = IjazahForm(request.POST, instance=ij)
		if form.is_valid():
			ij.mahasiswa_id = request.POST['mahasiswa']
			ij.nomor = request.POST['nomor']
			ij.nr_seri = request.POST['nr_seri']
			ij.status_id = request.POST['status']
			ij.catatan = request.POST['catatan']
			ij.ijazah_id = request.POST['ijazah']
			ij.save()
			return redirect('ijaz_detail', pk=ij.pk)
	else:
		form = IjazForm(instance=ij)
	return render(request, 'home/ijaz_edit.html', {'form': form})

#KEMAHASISWAAN
# ----------------------------------------------------- Mahasiswa
from .maha_forms import MahasiswaForm
from db.models import Mahasiswa

def maha_list(request):
	if request.user.has_perm('db.change_mahasiswa') is False:
		return render(request, 'home/taek.html', {})
	ma = Mahasiswa.objects.all().order_by('idx')
	return render(request, 'home/maha_list.html', {'ma': ma})

def maha_detail(request, pk):
	ma = get_object_or_404(Mahasiswa, pk=pk)
	return render(request, 'home/maha_detail.html', {'ma': ma})

def maha_new(request):
	if request.user.has_perm('db.add_mahasiswa') is False:
		return render(request, 'home/taek.html', {})
	idx=pts_id(request)
	if request.method == "POST":
		form = MahasiswaForm(idx, request.POST)
		if form.is_valid():
			ma = form.save(commit=False)
			ma.nim = request.POST['nim']
			ma.nama = request.POST['nama']
			ma.angkatan = request.POST['angkatan']
			ma.sks = request.POST['sks']
			ma.catatan = request.POST['catatan']
			ma.konversi_id = request.POST['konversi']
			ma.pts_id = request.POST['pts']
			ma.prodi_id = request.POST['prodi']
			ma.status_id = request.POST['status']
			ma.save()
			return redirect('maha_detail', pk=ma.pk)
	else:
		form = MahasiswaForm(idx,)
	return render(request, 'home/maha_edit.html', {'form': form})

def maha_edit(request, pk):
	ma = get_object_or_404(Mahasiswa, pk=pk)
	idx=pts_id(request)
	if request.method == "POST":
		form = MahasiswaForm(idx, request.POST, instance=ma)
		if form.is_valid():
			ma = form.save(commit=False)
			ma.nim = request.POST['nim']
			ma.nama = request.POST['nama']			
			ma.angkatan = request.POST['angkatan']
			ma.sks = request.POST['sks']
			ma.catatan = request.POST['catatan']
			ma.konversi_id = request.POST['konversi']
			ma.pts_id = request.POST['pts']
			ma.prodi_id = request.POST['prodi']
			ma.status_id = request.POST['status']
			ma.save()
			return redirect('maha_detail', pk=ma.pk)
	else:
		form = MahasiswaForm(idx, instance=ma)
	return render(request, 'home/maha_edit.html', {'form': form})

# ----------------------------------------------------------- Krs
from .krs_forms import KrsForm
from db.models import Krs

def krs_list(request):
	if request.user.has_perm('db.change_krs') is False:
		return render(request, 'home/taek.html', {})
	kr = Krs.objects.all().order_by('idx')
	return render(request, 'home/krs_list.html', {'kr': kr})

def krs_detail(request, pk):
	kr = get_object_or_404(Krs, pk=pk)
	return render(request, 'home/krs_detail.html', {'kr': kr})

def krs_new(request):
	if request.user.has_perm('db.add_krs') is False:
		return render(request, 'home/taek.html', {})
	if request.method == "POST":
		form = KrsForm(request.POST)
		if form.is_valid():
			kr = form.save(commit=False)
			kr.takrs_id = request.POST['takrs']
			kr.mahasiswa_id = request.POST['mahasiswa']
			kr.kelompok_id = request.POST['kelompok']
			kr.tanggal = request.POST['tanggal']
			kr.save()
			return redirect('krs_detail', pk=kr.pk)
	else:
		form = KrsForm()
	return render(request, 'home/krs_edit.html', {'form': form})

def krs_edit(request, pk):
	kr = get_object_or_404(Krs, pk=pk)
	idx=pts_id(request)
	if request.method == "POST":
		form = KrsForm(idx, request.POST, instance=kr)
		if form.is_valid():
			kr = form.save(commit=False)
			kr.takrs_id = request.POST['takrs']
			kr.mahasiswa_id = request.POST['mahasiswa']
			kr.kelompok_id = request.POST['kelompok']
			kr.tanggal = request.POST['tanggal']
			kr.save()
			return redirect('krs_detail', pk=kr.pk)
	else:
		form = KrsForm(idx, instance=kr)
	return render(request, 'home/krs_edit.html', {'form': form})

# ---------------------------------------------------- Pembayaran
from .pbay_forms import PembayaranForm
from db.models import Pembayaran

def pbay_list(request):
	if request.user.has_perm('db.change_pembayaran') is False:
		return render(request, 'home/taek.html', {})
	pb = Pembayaran.objects.all().order_by('idx')
	return render(request, 'home/pbay_list.html', {'pb': pb})

def pbay_detail(request, pk):
	pb = get_object_or_404(Pembayaran, pk=pk)
	return render(request, 'home/pbay_detail.html', {'pb': pb})

def pbay_new(request):
	if request.user.has_perm('db.add_pembayaran') is False:
		return render(request, 'home/taek.html', {})
	if request.method == "POST":
		form = PembayaranForm(request.POST)
		if form.is_valid():
			pb = form.save(commit=False)
			pb.tanggal = request.POST['tanggal']
			pb.jenis = request.POST['jenis']
			pb.nr_validasi = request.POST['nr_validasi']
			pb.mahasiswa_id = request.POST['mahasiswa']
			pb.save()
			return redirect('pbay_detail', pk=pb.pk)
	else:
		form = PembayaranForm()
	return render(request, 'home/pbay_edit.html', {'form': form})

def pbay_edit(request, pk):
	pb = get_object_or_404(Pembayaran, pk=pk)
	if request.method == "POST":
		form = PembayaranForm(request.POST, instance=pb)
		if form.is_valid():
			pb = form.save(commit=False)
			pb.tanggal = request.POST['tanggal']
			pb.jenis = request.POST['jenis']
			pb.nr_validasi = request.POST['nr_validasi']
			pb.mahasiswa_id = request.POST['mahasiswa']
			pb.save()
			return redirect('pbay_detail', pk=pb.pk)
	else:
		form = PembayaranForm(instance=pb)
	return render(request, 'home/pbay_edit.html', {'form': form})

# ---------------------------------------------------------- Info

def info(request):
	return render(request, 'home/info.html', {})

