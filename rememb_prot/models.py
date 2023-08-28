from django.db import models


class Enrich(models.Model):
    pmid = models.CharField(max_length = 255,null = True, blank = True)
    enrichment = models.CharField(max_length = 255,null = True, blank = True)
    count_total = models.IntegerField(null=True)
    method = models.CharField(max_length = 255, null = True)


    def __str__(self):
        return self.pmid



class Remembprot(models.Model):
    pmid = models.CharField( max_length = 255,null = True, blank = True )
    author = models.CharField(max_length = 255,null = True, blank = True )
    paper = models.CharField(max_length = 255,null = True, blank = True )
    organism = models.CharField(max_length = 255,null = True, blank = True )
    CellOrtissue = models.CharField(max_length = 255,null = True, blank = True )
    disease = models.CharField(max_length = 255,null = True, blank = True )
    profileOrDifex = models.CharField(max_length = 255,null = True, blank = True )
    contxtOfIdent = models.CharField(max_length = 255,null = True, blank = True )
    contxtOfDiferentialREG = models.CharField(max_length = 255,null = True, blank = True )
    test = models.CharField(max_length = 255,null = True, blank = True )
    control = models.CharField(max_length = 255,null = True, blank = True )
    foldchange = models.CharField(max_length = 255,null = True, blank = True )
    expression = models.CharField(max_length = 255,null = True, blank = True )
    protienExtractMethod = models.CharField(max_length = 255,null = True, blank = True )
    geneSymbol = models.CharField(max_length = 255,null = True, blank = True )
    geneID = models.CharField(max_length = 255,null = True, blank = True )
    isTrans = models.CharField(max_length = 255,null = True, blank = True )

    def __str__(self):
        return self.geneSymbol


class Cellmarker(models.Model):
    geneSymbol = models.CharField(max_length = 255,null = True, blank = True )
    species = models.CharField(max_length = 255,null = True, blank = True )
    tissueType = models.CharField(max_length = 255,null = True, blank = True )
    cancerType =  models.CharField(max_length = 255,null = True, blank = True )
    cellName = models.CharField(max_length = 255,null = True, blank = True )

    def __str__(self):
        return self.geneSymbol


class Dose(models.Model):
    dose_id = models.CharField(max_length = 255,null = True, blank = True )
    description = models.CharField(max_length = 255,null = True, blank = True)
    gene_id = models.CharField(max_length = 1000, null = True, blank = True)
    gene_symbol = models.CharField(max_length = 1000, null = True, blank = True)
    p_value = models.FloatField(max_length = 100, null = True)
    adj_pvalue = models.FloatField(max_length = 100, null = True)
    count = models.IntegerField(null = True)
    organism = models.CharField(max_length = 255, null = True)


    def __str__(self):
        return self.dose_id


