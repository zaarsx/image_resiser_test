# Generated by Django 3.1.5 on 2021-01-19 17:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SourceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded', models.DateTimeField(auto_created=True, verbose_name='uploaded')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='title')),
                ('image', models.ImageField(upload_to='upload/source_images', verbose_name='image')),
            ],
            options={
                'verbose_name': 'source image',
                'verbose_name_plural': 'source images',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ModifiedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='image width')),
                ('height', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='image height')),
                ('image', models.ImageField(upload_to='upload/modified_images', verbose_name='image')),
                ('source_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resizer.sourceimage', verbose_name='source image')),
            ],
            options={
                'verbose_name': 'modified image',
                'verbose_name_plural': 'modified images',
                'ordering': ['source_image__title', 'width', 'height'],
            },
        ),
    ]
