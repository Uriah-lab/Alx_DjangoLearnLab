# Generated by Django 5.1.6 on 2025-03-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('published_date', models.DateField()),
            ],
            options={
                'permissions': [('can_view', 'Can view books'), ('can_create', 'Can add books'), ('can_edit', 'Can edit books'), ('can_delete', 'Can delete books')],
            },
        ),
    ]
