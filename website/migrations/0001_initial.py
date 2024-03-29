# Generated by Django 4.0.5 on 2022-07-10 18:05

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('featured_image', models.ImageField(null=True, upload_to='')),
                ('content', tinymce.models.HTMLField(null=True)),
                ('excerpt', models.CharField(max_length=255, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phone_number', models.CharField(max_length=40)),
                ('client_message', models.TextField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='GettingInvolvedLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phone_number', models.CharField(max_length=40)),
                ('category', models.CharField(choices=[('Financially', 'Financially'), ('Ideas', 'Ideas'), ('Volunteerting', 'Volunteerting')], default='Financially', max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('college', models.CharField(max_length=255)),
                ('expectations', models.TextField(max_length=500)),
                ('cv', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='ImportantUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('update_link', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OfficialDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Legal Personality', 'Legal Personality'), ('Ministerial Collaboration', 'Ministerial Collaboration'), ('Signed MOUs', 'Signed MOUs')], default='Legal Personality', max_length=255)),
                ('document_file', models.FileField(upload_to='official_documents')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_status', models.CharField(choices=[('Regected', 'Rejected'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('nationality', models.CharField(max_length=255, null=True)),
                ('current_adress', models.CharField(max_length=255, null=True)),
                ('level_of_education', models.CharField(max_length=255, null=True)),
                ('specialization', models.CharField(max_length=255, null=True)),
                ('graduation_country', models.CharField(max_length=255, null=True)),
                ('experience', models.TextField(max_length=2550, null=True)),
                ('consept_note', models.TextField(max_length=2550, null=True)),
                ('owns_a_computer', models.TextField(max_length=2550, null=True)),
                ('cv', models.FileField(null=True, upload_to="Applicant's CVs")),
            ],
        ),
    ]
