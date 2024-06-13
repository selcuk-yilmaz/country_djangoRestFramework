from django.urls import path, include
# from .views import country_list, country_detail #Function based usage
from .views import CountryView, CountryDetailView



urlpatterns = [
    # path("list/", country_list),              #Function based usage
    # path("detail/<int:pk>", country_detail),  #Function based usage
    path("list/", CountryView.as_view()),       #Class based usage
    path("detail/<int:pk>", CountryDetailView.as_view()),   #Class based usage


]