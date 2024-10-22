from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page' ),
    path('jobs/detail/<int:pk>/', views.rent_detail_page, name='rent_detail_page'),
    path('jobs/', views.rents_page, name='rents_page'),
    path('category/jobs/<slug:slug>/', views.rents_by_category_page, name='rents_by_category_page'),
    path('sign-up/', views.sign_up_page, name = 'sign_up_page'),
    path('login/', views.login_page, name = 'login_page'),
    path('logout/', views.logout_action, name = 'logout_action'),
    
]
