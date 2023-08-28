from django.db.models import Count
from rest_framework import viewsets, generics, permissions
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import NhanVien, PhongBan
from .serializers import NhanVienSerializer, PhongBanSerializer, DemSerializer



class NhanVienViewSet(viewsets.ModelViewSet):
    queryset = NhanVien.objects.all()
    serializer_class = NhanVienSerializer
  
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()] 

        return [permissions.IsAuthenticated()]
   
    
    @action(methods=['get'], detail=False, url_path="tuoi-hon-25")
    def tuoi_hon_25(self, request):
        tuoihon25 = NhanVien.objects.filter(tuoi__gt=25)
        serializer = NhanVienSerializer(tuoihon25, many=True)
        return Response(serializer.data)
    
    
    @action(methods=['get'], detail=False, url_path="sap-xep-tuoi")
    def sap_xep_tuoi(self, request):
        sapxeptuoi = NhanVien.objects.order_by('tuoi')
        serializer = NhanVienSerializer(sapxeptuoi, many=True)
        return Response(serializer.data)
    
    
    @action(methods=['get'], detail=False, url_path="tong-nhan-vien")
    def tong_so_nhan_vien(self, request):
        tongnhanvien = NhanVien.objects.count()
        context = {'tong_nhan_vien': tongnhanvien}
        return Response(context)   
    
    
    @action( methods=['get'], detail=False, url_path="tong-theo-chuc-vu")
    def tong_theo_chuc_vu(self, request):
        tong_theo_chuc_vu = NhanVien.objects.values('chuc_vu').annotate(tong_so_luong=Count('id'))
        serializer = DemSerializer(tong_theo_chuc_vu, many=True)
        return Response(serializer.data)
    
    
    @action( methods=['get'], detail=False, url_path="danh-sach-theo-phong-ban")
    def danh_sach_theo_phong_ban(self, request):
        phong_bans = PhongBan.objects.all()
        data = []
    
        for phong_ban in phong_bans:
            nhan_viens = NhanVien.objects.filter(ten_phong=phong_ban)
            serializer = NhanVienSerializer(nhan_viens, many=True)
            data.append({'phong_ban': phong_ban.ten_phong, 
                            'nhan_viens': serializer.data})
            
        nhan_vien_null = NhanVien.objects.filter(ten_phong=None)
        serializer_null = NhanVienSerializer(nhan_vien_null, many = True)
        data.append({'phong_ban': 'Chua xac dinh',
                     'nhan_viens': serializer_null.data})
        
        return Response(data)
    
    
    @action(methods=['get'], detail=False, url_path="tim")
    def nhan_vien_ky_tu_an(self, request): 
        keyword = "an"
        nhan_viens = NhanVien.objects.filter(chuc_vu__icontains=keyword)
        serializer = NhanVienSerializer(nhan_viens, many=True)
        return Response(serializer.data)

    
    @action( methods=['get'], detail=False, url_path="tong-theo-chuc-vu-hon-1")
    def tong_theo_chuc_vu_hon_1(self, request):
        tong_theo_chuc_vu = NhanVien.objects.values('chuc_vu').annotate(tong_so_luong=Count('id'))
        tong_theo_chuc_vu_hon_1 = tong_theo_chuc_vu.filter(tong_so_luong__gt=1)
        serializer = DemSerializer(tong_theo_chuc_vu_hon_1, many=True)
        
        return Response(serializer.data)
    
    


class PhongBanViewSet(viewsets.ModelViewSet):
    queryset = PhongBan.objects.all()
    serializer_class = PhongBanSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()] 

        return [permissions.IsAuthenticated()]
    





    