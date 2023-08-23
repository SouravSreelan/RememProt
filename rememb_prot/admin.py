from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import pandas as pd
import csv

from .models import Remembprot , Enrich, Dose , Cellmarker

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class RemembprotaAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):
        if (request.method == 'POST' ):
            csv_file = request.FILES['csv_upload']
            # if not csv_file.name.endswith('.csv'):
            #     messages.warning(request,'the wrong type of file was uploaded ')
            #     return HttpResponseRedirect(request.path_info)

            df = pd.read_excel(csv_file, engine = 'openpyxl')
            df.fillna('', inplace=True)

            df_records = df.to_dict('records')

            for data in df_records:
                created = Remembprot.objects.update_or_create (

                pmid = data['PMID'],
                author = data['Author'],
                paper = data['Title of the paper'],
                organism = data['Organism'],
                CellOrtissue = data['Cell/tissue'],
                disease = data['Disease'],
                profileOrDifex = data['Profile and/or differential expression'],
                contxtOfIdent = data['Context of identification'],
                contxtOfDiferentialREG = data['Context of differential regulation'],
                test = data['Test'],
                control = data['Control'],
                foldchange = data['Fold change'],
                expression = data['Expression'],
                protienExtractMethod = data['Method of protein extraction'],
                geneSymbol = data['Gene symbol'],
                geneID = data['Entrez Gene ID'],
                ontology = data['Ontology'],
                membraneType = data['Membrane type'],
                peripheral = data['Peripheral'],
                # refSeq  = data['RefSeq Protein Accession'],
                predictedTmh = data['Number of predicted TMHs'],
                isTrans = data['is it Transmembrane']
                      )

        form = CsvImportForm()
        data = {'form': form }
        return render(request,'admin/csv_upload.html',data)




class EnrichAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):
        if (request.method == 'POST' ):
            csv_file = request.FILES['csv_upload']
            # if not csv_file.name.endswith('.csv'):
            #     messages.warning(request,'the wrong type of file was uploaded ')
            #     return HttpResponseRedirect(request.path_info)

            df = pd.read_excel(csv_file, engine = 'openpyxl')
            df.fillna('', inplace=True)

            df_records = df.to_dict('records')

            for data in df_records:
                created = Enrich.objects.update_or_create (

                pmid = data['pmid'],
                enrichment = data['enrich'],
                count_total = data['count'],
                               )
        form = CsvImportForm()
        data = {'form': form }
        return render(request,'admin/csv_upload.html',data)


class CellmarkerAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if (request.method == 'POST' ):
            csv_file = request.FILES['csv_upload']

            df = pd.read_excel(csv_file, engine = 'openpyxl')
            df.fillna('', inplace=True)

            df_records = df.to_dict('records')

            for data in df_records:
                created = Cellmarker.objects.update_or_create (
                geneSymbol = data['Gene Symbol'],
                species = data['Species Type'],
                tissueType = data['Tissue Type'],
                cancerType = data['Cancer Type'],
                cellName = data['Cell Name'],
                               )
        form = CsvImportForm()
        data = {'form': form }
        return render(request,'admin/csv_upload.html',data)


class DoseAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if (request.method == 'POST' ):
            csv_file = request.FILES['csv_upload']

            df = pd.read_excel(csv_file, engine = 'openpyxl')
            df.fillna('', inplace=True)

            df_records = df.to_dict('records')

            for data in df_records:
                created = Dose.objects.update_or_create (
                dose_id = data['ID'],
                description = data['Description'],
                gene_id = data['Entrez Gene ID'],
                p_value = data['pvalue'],
                adj_pvalue = data['p.adjust'],
                count = data['Count'],
                organism = data['organism'],
                gene_symbol = data['Membrane protein Gene symbol'],
                               )

        form = CsvImportForm()
        data = {'form': form }
        return render(request,'admin/csv_upload.html',data)


admin.site.register(Dose,DoseAdmin)
admin.site.register(Remembprot,RemembprotaAdmin)
admin.site.register(Enrich,EnrichAdmin)
# admin.site.register(Cellmarker,CellmarkerAdmin)

