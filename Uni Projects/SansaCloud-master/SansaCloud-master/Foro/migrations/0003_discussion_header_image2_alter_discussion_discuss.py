# Generated by Django 4.1 on 2022-11-22 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foro', '0002_alter_forum_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='header_image2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/respuestas/', verbose_name='Añadir Imagen (Opcional)'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='discuss',
            field=models.TextField(max_length=1000, verbose_name='Discusión'),
        ),
    ]
