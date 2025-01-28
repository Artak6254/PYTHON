from django.contrib import admin
from .models import Travel_banner, Travel_gallery,Travel_Brand, Travel_services,Travel_packages_gallery, Travel_Review
# Register your models here.

admin.site.register(Travel_banner)
admin.site.register(Travel_gallery)
admin.site.register(Travel_services)
admin.site.register(Travel_packages_gallery)
admin.site.register(Travel_Review)
admin.site.register(Travel_Brand)