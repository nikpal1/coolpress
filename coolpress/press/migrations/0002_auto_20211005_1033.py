# Generated by Django 3.2.7 on 2021-10-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default='-', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published post')], default='DRAFT', max_length=32),
        ),
    ]
