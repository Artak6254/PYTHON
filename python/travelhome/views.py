from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Travel_banner,Contact, Travel_gallery,Travel_Brand, Travel_services, Travel_packages_gallery, Travel_Review,Booking
from .forms import BookingForm, ContactForm
# Create your views here.

def index(request):
    banner_data = Travel_banner.objects.all()
    pack = Travel_gallery.objects.all()
    services_data = Travel_services.objects.all()
    gallery_data = Travel_packages_gallery.objects.all()
    review_data = Travel_Review.objects.all()
    brand_data = Travel_Brand.objects.all()
    context = {
        "data_banners": banner_data,
        "pack": pack,
        "services_data": services_data,
        "gallery_data": gallery_data,
        "review_data": review_data,
        "brand_data": brand_data  
    }
    return render(request, "travelhome/index.html", context)

 
def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
           booking = form.save() 
           return redirect('success', booking_id=booking.id)
        else:
            print("Form is not valid", request.POST)
    

def success(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'travelhome/success.html',{'booking':booking})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_success', contact_id=contact.id)
        else:
            print("Form is not valid.", form.errors)  # Print errors for debugging
            return render(request, 'travelhome/contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'travelhome/contact.html', {'form': form})


def contact_success(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'travelhome/contact.html', {'contact': contact})