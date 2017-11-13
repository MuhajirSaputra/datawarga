from django.db import models

class Pekerjaan(models.Model):
	nama = models.CharField(verbose_name='Jenis Pekerjaan', max_length=15)
	deskripsi = models.TextField(verbose_name='Keterangan', max_length=30, blank=True)

	def __unicode__(self):
		return self.nama


class DocImigrasi(models.Model):
	nama = models.CharField(verbose_name='Dokumen Imigrasi', max_length=12)

	class Meta:
		verbose_name = 'Dokumen'
		verbose_name_plural = 'Dokumen'

	def __unicode__(self):
		return self.nama


class Rt(models.Model):
	nama = models.CharField(verbose_name='RT', max_length=4)

	class Meta:
		verbose_name = 'RT'
		verbose_name_plural = 'RT'

	def __unicode__(self):
		return self.nama


class Rw(models.Model):
	nama = models.CharField(verbose_name='Rw', max_length=4)

	class Meta:
		verbose_name = 'RW'
		verbose_name_plural = 'RW'

	def __unicode__(self):
		return self.nama


class Desa(models.Model):
	nama = models.CharField(verbose_name='Desa', max_length=15)

	class Meta:
		verbose_name = 'Desa'
		verbose_name_plural = 'Desa'

	def __unicode__(self):
		return self.nama


class Kecamatan(models.Model):
	nama = models.CharField(verbose_name='Kecamatan', max_length=15)

	class Meta:
		verbose_name = 'Kecamatan'
		verbose_name_plural = 'Kecamatan'

	def __unicode__(self):
		return self.nama


class Kabupaten(models.Model):
	nama = models.CharField(verbose_name='Kabupaten', max_length=15)

	class Meta:
		verbose_name = 'Kabupaten'
		verbose_name_plural = 'Kabupaten'

	def __unicode__(self):
		return self.nama


class Provinsi(models.Model):
	nama = models.CharField(verbose_name='Provinsi', max_length=15)

	class Meta:
		verbose_name = 'Provinsi'
		verbose_name_plural = 'Provinsi'

	def __unicode__(self):
		return self.nama


class KaKel(models.Model):
	id_kk = models.CharField(verbose_name='Nomor KK', max_length=16, unique=True)
	head_kk = models.CharField(verbose_name='Kepala Keluarga', max_length=20)
	alamat = models.TextField(verbose_name='Alamat')
	rt = models.ForeignKey(Rt, verbose_name='RT', null=True)
	rw = models.ForeignKey(Rw, verbose_name='RW', null=True)
	desa = models.ForeignKey(Desa, verbose_name='DESA', null=True)
	kecamatan = models.ForeignKey(Kecamatan, verbose_name='KECAMATAN', null=True)
	kabupaten = models.ForeignKey(Kabupaten, verbose_name='KABUPATEN', null=True)
	provinsi = models.ForeignKey(Provinsi, verbose_name='PROVINSI', null=True)
	kodepos = models.TextField(verbose_name='Kode Pos', max_length=8, blank=True)

	class Meta:
		verbose_name = 'KaKel'
		verbose_name_plural = 'Kartu Keluarga'

	def __unicode__(self):
		return self.head_kk


class Warga(models.Model):
	GENDER_CHOICES=(
		('L', 'Laki-Laki'),
		('P', 'Perempuan')
		)
	RELIGION_CHOICES=(
		('IS', 'ISLAM'),
		('KR', 'KRISTEN'),
		('HI', 'HINDU'),
		('BU', 'BUDHA')
		)
	EDUCATION_CHOICES=(
		('1', 'SD'),
		('2', 'SMP'),
		('3', 'SMA'),
		('4', 'D-1'),
		('5', 'D-2'),
		('6', 'D-3'),
		('7', 'S-1'),
		('8', 'S-2'),
		('9', 'S-3')
		)
	MARIED_CHOICES=(
		('K', 'KAWIN'),
		('BK', 'BELUM KAWIN'),
		('CM', 'CERAI MATI'),
		('CH', 'CERAI HIDUP')
		)
	MARITAL_CHOICE=(
		('S', 'SUAMI'),
		('I', 'ISTRI'),
		('A', 'ANAK')
		)
	NATIONAL_CHOICE=(
		('WNI', 'WNI'),
		('WNA', 'WNA')
		)
	nik = models.CharField(verbose_name='NIK', max_length=16, unique=True)
	firts_name = models.CharField(verbose_name='Nama Depan', max_length=20)
	last_name = models.CharField(verbose_name='Nama Belakang', max_length=30, blank=True)
	birth_place = models.CharField(verbose_name='Tempat Lahir', max_length=20)
	birth_date = models.DateField(verbose_name='Tanggal Lahir')
	gender = models.CharField(verbose_name='Jenis Kelamin', max_length=1, choices=GENDER_CHOICES)
	religion = models.CharField(verbose_name='Agama', max_length=6, choices=RELIGION_CHOICES)
	education = models.CharField(verbose_name='Pendidikan', max_length=1, choices=EDUCATION_CHOICES, blank=True)
	maried = models.CharField(verbose_name='Status Pernikahan', max_length=2, choices=MARIED_CHOICES)
	marital = models.CharField(verbose_name='Hubungan Keluarga', max_length=1, choices=MARITAL_CHOICE)
	national = models.CharField(verbose_name='Kebangsaan', max_length=3, choices=NATIONAL_CHOICE)
	imigrasi = models.ForeignKey(DocImigrasi, verbose_name='Dokumen Imigrasi', blank=True)
	idimigrasi = models.CharField(verbose_name='ID Dokumen', max_length=15, unique=True)
	father_name = models.CharField(verbose_name='Nama Ayah', max_length=20)
	mother_name = models.CharField(verbose_name='Nama Ibu', max_length=20)

	class Meta:
		verbose_name = 'Warga'
		verbose_name_plural = 'Warga'

	def __unicode__(self):
		return self.firts_name


# Create your models here.
