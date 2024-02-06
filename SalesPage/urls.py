from django.urls import path
from . import views


urlpatterns = [
    path("page/<page_no>/", views.sales_page, name="sales-page"  )
]