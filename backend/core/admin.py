from django.contrib import admin
from django.http import HttpResponse
import csv
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
  NewsLetter,
)
from core.views import download_csv
from .csv_generator import generate_membership_csv

class MembershipAdmin(admin.ModelAdmin):
  list_display =['user','phone','membership_duration']
  def download_csv(self, request, queryset):
        # Generate the CSV file
        csv_data = generate_membership_csv()

        # Create the HTTP response with CSV file
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="memberships.csv"'

        # Write the CSV file content to the response
        writer = csv.writer(response)
        writer.writerow(['User', 'Phone', 'Membership Duration'])  # Add header row
        for membership in queryset:
            writer.writerow([membership.user, membership.phone, membership.membership_duration])

        return response

  download_csv.short_description = 'Download CSV'  # Action description in the admin site


# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ['user', 'phone', 'membership_duration']

#     def download_csv(self, request, queryset):
#         # Generate the CSV file
#         csv_data = generate_membership_csv()

#         # Create the HTTP response with CSV file
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="memberships.csv"'

#         # Write the CSV file content to the response
#         writer = csv.writer(response)
        
#         # Write the header row
#         header = [
#             'User',
#             'Address',
#             'Phone',
#             'Profile',
#             'Passport Front',
#             'Passport Back',
#             'Membership Type',
#             'Membership Duration',
#             'Agree Terms Condition',
#             'Membership Receipt',
#         ]
#         writer.writerow(header)

#         # Write the data rows
#         for membership in queryset:
#             data_row = [
#                 membership.user.username,
#                 membership.address,
#                 membership.phone,
#                 membership.profile.url if membership.profile else '',
#                 membership.passport_front.url if membership.passport_front else '',
#                 membership.passport_back.url if membership.passport_back else '',
#                 membership.get_membership_type_display(),
#                 membership.get_membership_duration_display(),
#                 membership.agree_terms_condition,
#                 membership.membership_receipt.url if membership.membership_receipt else '',
#             ]
#             writer.writerow(data_row)

#         return response

#     download_csv.short_description = 'Download CSV'  # Action description in the admin site

# import base64
import base64
import urllib.request

import base64
from django.core.files import File

# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ['user', 'phone', 'membership_duration']

#     def download_csv(self, request, queryset):
#         # Generate the CSV file
#         csv_data = generate_membership_csv()

#         # Create the HTTP response with CSV file
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="memberships.csv"'

#         # Write the CSV file content to the response
#         writer = csv.writer(response)

#         # Write the header row
#         header = [
#             'User',
#             'Address',
#             'Phone',
#             'Profile',
#             'Passport Front',
#             'Passport Back',
#             'Membership Type',
#             'Membership Duration',
#             'Agree Terms Condition',
#             'Membership Receipt',
#         ]
#         writer.writerow(header)

#         # Write the data rows
#         for membership in queryset:
#             profile_image_data = self.get_image_data(membership.profile)
#             passport_front_image_data = self.get_image_data(membership.passport_front)
#             passport_back_image_data = self.get_image_data(membership.passport_back)
#             receipt_image_data = self.get_image_data(membership.membership_receipt)

#             data_row = [
#                 membership.user.username,
#                 membership.address,
#                 membership.phone,
#                 profile_image_data,
#                 passport_front_image_data,
#                 passport_back_image_data,
#                 membership.get_membership_type_display(),
#                 membership.get_membership_duration_display(),
#                 membership.agree_terms_condition,
#                 receipt_image_data,
#             ]
#             writer.writerow(data_row)

#         return response

#     download_csv.short_description = 'Download CSV'  # Action description in the admin site

#     def get_image_data(self, image_field):
#         if image_field:
#             image_data = image_field.read()
#             encoded_data = base64.b64encode(image_data).decode('utf-8')
#             return encoded_data
#         return ''

# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ['user', 'phone', 'membership_duration']

#     def download_csv(self, request, queryset):
#         # Generate the CSV file
#         csv_data = generate_membership_csv()

#         # Create the HTTP response with CSV file
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="memberships.csv"'

#         # Write the CSV file content to the response
#         writer = csv.writer(response)

#         # Write the header row
#         header = [
#             'User',
#             'Address',
#             'Phone',
#             'Profile',
#             'Passport Front',
#             'Passport Back',
#             'Membership Type',
#             'Membership Duration',
#             'Agree Terms Condition',
#             'Membership Receipt',
#         ]
#         writer.writerow(header)

#         # Write the data rows
#         for membership in queryset:
#             profile_image_data = self.get_image_data(membership.profile)
#             passport_front_image_data = self.get_image_data(membership.passport_front)
#             passport_back_image_data = self.get_image_data(membership.passport_back)
#             receipt_image_data = self.get_image_data(membership.membership_receipt)

#             data_row = [
#                 membership.user.username,
#                 membership.address,
#                 membership.phone,
#                 profile_image_data,
#                 passport_front_image_data,
#                 passport_back_image_data,
#                 membership.get_membership_type_display(),
#                 membership.get_membership_duration_display(),
#                 membership.agree_terms_condition,
#                 receipt_image_data,
#             ]
#             writer.writerow(data_row)

