# Generated by Django 4.0.5 on 2022-10-05 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_tag_note_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='category',
            new_name='tag',
        ),
    ]
