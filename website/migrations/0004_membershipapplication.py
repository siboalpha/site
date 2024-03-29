# Generated by Django 4.0.5 on 2022-07-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_blog_options_alter_importantupdate_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipApplication',
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
                ('application_letter', models.FileField(null=True, upload_to='Application Lettrs')),
                ('cv', models.FileField(null=True, upload_to='Applicants CVs')),
            ],
        ),
    ]
