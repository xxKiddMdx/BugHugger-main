# Generated by Django 4.1.7 on 2023-03-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_apps', '0002_course_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description_text',
            field=models.CharField(max_length=500),
        ),
    ]
