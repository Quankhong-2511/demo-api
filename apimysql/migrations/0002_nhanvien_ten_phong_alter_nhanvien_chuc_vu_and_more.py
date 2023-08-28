# Generated by Django 4.2.3 on 2023-08-25 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apimysql', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhanvien',
            name='ten_phong',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nhanvien_set', to='apimysql.phongban'),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='chuc_vu',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='ho_ten',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='nhanvien',
            name='tuoi',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='phongban',
            name='ten_phong',
            field=models.CharField(max_length=255, null=True),
        ),
    ]