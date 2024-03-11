# Generated by Django 4.2.10 on 2024-03-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_form', '0002_remove_mymodel_agreed_remove_mymodel_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='agreed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='char_field',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='ip_address',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='price',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='auto_field',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]