#         return response

#     download_csv.short_description = 'Download CSV'  # Action description in the admin site

#     def get_image_data(self, image_field):
#         if image_field:
#             image_url = image_field.url
#             image_data = urllib.request.urlopen(image_url).read()
#             encoded_data = base64.b64encode(image_data).decode('utf-8')
#             return encoded_data
#         return ''


# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ['user', 'phone', 'membership_duration']

#     def download_csv(self, request, queryset):
#         # Generate the CSV file
#         csv_data = generate_membership_csv()

#         # Create the HTTP response with CSV file
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="memberships.csv"'

#         # Write the CSV file content to the response
#         writer = csv.writer(response)
        
#         # Write the header row
#         header = [
#             'User',
#             'Address',
#             'Phone',
#             'Profile',
#             'Passport Front',
#             'Passport Back',
#             'Membership Type',
#             'Membership Duration',
#             'Agree Terms Condition',
#             'Membership Receipt',
#         ]
#         writer.writerow(header)

#         # Write the data rows
#         for membership in queryset:
#             profile_data = self.get_image_data(membership.profile)
#             passport_front_data = self.get_image_data(membership.passport_front)
#             passport_back_data = self.get_image_data(membership.passport_back)
#             receipt_data = self.get_image_data(membership.membership_receipt)

#             data_row = [
#                 membership.user.username,
#                 membership.address,
#                 membership.phone,
#                 profile_data,
#                 passport_front_data,
#                 passport_back_data,
#                 membership.get_membership_type_display(),
#                 membership.get_membership_duration_display(),
#                 membership.agree_terms_condition,
#                 receipt_data,
#             ]
#             writer.writerow(data_row)

#         return response

#     download_csv.short_description = 'Download CSV'  # Action description in the admin site

#     def get_image_data(self, image_field):
#         if image_field:
#             with open(image_field.path, 'rb') as image_file:
#                 encoded_data = base64.b64encode(image_file.read())
#                 return encoded_data.decode('utf-8')
#         return ''

# import base64

# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ['user', 'phone', 'membership_duration']

#     def download_csv(self, request, queryset):
#         # Generate the CSV file
#         csv_data = generate_membership_csv()

#         # Create the HTTP response with CSV file
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="memberships.csv"'

#         # Write the CSV file content to the response
#         writer = csv.writer(response)

#         # Write the header row
#         header = [
#             'User',
#             'Address',
#             'Phone',
#             'Profile',
#             'Passport Front',
#             'Passport Back',
#             'Membership Type',
#             'Membership Duration',
#             'Agree Terms Condition',
#             'Membership Receipt',
#         ]
#         writer.writerow(header)

#         # Write the data rows
#         for membership in queryset:
#             profile_url = membership.profile.url if membership.profile else ''
#             passport_front_url = membership.passport_front.url if membership.passport_front else ''
#             passport_back_url = membership.passport_back.url if membership.passport_back else ''
#             receipt_url = membership.membership_receipt.url if membership.membership_receipt else ''

#             data_row = [
#                 membership.user.username,
#                 membership.address,
#                 membership.phone,
#                 profile_url,
#                 passport_front_url,
#                 passport_back_url,
#                 membership.get_membership_type_display(),
#                 membership.get_membership_duration_display(),
#                 membership.agree_terms_condition,
#                 receipt_url,
#             ]
#             writer.writerow(data_row)

#         return response

#     download_csv.short_description = 'Download CSV'  # Action description in the admin site

# Register the MembershipAdmin with the Membership model
# admin.site.register(Membership, MembershipAdmin)

# Register the MembershipAdmin with the Membership model


# Register the MembershipAdmin with the Membership model
# admin.site.register(Membership, MembershipAdmin)
import csv
from django.contrib import admin
from django.http import HttpResponse
from core.models import Membership

class MembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'membership_duration']

    def download_csv(self, request, queryset):
        # Generate the CSV file
        csv_data = generate_membership_csv()

        # Create the HTTP response with CSV file
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="memberships.csv"'

        # Write the CSV file content to the response
        writer = csv.writer(response)

        # Write the header row
        header = [
            'User',
            'First Name',
            'Last Name',
            'Email',
            'Address',
            'Phone',
            'Membership Type',
            'Membership Duration',
            'Agree Terms Condition',
        ]
        writer.writerow(header)

        # Write the data rows
        for membership in queryset:
            data_row = [
                membership.user.username,
                membership.user.first_name,
                membership.user.last_name,
                membership.user.email,
                membership.address,
                membership.phone,
                membership.get_membership_type_display(),
                membership.get_membership_duration_display(),
                membership.agree_terms_condition,
            ]
            writer.writerow(data_row)

        return response

    download_csv.short_description = 'Download CSV'  # Action description in the admin site




admin.site.add_action(MembershipAdmin.download_csv, 'membership_download_csv')

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
admin.site.register(NewsLetter)









