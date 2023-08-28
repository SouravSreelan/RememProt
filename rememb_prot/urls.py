from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'rememb_prot'

urlpatterns = [
path('',views.home, name = 'home'),
path('browse/',views.browse, name='browse'),
path('browseResult/',views.browseResult, name = 'browseResult'),
path('analysisPage/', TemplateView.as_view(template_name="rememb_prot/analysis.html"), name = 'analysisPage'),
path('dose/', TemplateView.as_view(template_name="rememb_prot/dosee.html"), name = 'dose'),

path('enrichment/', views.enrichment, name = 'enrichment'),
path('transmembrane/', views.transmembrane, name = 'transmembrane'),
path('faqs/', TemplateView.as_view(template_name="rememb_prot/faqs.html"), name = 'faqs'),
path('bquery/', TemplateView.as_view(template_name="rememb_prot/bquery.html"), name = 'bquery'),
path('bqueryResult/', views.bqueryResult, name = 'bqueryResult'),

path('dose_ontology/', views.dose_ontology, name = 'dose_ontology'),

path('selectedSpecies/', views.selectedSpecies, name = 'selectedSpecies'),
path('selectedMethod/', views.selectedMethod, name = 'selectedMethod'),
path('get_csrf_token/', views.get_csrf_token, name = 'get_csrf_token'),

path('contributers/', TemplateView.as_view(template_name="rememb_prot/contributer.html"), name = 'contributers'),

path('contactus/', TemplateView.as_view(template_name="rememb_prot/contactus.html"), name = 'contactus'),

]
