# Generated by Django 4.0.1 on 2022-04-16 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookGenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BookRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_description', models.TextField(blank=True, null=True)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(max_length=100)),
                ('book_status', models.CharField(choices=[('AV', 'Available'), ('NA', 'Not-Available'), ('RE', 'Reserved'), ('SP', 'Special'), ('OT', 'Other')], default='AV', max_length=50)),
                ('location_number', models.CharField(blank=True, max_length=50, null=True)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='app.bookgenres')),
            ],
        ),
    ]