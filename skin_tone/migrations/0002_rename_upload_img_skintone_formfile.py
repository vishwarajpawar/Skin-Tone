# Generated by Django 3.2.2 on 2021-05-14 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skin_tone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skintone',
            old_name='upload_img',
            new_name='formfile',
        ),
    ]
