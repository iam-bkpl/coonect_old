import csv
from django.conf import settings
from . models import Membership


def generate_membership_csv():
    memberships = Membership.objects.all()

    with open('memberships.csv', 'w', newline='') as csvfile:
        fieldnames = ['User First Name', 'Address', 'Phone', 'Profile Image', 'Passport Front', 'Passport Back', 'Membership Type', 'Membership Duration']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for membership in memberships:
            profile_image_url = membership.profile.url if membership.profile else ''
            passport_front_url = membership.passport_front.url if membership.passport_front else ''
            passport_back_url = membership.passport_back.url if membership.passport_back else ''

            writer.writerow({
                'User First Name': membership.user.first_name,
                'Address': membership.address,
                'Phone': membership.phone,
                'Profile Image': profile_image_url,
                'Passport Front': passport_front_url,
                'Passport Back': passport_back_url,
                'Membership Type': membership.get_membership_type_display(),
                'Membership Duration': membership.get_membership_duration_display()
            })

    print('CSV file generated successfully.')

# Call the function to generate the CSV file
generate_membership_csv()
