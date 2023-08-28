from django.db import models


class PhongBan(models.Model):
    id = models.IntegerField(primary_key=True)
    ten_phong = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.ten_phong


class NhanVien(models.Model):
    id = models.IntegerField(primary_key=True)
    ho_ten = models.CharField(max_length=255, null=True)
    tuoi = models.IntegerField(null=True)
    ten_phong = models.ForeignKey(PhongBan, on_delete=models.CASCADE, related_name='nhanvien_set', null=True)
    chuc_vu = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.ho_ten if self.ho_ten else str(self.id)
  

