from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Document
from ..forms import DocumentForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class DocumentListView(ListView):
    model = Document
    template_name = "arosenius-admin-django/document_list.html"
    paginate_by = 20
    context_object_name = "document_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DocumentListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DocumentListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DocumentListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DocumentListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DocumentListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DocumentListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DocumentListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DocumentListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentListView, self).get_template_names()


class DocumentDetailView(DetailView):
    model = Document
    template_name = "arosenius-admin-django/document_detail.html"
    context_object_name = "document"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DocumentDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentDetailView, self).get_template_names()


class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    # fields = ['title', 'archive_id', 'date', 'description', 'content', 'type', 'width_inner', 'height_inner', 'width_outer', 'height_outer', 'material', 'technique_material', 'acquisition', 'creator', 'published', 'signature', 'inscriptions', 'source_museum']
    template_name = "arosenius-admin-django/document_create.html"
    success_url = reverse_lazy("document_list")

    def __init__(self, **kwargs):
        return super(DocumentCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DocumentCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DocumentCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("document_detail", args=(self.object.pk,))


class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm
    # fields = ['title', 'archive_id', 'date', 'description', 'content', 'type', 'width_inner', 'height_inner', 'width_outer', 'height_outer', 'material', 'technique_material', 'acquisition', 'creator', 'published', 'signature', 'inscriptions', 'source_museum']
    template_name = "arosenius-admin-django/document_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "document"

    def __init__(self, **kwargs):
        return super(DocumentUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DocumentUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("document_detail", args=(self.object.pk,))


class DocumentDeleteView(DeleteView):
    model = Document
    template_name = "arosenius-admin-django/document_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "document"

    def __init__(self, **kwargs):
        return super(DocumentDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DocumentDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DocumentDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("document_list")
