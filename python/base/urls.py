"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static #videoi hamr
from django.urls import path, include
from django.contrib import admin
from api.models import BannerResourse,GalleryResourse,ServicesResourse,PackagesResourse
#avelcnum enq versia vorpisi senc dimenq http://127.0.0.1:8000/api/ inq@ haskana
from tastypie.api import Api

api = Api(api_name="v1")

b_resourse = BannerResourse()
g_resourse = GalleryResourse()
s_resourse = ServicesResourse()
p_resourse = PackagesResourse()

#hima menq sa registeracia enq anum vor v1 sksi
api.register(b_resourse)
api.register(g_resourse)
api.register(s_resourse)
api.register(p_resourse)

#api/v1/banner api senc en stexcum
urlpatterns = [
    path('', include("travelhome.urls")),
    path('admin/', admin.site.urls),
    path("api/", include(api.urls)),
    # path("api/", include(b_resourse.urls)),
    # path("api/", include(g_resourse.urls)), sa hanum enq
    # path("api/", include(s_resourse.urls)),
    # path("api/", include(p_resourse.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #video-i hamar
