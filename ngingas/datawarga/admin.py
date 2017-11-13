from django.contrib import admin
from datawarga.models import Pekerjaan, DocImigrasi, Rt, Rw
from datawarga.models import Desa, Kecamatan, Kabupaten, Provinsi
from datawarga.models import KaKel, Warga

@admin.register(Pekerjaan)
class PekerjaanAdmin(admin.ModelAdmin):
	pass

@admin.register(DocImigrasi)
class DocImigrasiAdmin(admin.ModelAdmin):
	pass

@admin.register(Rt)
class RtAdmin(admin.ModelAdmin):
	pass

@admin.register(Rw)
class RwAdmin(admin.ModelAdmin):
	pass

@admin.register(Desa)
class DesaAdmin(admin.ModelAdmin):
	pass

@admin.register(Kecamatan)
class KecamatanAdmin(admin.ModelAdmin):
	pass

@admin.register(Kabupaten)
class KabupatenAdmin(admin.ModelAdmin):
	pass

@admin.register(Provinsi)
class ProvinsiAdmin(admin.ModelAdmin):
	pass

@admin.register(KaKel)
class KaKelAdmin(admin.ModelAdmin):
	list_display = ('id_kk', 'head_kk', 'rt', 'rw', 'desa')
	list_filter = ('id_kk', 'head_kk', 'desa', 'rt')

@admin.register(Warga)
class WargaAdmin(admin.ModelAdmin):
	list_display = ('nik', 'firts_name')
	list_filter = ('nik', 'firts_name', 'gender', 'maried')
# Register your models here.
