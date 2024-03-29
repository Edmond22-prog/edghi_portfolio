# Generated by Django 4.1 on 2023-03-02 17:37

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='Python Developer', max_length=150)),
                ('brief', django_quill.fields.QuillField(default="This is the kind of language I'm used to speak. Together with some mobile and web dev languages too. 😁😊")),
                ('degree', models.CharField(default='Master in Computer Science', max_length=150)),
                ('phone', models.CharField(default='+23791678378', max_length=13)),
                ('email', models.EmailField(default='ghislain.makolle@facsciences-uy1.cm', max_length=254)),
                ('city', models.CharField(default='Yaounde, Cameroon', max_length=150)),
                ('freelance', models.CharField(choices=[('Available | Full time', 'Available | Full time'), ('Available | Part time', 'Available | Part time'), ('Not Available', 'Not Available')], default='Available | Part time', max_length=150)),
                ('about_text', django_quill.fields.QuillField(default="Dynamic youth studying Computer Science at the University of Yaounde 1 for the past four years already. I am very passionate about coding and programming and that's what I spend most of my time doing")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(default='Bootstrap Icon name', max_length=150)),
                ('number', models.PositiveIntegerField()),
                ('text', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='resumes/')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(default='Remix Icon name', max_length=150)),
                ('text', models.CharField(max_length=150)),
                ('color', colorfield.fields.ColorField(default='#18d26e', image_field=None, max_length=18, samples=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('client', models.CharField(max_length=150)),
                ('project_date', models.DateTimeField()),
                ('project_url', models.URLField()),
                ('description', django_quill.fields.QuillField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Web', 'Web'), ('App', 'App'), ('Other', 'Other')], default='Other', max_length=150, unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(max_length=300)),
                ('name', models.CharField(max_length=150)),
                ('role', models.CharField(max_length=150)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('show', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects/')),
                ('caption', models.CharField(max_length=150)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='website.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.projectcategory'),
        ),
    ]
