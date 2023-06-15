from core.models import Contact, Service, Timing

# In your Django project directory
# Create a new file called "context_processors.py"

def navbar_footer_context(request):
    # Retrieve the necessary objects
    contact_data = Contact.objects.last()
    service_data = Service.objects.all()[:4]
    timing_data = Timing.objects.last()


    # Return a dictionary with the objects
    return {
        'contact_data': contact_data,
        'footer_data': service_data,
        'timing_data':timing_data,
        'service_data':service_data,
        
    }
