from django.db import models

''' KELEM '''

class Pt(models.Model):
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=80)
	alamat = models.CharField(max_length=200)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Pts(models.Model):
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=20)
	namapanjang = models.CharField(max_length=200)
	catatan = models.TextField()
	#logo = models.BinaryField()
	pt = models.ForeignKey('Pt', on_delete=models.CASCADE, null=False)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Prodi(models.Model):
	idx = models.IntegerField(primary_key=True)
	nama = models.CharField(max_length=80)
	pts = models.ForeignKey('Pts', on_delete=models.CASCADE, null=False)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

''' KETEP '''

class Fix1(models.Model): #semester: na/ganjil/genap/pendek
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=10)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Fix2(models.Model): #status mah/pgw: tidak/ada/pindah/dopensiun/keluar
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=6)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Fix3(models.Model): #tidak/ya
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=5)
	
	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Fix4(models.Model): #jeniskelamin: perempuan/laki-laki
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=10)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Fix5(models.Model): #identitas: na/ktp/paspor/sim
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=6)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Fix6(models.Model): #!kelas: reg/non reg/exec/d
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=10)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Fix7(models.Model): #jenis ruang: na/kantor/kuliah/lab/praktikum/seminar/gudang/kantin/wc/rapat
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=20)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)
	
class Fix8(models.Model): #status ijazah: belum/asli/copy/duplikat
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=30)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Fix9(models.Model): #agama
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=30)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Kelompok(models.Model): #pengganti Fix6
	idx = models.SmallIntegerField(primary_key=True)
	pts = models.ForeignKey('Pts', on_delete=models.CASCADE, null=True) # Kenapa null=True ?
	nama = models.CharField(max_length=12)

	def __str__(self):
		return '%d-%s-%s' % (self.idx, self.pts, self.nama)

class Grppgw(models.Model):
	''' grup pegawai '''
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=20)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Golpgw(models.Model):
	''' golongan pegawai '''
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=20)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Japgw(models.Model):
	''' JA pegawai'''
	idx = models.SmallIntegerField(primary_key=True)
	nama = models.CharField(max_length=20)

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

''' KEPEG '''

class Person(models.Model):
	idx = models.AutoField(primary_key=True)
	infopgw = models.IntegerField(default=0)
	tempat_lhr = models.CharField(max_length=50)
	tanggal_lhr = models.DateField(auto_now=False)
	jeniskel = models.ForeignKey('Fix4', on_delete=models.CASCADE)
	telpon = models.CharField(max_length=50)
	alamat = models.CharField(max_length=50)
	rtrw = models.CharField(max_length=10)
	kelurahan = models.CharField(max_length=50)
	kecamatan = models.CharField(max_length=50)
	kota = models.CharField(max_length=50)
	propinsi = models.CharField(max_length=50)
	agama = models.ForeignKey('Fix9', on_delete=models.CASCADE)
	kwrg_negara = models.CharField(max_length=30)
	ki = models.ForeignKey('Fix5', on_delete=models.CASCADE)
	nr_identitas = models.CharField(max_length=20)

	def __str__(self):
		return 'idx=%d-tempat lahir=%s-tanggal lahir=%s-kelamin=%s-alamat=%s' % (self.idx, self.tempat_lhr, self.tanggal_lhr, self.jeniskel, self.alamat)

class Pegawai(models.Model):
	idx = models.AutoField(primary_key=True)
	nama = models.CharField(max_length=80)
	nip = models.CharField(max_length=20)
	nidn = models.CharField(max_length=20)
	pts = models.ForeignKey('Pts', on_delete=models.CASCADE)
	grppgw = models.ForeignKey('Grppgw', on_delete=models.CASCADE)
	tanggal = models.DateField(auto_now=False)
	golpgw = models.ForeignKey('Golpgw', on_delete=models.CASCADE)
	japgw = models.ForeignKey('Japgw', on_delete=models.CASCADE)
	na_titel = models.CharField(max_length=50)
	na_titel_setara = models.CharField(max_length=50)
	catatan = models.TextField()
	status = models.ForeignKey('Fix2', on_delete=models.CASCADE)
	person = models.IntegerField(default=0) # ini tidak digunakan, digantikan dengan person.infopgw

	def __str__(self):
		return '%d-%s' % (self.idx, self.nama)

class Sk(models.Model):
	idx = models.AutoField(primary_key=True)
	nr_sk = models.CharField(max_length=50)
	nr_kk = models.CharField(max_length=50, default=0)
	judul = models.CharField(max_length=50)
	tanggal = models.DateField(auto_now=False)
	catatan = models.TextField()
	status = models.ForeignKey('Fix2', on_delete=models.CASCADE)
	pegawai = models.ForeignKey('Pegawai', on_delete=models.CASCADE)

	def __str__(self):
		return '%d-%s-%s' % (self.idx, self.nr_sk, self.tanggal)

''' KEMAH '''

