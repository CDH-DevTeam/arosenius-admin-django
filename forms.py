from django import forms
from .models import Document, DocumentsPersons, DocumentsPlaces, DocumentsImages, Place, DocumentsTags, Museum, Tag, Genre, Image, Images, Person, DocumentsGenres


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['title', 'archive_id', 'date', 'description', 'content', 'type', 'width_inner', 'height_inner', 'width_outer', 'height_outer', 'material', 'technique_material', 'acquisition', 'creator', 'published', 'signature', 'inscriptions', 'source_museum']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DocumentForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DocumentForm, self).is_valid()

    def full_clean(self):
        return super(DocumentForm, self).full_clean()

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_archive_id(self):
        archive_id = self.cleaned_data.get("archive_id", None)
        return archive_id

    def clean_date(self):
        date = self.cleaned_data.get("date", None)
        return date

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_content(self):
        content = self.cleaned_data.get("content", None)
        return content

    def clean_type(self):
        type = self.cleaned_data.get("type", None)
        return type

    def clean_width_inner(self):
        width_inner = self.cleaned_data.get("width_inner", None)
        return width_inner

    def clean_height_inner(self):
        height_inner = self.cleaned_data.get("height_inner", None)
        return height_inner

    def clean_width_outer(self):
        width_outer = self.cleaned_data.get("width_outer", None)
        return width_outer

    def clean_height_outer(self):
        height_outer = self.cleaned_data.get("height_outer", None)
        return height_outer

    def clean_material(self):
        material = self.cleaned_data.get("material", None)
        return material

    def clean_technique_material(self):
        technique_material = self.cleaned_data.get("technique_material", None)
        return technique_material

    def clean_acquisition(self):
        acquisition = self.cleaned_data.get("acquisition", None)
        return acquisition

    def clean_creator(self):
        creator = self.cleaned_data.get("creator", None)
        return creator

    def clean_published(self):
        published = self.cleaned_data.get("published", None)
        return published

    def clean_signature(self):
        signature = self.cleaned_data.get("signature", None)
        return signature

    def clean_inscriptions(self):
        inscriptions = self.cleaned_data.get("inscriptions", None)
        return inscriptions

    def clean_source_museum(self):
        source_museum = self.cleaned_data.get("source_museum", None)
        return source_museum

    def clean(self):
        return super(DocumentForm, self).clean()

    def validate_unique(self):
        return super(DocumentForm, self).validate_unique()

    def save(self, commit=True):
        return super(DocumentForm, self).save(commit)


class DocumentsPersonsForm(forms.ModelForm):

    class Meta:
        model = DocumentsPersons
        fields = ['document', 'person']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DocumentsPersonsForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DocumentsPersonsForm, self).is_valid()

    def full_clean(self):
        return super(DocumentsPersonsForm, self).full_clean()

    def clean_document(self):
        document = self.cleaned_data.get("document", None)
        return document

    def clean_person(self):
        person = self.cleaned_data.get("person", None)
        return person

    def clean(self):
        return super(DocumentsPersonsForm, self).clean()

    def validate_unique(self):
        return super(DocumentsPersonsForm, self).validate_unique()

    def save(self, commit=True):
        return super(DocumentsPersonsForm, self).save(commit)


class DocumentsPlacesForm(forms.ModelForm):

    class Meta:
        model = DocumentsPlaces
        fields = ['document', 'place']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DocumentsPlacesForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DocumentsPlacesForm, self).is_valid()

    def full_clean(self):
        return super(DocumentsPlacesForm, self).full_clean()

    def clean_document(self):
        document = self.cleaned_data.get("document", None)
        return document

    def clean_place(self):
        place = self.cleaned_data.get("place", None)
        return place

    def clean(self):
        return super(DocumentsPlacesForm, self).clean()

    def validate_unique(self):
        return super(DocumentsPlacesForm, self).validate_unique()

    def save(self, commit=True):
        return super(DocumentsPlacesForm, self).save(commit)


class DocumentsImagesForm(forms.ModelForm):

    class Meta:
        model = DocumentsImages
        fields = ['document', 'images']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DocumentsImagesForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DocumentsImagesForm, self).is_valid()

    def full_clean(self):
        return super(DocumentsImagesForm, self).full_clean()

    def clean_document(self):
        document = self.cleaned_data.get("document", None)
        return document

    def clean_images(self):
        images = self.cleaned_data.get("images", None)
        return images

    def clean(self):
        return super(DocumentsImagesForm, self).clean()

    def validate_unique(self):
        return super(DocumentsImagesForm, self).validate_unique()

    def save(self, commit=True):
        return super(DocumentsImagesForm, self).save(commit)


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ['name', 'district', 'country', 'lat', 'lon']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PlaceForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PlaceForm, self).is_valid()

    def full_clean(self):
        return super(PlaceForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_district(self):
        district = self.cleaned_data.get("district", None)
        return district

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean_lat(self):
        lat = self.cleaned_data.get("lat", None)
        return lat

    def clean_lon(self):
        lon = self.cleaned_data.get("lon", None)
        return lon

    def clean(self):
        return super(PlaceForm, self).clean()

    def validate_unique(self):
        return super(PlaceForm, self).validate_unique()

    def save(self, commit=True):
        return super(PlaceForm, self).save(commit)


class DocumentsTagsForm(forms.ModelForm):

    class Meta:
        model = DocumentsTags
        fields = ['document', 'tag']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DocumentsTagsForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DocumentsTagsForm, self).is_valid()

    def full_clean(self):
        return super(DocumentsTagsForm, self).full_clean()

    def clean_document(self):
        document = self.cleaned_data.get("document", None)
        return document

    def clean_tag(self):
        tag = self.cleaned_data.get("tag", None)
        return tag

    def clean(self):
        return super(DocumentsTagsForm, self).clean()

    def validate_unique(self):
        return super(DocumentsTagsForm, self).validate_unique()

    def save(self, commit=True):
        return super(DocumentsTagsForm, self).save(commit)


