# Generated by Django 3.0.8 on 2020-07-31 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogPost', '0002_auto_20200801_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Tags',
            field=models.ManyToManyField(related_name='Tags', to='BlogPost.Tag'),
        ),
    ]
