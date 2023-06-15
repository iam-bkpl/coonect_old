from django.urls import path
from .import views


urlpatterns = [
  path('',views.HomeView.as_view(), name='home'),
  path('aboutus/', views.AboutUsView.as_view(),name='aboutus'),
  path('event/', views.EventView.as_view(),name='event'),
  path('event/<int:pk>/', views.EventDetailView.as_view(),name='event'),
  path('service/', views.ServiceView.as_view(),name='service'),
  path('service/<int:pk>/', views.ServiceDetailView.as_view(),name='service'),

  path('contact/', views.ContactView.as_view(),name='contact'),
  # path('usercontact/', views.UserContactView.as_view(),name='user-contact'),
  
  path('membership/', views.MembershipView.as_view(),name='membership'),
  
  
  
  
  
]