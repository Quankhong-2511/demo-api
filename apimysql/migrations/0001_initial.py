# Generated by Django 4.2.3 on 2023-08-25 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NhanVien',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ho_ten', models.CharField(max_length=255)),
                ('tuoi', models.IntegerField()),
                ('chuc_vu', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PhongBan',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ten_phong', models.CharField(max_length=255)),
            ],
        ),
    ]
