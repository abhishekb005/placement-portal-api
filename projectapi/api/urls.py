from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('school/', views.SchoolList.as_view()),
    path('school/<int:pk>/', views.SchoolDetail.as_view()),    
    path('branch/', views.BranchList.as_view()),
    path('branch/<int:pk>/', views.BranchDetail.as_view()),
    path('degree/', views.DegreeList.as_view()),
    path('degree/<int:pk>/', views.DegreeDetail.as_view()),
    path('mentor/', views.MentorList.as_view()),
    path('mentor/<int:pk>/', views.MentorDetail.as_view()),
    path('company/', views.CompanyList.as_view()),
    path('company/<int:pk>/', views.CompanyDetail.as_view()),
    path('position/', views.PositionList.as_view()),
    path('position/<int:pk>/', views.PositionDetail.as_view()),
    path('placementcell/', views.PlacementCellList.as_view()),
    path('placementcell/<int:pk>/', views.PlacementCellDetail.as_view()),
    path('stu/', views.StudentList.as_view()),
    path('stu/<str:pk>/', views.StudentDetail.as_view()),
    path('plof/', views.PlacementOfficerList.as_view()),
    path('plof/<int:pk>/', views.PlacementOfficerDetail.as_view()),
    path('msgps/', views.MessageP2SList.as_view()),
    path('msgps/<int:pk>/', views.MessageP2SDetail.as_view()),
    path('msgpc/', views.MessageP2CList.as_view()),
    path('msgpc/<int:pk>/', views.MessageP2CDetail.as_view()),
    path('msgcp/', views.MessageC2PList.as_view()),
    path('msgcp/<int:pk>/', views.MessageC2PDetail.as_view()),
    path('offers/', views.OffersList.as_view()),
    path('offers/<int:pk>/', views.OffersDetail.as_view()),
    path('applied/', views.AppliedList.as_view()),
    path('applied/<int:pk>/', views.AppliedDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)