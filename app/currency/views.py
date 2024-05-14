from currency.forms import ContactUSForm, RateForm, SourceForm
from currency.models import ContactUS, Rate, Source

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView


class IndexView(TemplateView):
    template_name = "index.html"


class RateListView(ListView):
    model = Rate
    template_name = "rate_list.html"


class RateDetailView(DetailView):
    model = Rate
    template_name = "rate_details.html"


class RateCreateView(CreateView):
    model = Rate
    form_class = RateForm
    template_name = "rate_create.html"
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    template_name = "rate_update.html"
    success_url = reverse_lazy('currency:rate-list')


class RateDeleteView(DeleteView):
    model = Rate
    template_name = "rate_delete.html"
    success_url = reverse_lazy('currency:rate-list')


class SourceListView(ListView):
    model = Source
    template_name = "source_list.html"


class SourceDetailView(DetailView):
    model = Source
    template_name = "source_details.html"


class SourceCreateView(CreateView):
    model = Source
    form_class = SourceForm
    template_name = "source_create.html"
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    template_name = "source_update.html"
    success_url = reverse_lazy('currency:source-list')


class SourceDeleteView(DeleteView):
    model = Source
    template_name = "source_delete.html"
    success_url = reverse_lazy('currency:source-list')


class ContactUSCreateView(CreateView):
    model = ContactUS
    form_class = ContactUSForm
    template_name = "contact_us_create.html"
    success_url = reverse_lazy('index')
