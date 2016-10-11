from django.views.generic import ListView, DetailView

from projects.models import FundingSource


class FundingSourceView(ListView):
    template_name = "web/funding_source_index.html"
    context_object_name = "funding_sources"
    ordering = 'name'
    model = FundingSource
    
    
class FundingSourceDetailView(ListView):
    