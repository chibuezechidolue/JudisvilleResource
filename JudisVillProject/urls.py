from django.contrib import admin
from django.urls import path,include
from SalesPage import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("sales/", include("SalesPage.urls")),
    path("", views.home_page, name="home-page" ),
    path("contact-us/", views.contact_page, name="contact-page" ),
    path("about-us/", views.about_page, name="about-page" ),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
