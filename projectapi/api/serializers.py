from django.db.models import fields
from django.db.models.fields import files
from rest_framework import serializers
from .models import *

#query

class DegreeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Degree
        fields='__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Position
        fields='__all__'
               
class BranchSerializer(serializers.ModelSerializer):
    Position=PositionSerializer(many=True,read_only=True)

    class Meta:
        model=Branch
        fields=['id','Branch_Name','Degree','Start_year','Position']
        depth=3
    

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mentor
        fields='__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'
 

class PlacementCellSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlacementCell
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    Position=PositionSerializer(many=True,read_only=True,)
    class Meta:
        model=Student
        fields=['first_name','Position','Branch']
        
        
        
        
class SchoolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = School
        fields = ['id','Name','Board']

class PlacementOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlacementOfficer
        fields='__all__'

class MessageP2SSerializer(serializers.ModelSerializer):
    class Meta:
        model=MessageP2S
        fields='__all__'

class MessageP2CSerializer(serializers.ModelSerializer):
    class Meta:
        models=MessageP2C
        fields='__all__'

class MessageC2PSerializer(serializers.ModelSerializer):
    class Meta:
        model=MessageC2P
        fields='__all__'

class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Offers
        fields='__all__'

class AppliedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Applied
        fields='__all__'

