from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render,redirect
from .models import (AboutUs, AdminBank, Contact, Event, HomePageImage, MainService, Membership,
  Partners, Service, SubscriptionPlan, Team, Timing, UserContact)
from django.utils import timezone
import random

class HomeView(View):
  def get(self,request):
    aboutus = AboutUs.objects.first()
    teams = Team.objects.all()
    services = Service.objects.all()
    partners = Partners.objects.all()
    events = Event.objects.all()
    home_page_images  = HomePageImage.objects.all()
    # timing = Timing.objects.last()
    # contact = Contact.objects.last()
    
    context = {
      'about':aboutus,
      'teams':teams,
      'services':services,
      'partners':partners,
      'events':events,
      'home_page_images':home_page_images,
      # 'timing':timing,
      # 'contact':contact,
    }
    return render(request, 'index.html',context)
  
  
class AboutUsView(View):
  def get(self,request):
    aboutus = AboutUs.objects.first()
    teams = Team.objects.all()
    services = Service.objects.all()
    partners = Partners.objects.all()
    events = Event.objects.all()
    
    
    context = {
      'about':aboutus,
      'teams':teams,
      'services':services,
      'partners':partners,
      'events':events,
      
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

class EventDetailView(View):
  def get(self,request, pk):
    partners = Partners.objects.all()
    event = Event.objects.get(pk=pk)
    context = {
    'partners':partners,
    'event':event,
      
    }
    return render(request,'event_detail.html', context)
  
class ServiceView(View):
  def get(self, request):
    services = MainService.objects.all()
    partners = Partners.objects.all()
    services_seconday = Service.objects.all()[:3]
    
    
    context = {
      'services':services,
      'partners':partners,
      'services_secondary':services_seconday,
      
    }
    return render (request, 'services.html', context)
  
class ServiceDetailView(View):
  def get(self,request,pk):
    service = MainService.objects.get(id=pk)
    partners = Partners.objects.all()
    
    context = {
      'service':service,
      'partners':partners,
    }
    return render(request,'service_detail.html',context)

class ContactView(View):
  def get(self, request):
    contact = Contact.objects.last()
    partners = Partners.objects.all()
    
    context = {
      'contact' : contact,
      'partners':partners,
      
    }
    return render(request, 'contact.html', context)
  

  def post(self,request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    
    
    user_contact = UserContact(name=name,email=email,subject=subject,message=message)
    user_contact.save()
    return redirect('home')
  
  
  
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
  
# class UserContactView(View):
#   def get(self,request):
#     return red
  
#   def post(self,request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     subject = request.POST.get('subject')
#     message = request.POST.get('message')
    
    
#     user_contact = UserContact(name=name,email=email,subject=subject,message=message)
#     user_contact.save()
#     return redirect(request,'home')
  
  