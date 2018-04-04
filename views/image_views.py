from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Image
from ..forms import ImageForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class ImageListView(ListView):
    model = Image
    template_name = "arosenius-admin-django/image_list.html"
    paginate_by = 20
    context_object_name = "image_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ImageListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ImageListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ImageListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ImageListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ImageListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ImageListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ImageListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ImageListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ImageListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ImageListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ImageListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ImageListView, self).get_template_names()


class ImageDetailView(DetailView):
    model = Image
    template_name = "arosenius-admin-django/image_detail.html"
    context_object_name = "image"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ImageDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ImageDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ImageDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ImageDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ImageDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ImageDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ImageDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ImageDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ImageDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ImageDetailView, self).get_template_names()


class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm
    # fields = ['file', 'google_vision_colors', 'google_vision_labels', 'width', 'height', 'page_number', 'page_side', 'page_order']
    template_name = "arosenius-admin-django/image_create.html"
    success_url = reverse_lazy("image_list")

    def __init__(self, **kwargs):
        return super(ImageCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ImageCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ImageCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ImageCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ImageCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ImageCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ImageCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ImageCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ImageCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ImageCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ImageCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ImageCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ImageCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("image_detail", args=(self.object.pk,))


class ImageUpdateView(UpdateView):
    model = Image
    form_class = ImageForm
    # fields = ['file', 'google_vision_colors', 'google_vision_labels', 'width', 'height', 'page_number', 'page_side', 'page_order']
    template_name = "arosenius-admin-django/image_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "image"

    def __init__(self, **kwargs):
        return super(ImageUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ImageUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ImageUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ImageUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ImageUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ImageUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ImageUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ImageUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ImageUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ImageUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ImageUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ImageUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ImageUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ImageUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ImageUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ImageUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ImageUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("image_detail", args=(self.object.pk,))


class ImageDeleteView(DeleteView):
    model = Image
    template_name = "arosenius-admin-django/image_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "image"

    def __init__(self, **kwargs):
        return super(ImageDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ImageDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ImageDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ImageDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ImageDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ImageDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ImageDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ImageDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ImageDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ImageDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ImageDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("image_list")
