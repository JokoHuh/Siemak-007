# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-11 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fix1',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fix2',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Fix3',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Fix4',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fix5',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Fix6',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fix7',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fix8',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fix9',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Golpgw',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Grppgw',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ijazah',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('nomor', models.CharField(default='', max_length=30)),
                ('nr_seri', models.CharField(default='', max_length=30)),
                ('catatan', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Itemkhs',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('quis', models.IntegerField(default=0)),
                ('tugas', models.IntegerField(default=0)),
                ('mid', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('hasilmutu', models.CharField(max_length=1)),
                ('ikutujian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix3')),
            ],
        ),
        migrations.CreateModel(
            name='Itemkrs',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Japgw',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Kelompok',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Kelulusan',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('nr_transkrip', models.CharField(max_length=20, null=True)),
                ('judul1', models.TextField(null=True)),
                ('judul2', models.TextField(null=True)),
                ('ipk', models.FloatField(default=0.0)),
                ('tgl_yudisium', models.DateField(null=True)),
                ('catatan', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Khs',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal', models.DateField(null=True)),
                ('ip', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Krs',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal', models.DateField()),
                ('kelompok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Kelompok')),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('nim', models.CharField(max_length=30, null=True, unique=True)),
                ('nama', models.CharField(max_length=100)),
                ('angkatan', models.IntegerField(default=0)),
                ('sks', models.IntegerField(default=0)),
                ('catatan', models.TextField()),
                ('konversi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix3')),
            ],
        ),
        migrations.CreateModel(
            name='Matakuliah',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('kode', models.CharField(max_length=15)),
                ('nama', models.CharField(max_length=50)),
                ('k', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='kerja', to='db.Fix3')),
                ('p', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='praktek', to='db.Fix3')),
            ],
        ),
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=80)),
                ('nip', models.CharField(max_length=20)),
                ('nidn', models.CharField(max_length=20)),
                ('tanggal', models.DateField()),
                ('na_titel', models.CharField(max_length=50)),
                ('na_titel_setara', models.CharField(max_length=50)),
                ('catatan', models.TextField()),
                ('person', models.IntegerField(default=0)),
                ('golpgw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Golpgw')),
                ('grppgw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Grppgw')),
                ('japgw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Japgw')),
            ],
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal', models.DateField()),
                ('jenis', models.CharField(max_length=80)),
                ('nr_validasi', models.CharField(max_length=80)),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Mahasiswa')),
            ],
        ),
        migrations.CreateModel(
            name='Pembimbing',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal', models.DateField(null=True)),
                ('dosen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Pegawai')),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Mahasiswa')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix8')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('infopgw', models.IntegerField(default=0)),
                ('tempat_lhr', models.CharField(max_length=50)),
                ('tanggal_lhr', models.DateField()),
                ('telpon', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=50)),
                ('rtrw', models.CharField(max_length=10)),
                ('kelurahan', models.CharField(max_length=50)),
                ('kecamatan', models.CharField(max_length=50)),
                ('kota', models.CharField(max_length=50)),
                ('propinsi', models.CharField(max_length=50)),
                ('kwrg_negara', models.CharField(max_length=30)),
                ('nr_identitas', models.CharField(max_length=20)),
                ('agama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix9')),
                ('jeniskel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix4')),
                ('ki', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix5')),
            ],
        ),
        migrations.CreateModel(
            name='Prodi',
            fields=[
                ('idx', models.IntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Pt',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=80)),
                ('alamat', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pts',
            fields=[
                ('idx', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=20)),
                ('namapanjang', models.CharField(max_length=200)),
                ('catatan', models.TextField()),
                ('pt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Pt')),
            ],
        ),
        migrations.CreateModel(
            name='Sk',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('nr_sk', models.CharField(max_length=50)),
                ('nr_kk', models.CharField(default=0, max_length=50)),
                ('judul', models.CharField(max_length=50)),
                ('tanggal', models.DateField()),
                ('catatan', models.TextField()),
                ('pegawai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Pegawai')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix2')),
            ],
        ),
        migrations.CreateModel(
            name='Takrs',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('tahunakademik', models.IntegerField(default=0)),
                ('tgldaftarA', models.DateField(null=True)),
                ('tgldaftarB', models.DateField(null=True)),
                ('tglubahA', models.DateField(null=True)),
                ('tglubahB', models.DateField(null=True)),
                ('tglkuliahA', models.DateField(null=True)),
                ('tglkuliahB', models.DateField(null=True)),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Prodi')),
            ],
        ),
        migrations.CreateModel(
            name='Tugasmengajar',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('sks', models.IntegerField(default=0)),
                ('tahunakademik', models.IntegerField(default=0)),
                ('dayatampung', models.IntegerField(default=0)),
                ('dosen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Pegawai')),
                ('kelompok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Kelompok')),
                ('matakuliah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Matakuliah')),
            ],
        ),
        migrations.AddField(
            model_name='prodi',
            name='pts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Pts'),
        ),
        migrations.AddField(
            model_name='pegawai',
            name='pts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Pts'),
        ),
        migrations.AddField(
            model_name='pegawai',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix2'),
        ),
        migrations.AddField(
            model_name='matakuliah',
            name='prodi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Prodi'),
        ),
        migrations.AddField(
            model_name='matakuliah',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix1'),
        ),
        migrations.AddField(
            model_name='matakuliah',
            name='t',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='teori', to='db.Fix3'),
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='prodi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Prodi'),
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix2'),
        ),
        migrations.AddField(
            model_name='krs',
            name='mahasiswa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Mahasiswa'),
        ),
        migrations.AddField(
            model_name='krs',
            name='takrs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Takrs'),
        ),
        migrations.AddField(
            model_name='khs',
            name='krs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Krs'),
        ),
        migrations.AddField(
            model_name='kelulusan',
            name='mahasiswa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Mahasiswa'),
        ),
        migrations.AddField(
            model_name='kelulusan',
            name='wisuda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Fix3'),
        ),
        migrations.AddField(
            model_name='kelompok',
            name='pts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Pts'),
        ),
        migrations.AddField(
            model_name='itemkrs',
            name='krs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Krs'),
        ),
        migrations.AddField(
            model_name='itemkrs',
            name='tugasmengajar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Tugasmengajar'),
        ),
        migrations.AddField(
            model_name='itemkhs',
            name='itemkrs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Itemkrs'),
        ),
        migrations.AddField(
            model_name='ijazah',
            name='mahasiswa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Mahasiswa'),
        ),
        migrations.AddField(
            model_name='ijazah',
            name='status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='db.Fix8'),
        ),
    ]
