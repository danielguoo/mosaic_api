# Generated by Django 2.1 on 2018-08-04 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('released', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(blank=True, default='', max_length=20)),
                ('cover_art', models.CharField(max_length=50)),
                ('spotify_URL', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('released',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('synopsis', models.CharField(max_length=150)),
                ('review_text', models.TextField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created', 'album'),
            },
        ),
    ]
