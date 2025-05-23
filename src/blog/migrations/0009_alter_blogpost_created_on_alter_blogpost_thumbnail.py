# Generated by Django 5.1 on 2024-08-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_commentanswer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_on',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date de publication'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(upload_to='blog'),
        ),
    ]