class Mahasiswa(models.Model):
	idx = models.AutoField(primary_key=True)
	nim = models.CharField(max_length=30, unique=True, null=True)
	nama = models.CharField(max_length=100)
	status = models.ForeignKey('Fix2', on_delete=models.CASCADE)
	pts = models.ForeignKey('Pts', on_delete=models.CASCADE, default=0)
	prodi = models.ForeignKey('Prodi', on_delete=models.CASCADE, default=0)
	angkatan = models.IntegerField(default=0)
	konversi = models.ForeignKey('Fix3', on_delete=models.CASCADE)
	sks = models.IntegerField(default=0)
	catatan = models.TextField()
	
	def __str__(self):
		return '%s-%s-%d' % (self.nim, self.nama, self.angkatan)

class Krs(models.Model):
	idx = models.AutoField(primary_key=True)
	takrs = models.ForeignKey('Takrs', on_delete=models.CASCADE)
	mahasiswa = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)
	kelompok = models.ForeignKey('Kelompok', on_delete=models.CASCADE)
	tanggal = models.DateField(auto_now=False)

	def __str__(self):
		return '%s-%s' % (self.takrs.tahunakademik, self.mahasiswa.nama)

class Itemkrs(models.Model):
	idx = models.AutoField(primary_key=True)
	krs = models.ForeignKey('Krs', on_delete=models.CASCADE)
	tugasmengajar = models.ForeignKey('Tugasmengajar', on_delete=models.CASCADE)

class Pembayaran(models.Model):
	idx = models.AutoField(primary_key=True)
	tanggal = models.DateField(auto_now=False)
	jenis = models.CharField(max_length=80)
	nr_validasi = models.CharField(max_length=80)
	mahasiswa = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)

''' KEAKA '''

class Takrs(models.Model):
	idx = models.AutoField(primary_key=True)
	pts = models.ForeignKey('Pts', on_delete=models.CASCADE, default=0)
	tahunakademik = models.IntegerField(default=0)
	tgldaftarA = models.DateField(null=True)
	tgldaftarB = models.DateField(null=True)
	tglubahA = models.DateField(null=True)
	tglubahB = models.DateField(null=True)
	tglkuliahA = models.DateField(null=True)
	tglkuliahB = models.DateField(null=True)

	def __str__(self):
		return '%s-%d' % (self.pts.nama, self.tahunakademik)

class Matakuliah(models.Model):
	idx = models.AutoField(primary_key=True)
	kode = models.CharField(max_length=15)
	nama = models.CharField(max_length=50)
	t = models.ForeignKey('Fix3', default=0, related_name='teori')
	p = models.ForeignKey('Fix3', default=0, related_name='praktek')
	k = models.ForeignKey('Fix3', default=0, related_name='kerja')
	semester = models.ForeignKey('Fix1', on_delete=models.CASCADE)
	pts = models.ForeignKey('Pts', on_delete=models.CASCADE, default=0)
	prodi = models.ForeignKey('Prodi', on_delete=models.CASCADE, default=0)
	
	def __str__(self):
		return '%d-%s-%s' % (self.idx, self.kode, self.nama, self.semester)

class Tugasmengajar(models.Model):
	idx = models.AutoField(primary_key=True)
	dosen = models.ForeignKey('Pegawai', on_delete=models.CASCADE, null=True)
	matakuliah = models.ForeignKey('Matakuliah', on_delete=models.CASCADE)
	sks = models.IntegerField(default=0)
	tahunakademik = models.IntegerField(default=0)
	dayatampung = models.IntegerField(default=0)
	kelompok = models.ForeignKey('Kelompok', on_delete=models.CASCADE)

class Ijazah(models.Model):
	idx = models.AutoField(primary_key=True)
	nomor = models.CharField(max_length=30, default='')
	nr_seri = models.CharField(max_length=30, default='')
	catatan = models.TextField(default='')
	status = models.ForeignKey('Fix8', on_delete=models.CASCADE, default=0)
	mahasiswa = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)	

class Pembimbing(models.Model):
	idx = models.AutoField(primary_key=True)
	mahasiswa = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)
	tanggal = models.DateField(null=True)
	dosen = models.ForeignKey('Pegawai', on_delete=models.CASCADE, null=True)
	status = models.ForeignKey('Fix8', on_delete=models.CASCADE)

class Kelulusan(models.Model):
	idx = models.AutoField(primary_key=True)
	mahasiswa = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)
	nr_transkrip = models.CharField(max_length=20, null=True)
	judul1 = models.TextField(null=True)
	judul2 = models.TextField(null=True)
	ipk = models.FloatField(default=0.0)
	tgl_yudisium = models.DateField(null=True)
	wisuda = models.ForeignKey('Fix3', on_delete=models.CASCADE)
	catatan = models.TextField(null=True)

class Khs(models.Model):
	idx = models.AutoField(primary_key=True)
	krs = models.ForeignKey('Krs', on_delete=models.CASCADE)
	tanggal = models.DateField(null=True)
	ip = models.FloatField(default=0)

class Itemkhs(models.Model):
	idx = models.AutoField(primary_key=True)
	itemkrs = models.ForeignKey('Itemkrs', on_delete=models.CASCADE)
	quis = models.IntegerField(default=0)
	tugas = models.IntegerField(default=0)
	mid = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	hasilmutu = models.CharField(max_length=1)
	ikutujian = models.ForeignKey('Fix3', on_delete=models.CASCADE)

''' KEDER '''

''' VIEW '''



