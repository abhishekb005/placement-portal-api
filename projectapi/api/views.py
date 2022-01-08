from django.shortcuts import render
from rest_framework import generics
from api.models import *
from api.serializers import *
# Create your views here.

class SchoolList(generics.ListCreateAPIView):
    queryset=School.objects.all()
    serializer_class=SchoolSerializer

class BranchList(generics.ListCreateAPIView):
    queryset=Branch.objects.all()
    serializer_class=BranchSerializer


class DegreeList(generics.ListCreateAPIView):
    queryset=Degree.objects.all()
    serializer_class=DegreeSerializer

class MentorList(generics.ListCreateAPIView):
    queryset=Mentor.objects.all()
    serializer_class=MentorSerializer

class CompanyList(generics.ListCreateAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

class PositionList(generics.ListCreateAPIView):
    queryset=Position.objects.all()
    serializer_class=PositionSerializer

class PlacementCellList(generics.ListCreateAPIView):
    queryset=PlacementCell.objects.all()
    serializer_class=PlacementCellSerializer
    
class StudentList(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
class PlacementOfficerList(generics.ListCreateAPIView):
    queryset=PlacementOfficer.objects.all()
    serializer_class=PlacementOfficerSerializer

class MessageP2SList(generics.ListCreateAPIView):
    queryset=MessageP2S.objects.all()
    serializer_class=MessageP2SSerializer

class MessageP2CList(generics.ListCreateAPIView):
    queryset=MessageP2C.objects.all()
    serializer_class=MessageP2CSerializer
class MessageC2PList(generics.ListCreateAPIView):
    queryset=MessageC2P.objects.all()
    serializer_class=MessageC2PSerializer
class OffersList(generics.ListCreateAPIView):
    queryset=Offers.objects.all()
    serializer_class=OffersSerializer
class AppliedList(generics.ListCreateAPIView):
    queryset=Applied.objects.all()
    serializer_class=AppliedSerializer

class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=School.objects.all()
    serializer_class=SchoolSerializer

class DegreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Degree.objects.all()
    serializer_class=DegreeSerializer

class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Branch.objects.all()
    serializer_class=BranchSerializer
class MentorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Mentor.objects.all()
    serializer_class=MentorSerializer
class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Position.objects.all()
    serializer_class=PositionSerializer
class PlacementCellDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=PlacementCell.objects.all()
    serializer_class=PlacementCellSerializer
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class PlacementOfficerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=PlacementOfficer.objects.all()
    serializer_class=PlacementOfficerSerializer
class MessageP2SDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=MessageP2S.objects.all()
    serializer_class=MessageP2SSerializer
class MessageP2CDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=MessageP2C.objects.all()
    serializer_class=MessageP2CSerializer
class MessageC2PDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=MessageC2P.objects.all()
    serializer_class=MessageC2PSerializer
class OffersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Offers.objects.all()
    serializer_class=OffersSerializer
class AppliedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Applied.objects.all()
    serializer_class=AppliedSerializer
