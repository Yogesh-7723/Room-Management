# Generated by Django 4.2.3 on 2024-01-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('post', models.CharField(choices=[('M', 'member only'), ('PM', 'PaymentManage'), ('BM', 'BillManage'), ('RM', 'RentManage'), ('FM', 'FoodManage'), ('WM', 'WorkManage')], max_length=2)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('pro_img', models.ImageField(blank=True, upload_to='profile')),
            ],
        ),
    ]