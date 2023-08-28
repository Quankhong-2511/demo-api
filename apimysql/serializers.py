from rest_framework import serializers
from .models import NhanVien, PhongBan


class PhongBanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhongBan
        fields = ["ten_phong"]


class NhanVienSerializer(serializers.ModelSerializer):
    # ten_phong = PhongBanSerializer()
    class Meta:
        model = NhanVien
        fields = ["id", "ho_ten", "tuoi", "chuc_vu", "ten_phong"]


class DemSerializer(serializers.Serializer):
    chuc_vu = serializers.CharField()
    tong_so_luong = serializers.IntegerField()
    
    class Meta:
        model = NhanVien
        fields = ["id", "ho_ten", "tuoi", "chuc_vu", "ten_phong"]
    


    
    
