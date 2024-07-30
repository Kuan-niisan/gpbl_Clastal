# Generated by Django 5.0.3 on 2024-07-30 02:52

import django.db.models.deletion
import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('description', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('context', models.FileField(blank=True, upload_to='uploads/')),
                ('youtube_url', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('is_sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
                ('tags', models.ManyToManyField(blank=True, to='courses.tags')),
            ],
        ),
    ]
