from tastypie.resources import ModelResource
from travelhome.models import Travel_banner,Travel_gallery,Travel_services,Travel_packages_gallery
#sa auth-i hamara
from tastypie.authorization import Authorization
from .auth import CustomAuthentication

#Authentication erb vor login enq linum
#authorization-erb vor mer mutq@ hastatvumva


class BannerResourse(ModelResource):
    class Meta:
        queryset = Travel_banner.objects.all()
        resource_name = "banner"
        allowed_methods = ["get"]

       
class GalleryResourse(ModelResource):
    class Meta:
       queryset = Travel_gallery.objects.all()    
       resource_name="gallery"   
       allowed_methods = ["get", "post","delete"]  
       authentication = CustomAuthentication()
       authorization = Authorization()
       
       
       
class ServicesResourse(ModelResource):
    class Meta:
       queryset = Travel_services.objects.all()    
       resource_name="services"   
       allowed_methods = ["get", "post","delete"] 
       authentication = CustomAuthentication()
       authorization = Authorization()
       

class PackagesResourse(ModelResource):
    class Meta:
       queryset = Travel_packages_gallery.objects.all()    
       resource_name="packages"   
       allowed_methods = ["get", "post","delete"]      
       authentication = CustomAuthentication()
       authorization = Authorization()               
                           
