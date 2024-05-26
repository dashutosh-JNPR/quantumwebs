# Generated by Django 5.0.3 on 2024-05-23 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_featured_alt_text_category_featured_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, help_text='Title for display in blog page', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='featured_image',
            field=models.ImageField(blank=True, help_text='Upload an image to feature for this category.', null=True, upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(upload_to='blog/post_images/'),
        ),
    ]
