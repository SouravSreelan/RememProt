# Generated by Django 4.1.4 on 2023-02-23 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rememb_prot', '0002_remove_remembprot_membranetype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remembprot',
            name='contxtOfDiferentialREG',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='remembprot',
            name='contxtOfIdent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='remembprot',
            name='profileOrDifex',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
