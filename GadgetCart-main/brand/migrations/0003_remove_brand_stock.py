# Generated by Django 3.1 on 2021-11-16 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("brand", "0002_brand_stock")]

    operations = [migrations.RemoveField(model_name="brand", name="stock")]