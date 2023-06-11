from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render,redirect
from .models import (AboutUs, AdminBank, Contact, Event, Membership, Partners, Service,
  SubscriptionPlan, Team)
from django.utils import timezone
import random

class HomeView(View):
  def get(self,request):
    return render(request, 'index.html')
  
  
class AboutUsView(View):
  def get(self,request):
    aboutus = AboutUs.objects.first()
    teams = Team.objects.all()
    services = Service.objects.all()
    partners = Partners.objects.all()
    
    context = {
      'about':aboutus,
      'teams':teams,
      'services':services,
      'partners':partners,
    }
    return render(request,'aboutus.html',context)
  
class EventView(View):
  def get(self, request):
    upcoming_events = Event.objects.order_by('date')[:3]
    events = Event.objects.all()
    partners = Partners.objects.all()
    
    context = {
    'upcoming_events':upcoming_events,
    'events':events,
    'partners':partners,
    }
    return render(request, 'events.html', context)
  
  
class ServiceView(View):
  def get(self, request):
    services = Service.objects.all()
    partners = Partners.objects.all()
    
    context = {
      'services':services,
      'partners':partners,
    }
    return render (request, 'services.html', context)
  
  
class ContactView(View):
  def get(self, request):
    contact = Contact.objects.last()
    partners = Partners.objects.all()
    
    
    
    context = {
      'contact' : contact,
      'partners':partners,
      
    }
    return render(request, 'contact.html', context)
  
class MembershipView(View):
  def get(self,request):
    admin_bank = AdminBank.objects.last()
    sub_plans = SubscriptionPlan.objects.all()
    
    context = {
      'admin_bank':admin_bank,
      'sub_plans':sub_plans,
    }
    return render(request,'mem.html',context)
  
  
  def post(self, request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    profile = request.FILES.get('profile')
    passport_front = request.FILES.get('passport_front')
    passport_back = request.FILES.get('passport_back')
    membership_type = request.POST.get('membership_type')
    membership_duration = request.POST.get('membership_duration')
    membership_receipt  = request.FILES.get('membership_receipt')
    agree_terms_condition =request.POST.get('agree_terms_condition', False) == 'on'
    
    
    random_number = random.randint(1000, 9999)
    username = f"{first_name}{last_name}#{random_number}"
    user = User.objects.create_user(
      email=email, first_name=first_name, last_name=last_name,username=username
    )
    user.save()
    membership = Membership(
      user=user, address=address, phone=phone, profile=profile, passport_front = passport_front, passport_back= passport_back, membership_type=membership_type, membership_duration=membership_duration, membership_receipt = membership_receipt,agree_terms_condition=agree_terms_condition)
    
    membership.save()
    
    print("done -----")
    
    return redirect('home')