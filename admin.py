from django.contrib import admin
from .models import Document, DocumentsPersons, DocumentsPlaces, Place, DocumentsTags, Museum, Tag, Type, Genre, Image, Person, DocumentsGenres
from django_baker.admin import ExtendedModelAdminMixin


class DocumentsImagesInline(admin.TabularInline):
	model = Image

	readonly_fields = ['image_tag']
	fields = [
		'image_tag',
		'file',
		'page_number',
		'page_order',
		'page_side'
	]


class DocumentsTagsInline(admin.TabularInline):
	model = DocumentsTags
	model._meta.verbose_name_plural = "Taggar"


class DocumentsGenresInline(admin.TabularInline):
	model = DocumentsGenres
	model._meta.verbose_name_plural = "Genre"


class DocumentsPersonsInline(admin.TabularInline):
	model = DocumentsPersons
	model._meta.verbose_name_plural = "Personer"


class DocumentAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	list_display = ['id', 'title', 'type', 'source_museum', 'list_image_tag']
	list_display_links = ['id', 'title', 'list_image_tag']
	extra_list_display = []
	extra_list_filter = ['source_museum', 'type']
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = [DocumentsTagsInline, DocumentsGenresInline, DocumentsImagesInline, DocumentsPersonsInline]
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []
	fields = [
		'title', 
		(
			'archive_id', 
			'source_museum', 
		),
		(
			'date', 
			'published', 
		),
		'description', 
		'content', 
		'type', 
		(
			'width_inner', 
			'height_inner', 
		),
		(
			'width_outer', 
			'height_outer', 
		),
		(
			'material', 
			'technique_material', 
		),
		'acquisition', 
		'creator', 
		(
			'signature', 
			'inscriptions', 
		),
	]

class DocumentsPersonsAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class DocumentsPlacesAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class PlaceAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class DocumentsTagsAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class MuseumAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class TagAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class TypeAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class GenreAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class ImageAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = [
		'image_tag'
	]
	fields = [
		'file',
		'page_number',
		'page_order',
		'page_side',
		'image_tag'
	] 


class PersonAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


class DocumentsGenresAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
	extra_list_display = []
	extra_list_filter = []
	extra_search_fields = []
	list_editable = []
	raw_id_fields = []
	inlines = []
	filter_vertical = []
	filter_horizontal = []
	radio_fields = {}
	prepopulated_fields = {}
	formfield_overrides = {}
	readonly_fields = []


admin.site.register(Document, DocumentAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Museum, MuseumAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Person, PersonAdmin)
#admin.site.register(DocumentsPersons, DocumentsPersonsAdmin)
#admin.site.register(DocumentsPlaces, DocumentsPlacesAdmin)
#admin.site.register(DocumentsTags, DocumentsTagsAdmin)
#admin.site.register(DocumentsGenres, DocumentsGenresAdmin)
