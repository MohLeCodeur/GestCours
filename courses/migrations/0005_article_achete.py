# Generated by Django 5.1.5 on 2025-01-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_article_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='achete',
            field=models.BooleanField(default=False),
        ),
    ]
