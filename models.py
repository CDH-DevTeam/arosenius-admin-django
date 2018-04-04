# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey hasdesired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals
from django.utils.safestring import mark_safe
from django.db import models


class Image(models.Model):
	file = models.CharField(max_length=255, blank=True, null=True)
	google_vision_colors = models.TextField(blank=True, null=True)
	google_vision_labels = models.TextField(blank=True, null=True)
	width = models.FloatField(blank=True, null=True)
	height = models.FloatField(blank=True, null=True)
	page_number = models.IntegerField(blank=True, null=True)
	page_side = models.CharField(max_length=255, blank=True, null=True)
	page_order = models.IntegerField(blank=True, null=True)
	document = models.ForeignKey('Document', db_column='document')

	def __str__(self):
		return self.file if self is not None else ''

	def image_tag(self):
		if (self.file is not None):
			return mark_safe('<a href="http://cdh-vir-1.it.gu.se:8004/images/255x/%s.jpg" target="_blank"><img src="http://cdh-vir-1.it.gu.se:8004/images/255x/%s.jpg" style="max-width: 300px" /></a>' % (self.file, self.file))
		else:
			return mark_safe('Image')

	image_tag.short_description = 'Bild'
	image_tag.allow_tags = True

	class Meta:
		managed = False
		db_table = 'images'


class Document(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	archive_id = models.CharField(max_length=255, blank=True, null=True)
	date = models.CharField(max_length=10, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	type = models.ForeignKey('Type', models.DO_NOTHING, db_column='type')
	width_inner = models.FloatField(blank=True, null=True)
	height_inner = models.FloatField(blank=True, null=True)
	width_outer = models.FloatField(blank=True, null=True)
	height_outer = models.FloatField(blank=True, null=True)
	material = models.TextField(blank=True, null=True)
	technique_material = models.CharField(max_length=255, blank=True, null=True)
	acquisition = models.CharField(max_length=255, blank=True, null=True)
	creator = models.CharField(max_length=255, blank=True, null=True)
	published = models.BooleanField(null=False, default=1)
	signature = models.TextField(blank=True, null=True)
	inscriptions = models.TextField(blank=True, null=True)
	source_museum = models.ForeignKey('Museum', models.DO_NOTHING, db_column='source_museum')

	def image_tag(self):
		images = Image.objects.filter(document=self.id)

		if (len(images) > 0):
			image = images[0]
			return mark_safe('<a href="http://cdh-vir-1.it.gu.se:8004/images/255x/%s.jpg" target="_blank"><img src="http://cdh-vir-1.it.gu.se:8004/images/255x/%s.jpg" style="max-height: 150px" /></a>' % (image, image))
		else:
			return mark_safe('Image')

	def list_image_tag(self):
		images = Image.objects.filter(document=self.id)

		if (len(images) > 0):
			image = images[0]
			return mark_safe('<img src="http://cdh-vir-1.it.gu.se:8004/images/255x/%s.jpg" style="max-height: 150px" />' % (image))
		else:
			return mark_safe('Image')

	class Meta:
		managed = False
		db_table = 'documents'


class Genre(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		managed = False
		db_table = 'genre'


class Museum(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		managed = False
		db_table = 'museums'


class Type(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		managed = False
		db_table = 'types'


class Person(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		managed = False
		db_table = 'persons'


class Place(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	district = models.CharField(max_length=255, blank=True, null=True)
	country = models.CharField(max_length=255, blank=True, null=True)
	lat = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
	lon = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		managed = False
		db_table = 'places'


class Tag(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		managed = False
		db_table = 'tags'


class DocumentsGenres(models.Model):
	document = models.ForeignKey(Document, db_column='document')
	genre = models.ForeignKey(Genre, db_column='genre')

	class Meta:
		managed = False
		db_table = 'documents_genres'


class DocumentsPersons(models.Model):
	document = models.ForeignKey(Document, db_column='document')
	person = models.ForeignKey(Person, db_column='person')

	class Meta:
		managed = False
		db_table = 'documents_persons'


class DocumentsPlaces(models.Model):
	document = models.ForeignKey(Document, db_column='document')
	place = models.ForeignKey(Place, db_column='place')

	class Meta:
		managed = False
		db_table = 'documents_places'


class DocumentsTags(models.Model):
	document = models.ForeignKey(Document, db_column='document')
	tag = models.ForeignKey(Tag, db_column='tag')

	class Meta:
		managed = False
		db_table = 'documents_tags'
