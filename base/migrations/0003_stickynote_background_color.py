# Generated by Django 4.1.7 on 2023-02-20 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_note_stickynote_note_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='stickynote',
            name='background_color',
            field=models.CharField(default='#FFFFFF', max_length=255),
        ),
    ]