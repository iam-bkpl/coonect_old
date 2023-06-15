from django.contrib import admin
from core.models import (
  AdminBank,
  Timing,
  HomePageImage,
  AboutUs,
  Team,
  Service,
  Partners,
  Event,
  MainService,
  Contact,
  Membership,
  SubscriptionPlan,
  UserContact,
)

class MembershipAdmin(admin.ModelAdmin):
  list_display =['user','phone','membership_duration']

admin.site.register(AdminBank)
admin.site.register(Timing)
admin.site.register(HomePageImage)
admin.site.register(AboutUs)
admin.site.register(Team)
admin.site.register(Service)
admin.site.register(Partners)
admin.site.register(Event)
admin.site.register(MainService)
admin.site.register(Contact)
admin.site.register(Membership,MembershipAdmin)
admin.site.register(SubscriptionPlan)
admin.site.register(UserContact)








