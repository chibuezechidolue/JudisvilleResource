from django.urls import path
from . import views


urlpatterns = [
    path("page/<product_name>/", views.sales_page, name="sales-page"  ),
    path("page/<product_name>/tk-you", views.thank_you_page, name="thank-you-page" ),
    path("", views.home_page, name="home-page"  ),
    
]