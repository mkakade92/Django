from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='grievance'

urlpatterns = [
    path('',views.GrievanceList.as_view(),name='all'),
    path('new',views.CreateGrievance.as_view(),name='create'),
    path('by/<str:username>/',views.GrievanceList.as_view(),name='for_user'),
    path('by/<str:username>/<int:pk>/',views.GrievanceDetail.as_view(),name='single'),
    path('delete/<int:pk>/',views.DeleteGrievance.as_view(),name='delete'),
]
