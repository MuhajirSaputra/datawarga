# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=15, verbose_name=b'Desa')),
            ],
            options={
                'verbose_name': 'Desa',
                'verbose_name_plural': 'Desa',
            },
        ),
        migrations.CreateModel(
            name='DocImigrasi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=12, verbose_name=b'Dokumen Imigrasi')),
            ],
            options={
                'verbose_name': 'Dokumen',
                'verbose_name_plural': 'Dokumen',
            },
        ),
        migrations.CreateModel(
            name='Kabupaten',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=15, verbose_name=b'Kabupaten')),
            ],
            options={
                'verbose_name': 'Kabupaten',
                'verbose_name_plural': 'Kabupaten',
            },
        ),
        migrations.CreateModel(
            name='KaKel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_kk', models.CharField(unique=True, max_length=16, verbose_name=b'Nomor KK')),
                ('head_kk', models.CharField(max_length=20, verbose_name=b'Kepala Keluarga')),
                ('alamat', models.TextField(verbose_name=b'Alamat')),
                ('kodepos', models.TextField(max_length=8, verbose_name=b'Kode Pos', blank=True)),
                ('desa', models.ForeignKey(verbose_name=b'DESA', to='datawarga.Desa', null=True)),
                ('kabupaten', models.ForeignKey(verbose_name=b'KABUPATEN', to='datawarga.Kabupaten', null=True)),
            ],
            options={
                'verbose_name': 'KaKel',
                'verbose_name_plural': 'Kartu Keluarga',
            },
        ),
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=15, verbose_name=b'Kecamatan')),
            ],
            options={
                'verbose_name': 'Kecamatan',
                'verbose_name_plural': 'Kecamatan',
            },
        ),
        migrations.CreateModel(
            name='Pekerjaan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=15, verbose_name=b'Jenis Pekerjaan')),
                ('deskripsi', models.TextField(max_length=30, verbose_name=b'Keterangan', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=15, verbose_name=b'Provinsi')),
            ],
            options={
                'verbose_name': 'Provinsi',
                'verbose_name_plural': 'Provinsi',
            },
        ),
        migrations.CreateModel(
            name='Rt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=4, verbose_name=b'RT')),
            ],
            options={
                'verbose_name': 'RT',
                'verbose_name_plural': 'RT',
            },
        ),
        migrations.CreateModel(
            name='Rw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=4, verbose_name=b'Rw')),
            ],
            options={
                'verbose_name': 'RW',
                'verbose_name_plural': 'RW',
            },
        ),
        migrations.CreateModel(
            name='Warga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nik', models.CharField(unique=True, max_length=16, verbose_name=b'NIK')),
                ('firts_name', models.CharField(max_length=20, verbose_name=b'Nama Depan')),
                ('last_name', models.CharField(max_length=30, verbose_name=b'Nama Belakang', blank=True)),
                ('birth_place', models.CharField(max_length=20, verbose_name=b'Tempat Lahir')),
                ('birth_date', models.DateField(verbose_name=b'Tanggal Lahir')),
                ('gender', models.CharField(max_length=1, verbose_name=b'Jenis Kelamin', choices=[(b'L', b'Laki-Laki'), (b'P', b'Perempuan')])),
                ('religion', models.CharField(max_length=6, verbose_name=b'Agama', choices=[(b'IS', b'ISLAM'), (b'KR', b'KRISTEN'), (b'HI', b'HINDU'), (b'BU', b'BUDHA')])),
                ('education', models.CharField(blank=True, max_length=1, verbose_name=b'Pendidikan', choices=[(b'1', b'SD'), (b'2', b'SMP'), (b'3', b'SMA'), (b'4', b'D-1'), (b'5', b'D-2'), (b'6', b'D-3'), (b'7', b'S-1'), (b'8', b'S-2'), (b'9', b'S-3')])),
                ('maried', models.CharField(max_length=2, verbose_name=b'Status Pernikahan', choices=[(b'K', b'KAWIN'), (b'BK', b'BELUM KAWIN'), (b'CM', b'CERAI MATI'), (b'CH', b'CERAI HIDUP')])),
                ('marital', models.CharField(max_length=1, verbose_name=b'Hubungan Keluarga', choices=[(b'S', b'SUAMI'), (b'I', b'ISTRI'), (b'A', b'ANAK')])),
                ('national', models.CharField(max_length=3, verbose_name=b'Kebangsaan', choices=[(b'WNI', b'WNI'), (b'WNA', b'WNA')])),
                ('idimigrasi', models.CharField(unique=True, max_length=15, verbose_name=b'ID Dokumen')),
                ('father_name', models.CharField(max_length=20, verbose_name=b'Nama Ayah')),
                ('mother_name', models.CharField(max_length=20, verbose_name=b'Nama Ibu')),
                ('imigrasi', models.ForeignKey(verbose_name=b'Dokumen Imigrasi', to='datawarga.DocImigrasi')),
            ],
            options={
                'verbose_name': 'Warga',
                'verbose_name_plural': 'Warga',
            },
        ),
        migrations.AddField(
            model_name='kakel',
            name='kecamatan',
            field=models.ForeignKey(verbose_name=b'KECAMATAN', to='datawarga.Kecamatan', null=True),
        ),
        migrations.AddField(
            model_name='kakel',
            name='provinsi',
            field=models.ForeignKey(verbose_name=b'PROVINSI', to='datawarga.Provinsi', null=True),
        ),
        migrations.AddField(
            model_name='kakel',
            name='rt',
            field=models.ForeignKey(verbose_name=b'RT', to='datawarga.Rt', null=True),
        ),
        migrations.AddField(
            model_name='kakel',
            name='rw',
            field=models.ForeignKey(verbose_name=b'RW', to='datawarga.Rw', null=True),
        ),
    ]
