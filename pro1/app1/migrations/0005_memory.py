# Generated by Django 4.2.3 on 2024-01-01 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_purches_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('F', 'FRIENDS'), ('S', 'MYSELF')], max_length=1)),
                ('image', models.ImageField(blank=True, upload_to='memory')),
                ('discribe', models.TimeField()),
                ('upload_date', models.DateTimeField()),
                ('upload_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.user')),
            ],
        ),
    ]
