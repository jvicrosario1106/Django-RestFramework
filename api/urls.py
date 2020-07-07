from django.urls import path
from . import views

urlpatterns = [

    path('', views.apiOverview, name= 'api-overview'),
    path('api-detail/<str:pk>/', views.apiDetail, name= 'api-detail'),
    path('api-list/', views.apiList, name= 'api-list'),
    path('api-create/', views.apiCreate, name= 'api-create'),
    path('api-update/<str:pk>/', views.apiUpdate, name= 'api-update'),
    path('api-delete/<str:pk>/', views.apiDelete, name= 'api-delete'),
]