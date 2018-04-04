from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DocumentsImages
from ..forms import DocumentsImagesForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class DocumentsImagesListView(ListView):
    model = DocumentsImages
    template_name = "arosenius-admin-django/documents_images_list.html"
    paginate_by = 20
    context_object_name = "documents_images_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DocumentsImagesListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsImagesListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsImagesListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DocumentsImagesListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DocumentsImagesListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DocumentsImagesListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DocumentsImagesListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DocumentsImagesListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DocumentsImagesListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DocumentsImagesListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsImagesListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsImagesListView, self).get_template_names()


class DocumentsImagesDetailView(DetailView):
    model = DocumentsImages
    template_name = "arosenius-admin-django/documents_images_detail.html"
    context_object_name = "documents_images"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DocumentsImagesDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsImagesDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsImagesDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsImagesDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsImagesDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsImagesDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentsImagesDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsImagesDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsImagesDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsImagesDetailView, self).get_template_names()


class DocumentsImagesCreateView(CreateView):
    model = DocumentsImages
    form_class = DocumentsImagesForm
    # fields = ['document', 'images']
    template_name = "arosenius-admin-django/documents_images_create.html"
    success_url = reverse_lazy("documents_images_list")

    def __init__(self, **kwargs):
        return super(DocumentsImagesCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DocumentsImagesCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsImagesCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentsImagesCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DocumentsImagesCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentsImagesCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentsImagesCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentsImagesCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentsImagesCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentsImagesCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentsImagesCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsImagesCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsImagesCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_images_detail", args=(self.object.pk,))


class DocumentsImagesUpdateView(UpdateView):
    model = DocumentsImages
    form_class = DocumentsImagesForm
    # fields = ['document', 'images']
    template_name = "arosenius-admin-django/documents_images_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "documents_images"

    def __init__(self, **kwargs):
        return super(DocumentsImagesUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsImagesUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsImagesUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentsImagesUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsImagesUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsImagesUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsImagesUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DocumentsImagesUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentsImagesUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentsImagesUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentsImagesUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentsImagesUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentsImagesUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentsImagesUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsImagesUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsImagesUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsImagesUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_images_detail", args=(self.object.pk,))


class DocumentsImagesDeleteView(DeleteView):
    model = DocumentsImages
    template_name = "arosenius-admin-django/documents_images_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "documents_images"

    def __init__(self, **kwargs):
        return super(DocumentsImagesDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsImagesDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DocumentsImagesDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DocumentsImagesDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsImagesDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsImagesDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsImagesDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentsImagesDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsImagesDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsImagesDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsImagesDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_images_list")
