# Generated by Django 4.2.7 on 2024-05-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]