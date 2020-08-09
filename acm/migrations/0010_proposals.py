# Generated by Django 2.0 on 2020-08-09 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acm', '0009_auto_20200724_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration_in_months', models.IntegerField(blank=True)),
                ('mentors', models.TextField(blank=True)),
                ('members', models.TextField(blank=True)),
                ('introduction', models.TextField(blank=True)),
                ('method', models.TextField(blank=True)),
                ('existing_work', models.TextField(blank=True)),
                ('application', models.TextField(blank=True)),
                ('sig_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acm.SIG')),
            ],
        ),
    ]
