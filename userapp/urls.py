
from . import views
from django.urls import path

from .views import home

urlpatterns = [
    path('ho/',views.home, name='home'),
    path('add_com/',views.company, name='add_company'),
    path('add_job/',views.job, name='add_job'),
    path('ac/',views.candidate, name='add_candidate'),
    path('vcom/',views.view_company, name='view_company'),
    path('vjob/',views.view_job, name='view_job'),
    path('vcan/',views.view_candidate, name='view_candidate'),
    path('update/<int:pk>/',views.updatecomp.as_view(), name='updt'),
    path('upload-csv/', views.profile_upload, name="profile_upload")

]