class MuseumForm(forms.ModelForm):

    class Meta:
        model = Museum
        fields = ['name']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(MuseumForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(MuseumForm, self).is_valid()

    def full_clean(self):
        return super(MuseumForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean(self):
        return super(MuseumForm, self).clean()

    def validate_unique(self):
        return super(MuseumForm, self).validate_unique()

    def save(self, commit=True):
        return super(MuseumForm, self).save(commit)


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['name']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(TagForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(TagForm, self).is_valid()

    def full_clean(self):
        return super(TagForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean(self):
        return super(TagForm, self).clean()

    def validate_unique(self):
        return super(TagForm, self).validate_unique()

    def save(self, commit=True):
        return super(TagForm, self).save(commit)


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ['name']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(GenreForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(GenreForm, self).is_valid()

    def full_clean(self):
        return super(GenreForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean(self):
        return super(GenreForm, self).clean()

    def validate_unique(self):
        return super(GenreForm, self).validate_unique()

    def save(self, commit=True):
        return super(GenreForm, self).save(commit)


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['file', 'google_vision_colors', 'google_vision_labels', 'width', 'height', 'page_number', 'page_side', 'page_order']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ImageForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ImageForm, self).is_valid()

    def full_clean(self):
        return super(ImageForm, self).full_clean()

    def clean_file(self):
        file = self.cleaned_data.get("file", None)
        return file

    def clean_google_vision_colors(self):
        google_vision_colors = self.cleaned_data.get("google_vision_colors", None)
        return google_vision_colors

    def clean_google_vision_labels(self):
        google_vision_labels = self.cleaned_data.get("google_vision_labels", None)
        return google_vision_labels

    def clean_width(self):
        width = self.cleaned_data.get("width", None)
        return width

    def clean_height(self):
        height = self.cleaned_data.get("height", None)
        return height

    def clean_page_number(self):
        page_number = self.cleaned_data.get("page_number", None)
        return page_number

    def clean_page_side(self):
        page_side = self.cleaned_data.get("page_side", None)
        return page_side

    def clean_page_order(self):
        page_order = self.cleaned_data.get("page_order", None)
        return page_order

    def clean(self):
        return super(ImageForm, self).clean()

    def validate_unique(self):
        return super(ImageForm, self).validate_unique()

    def save(self, commit=True):
        return super(ImageForm, self).save(commit)


class ImagesForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = ['file', 'page_number', 'page_side', 'page_ider']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ImagesForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ImagesForm, self).is_valid()

    def full_clean(self):
        return super(ImagesForm, self).full_clean()

    def clean_file(self):
        file = self.cleaned_data.get("file", None)
        return file

    def clean_page_number(self):
        page_number = self.cleaned_data.get("page_number", None)
        return page_number

    def clean_page_side(self):
        page_side = self.cleaned_data.get("page_side", None)
        return page_side

    def clean_page_ider(self):
        page_ider = self.cleaned_data.get("page_ider", None)
        return page_ider

    def clean(self):
        return super(ImagesForm, self).clean()

    def validate_unique(self):
        return super(ImagesForm, self).validate_unique()

    def save(self, commit=True):
        return super(ImagesForm, self).save(commit)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PersonForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PersonForm, self).is_valid()

    def full_clean(self):
        return super(PersonForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean(self):
        return super(PersonForm, self).clean()

    def validate_unique(self):
        return super(PersonForm, self).validate_unique()

    def save(self, commit=True):
        return super(PersonForm, self).save(commit)


class DocumentsGenresForm(forms.ModelForm):

    class Meta:
        model = DocumentsGenres
        fields = ['document', 'genre']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DocumentsGenresForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DocumentsGenresForm, self).is_valid()

    def full_clean(self):
        return super(DocumentsGenresForm, self).full_clean()

    def clean_document(self):
        document = self.cleaned_data.get("document", None)
        return document

    def clean_genre(self):
        genre = self.cleaned_data.get("genre", None)
        return genre

    def clean(self):
        return super(DocumentsGenresForm, self).clean()

    def validate_unique(self):
        return super(DocumentsGenresForm, self).validate_unique()

    def save(self, commit=True):
        return super(DocumentsGenresForm, self).save(commit)

