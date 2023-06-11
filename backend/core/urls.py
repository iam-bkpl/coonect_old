from django.urls import path
from .import views


urlpatterns = [
  path('',views.HomeView.as_view(), name='home'),
  path('aboutus/', views.AboutUsView.as_view(),name='aboutus'),
  path('event/', views.EventView.as_view(),name='event'),
  path('service/', views.ServiceView.as_view(),name='service'),
  path('contact/', views.ContactView.as_view(),name='contact'),
  path('membership/', views.MembershipView.as_view(),name='membership'),
  
  
  
  
  
]