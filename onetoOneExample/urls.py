from django.urls import path, include
# from .views import country_list, country_detail #Function based usage
from .views import ProfileView, MemberView



urlpatterns = [
    path("profile/", ProfileView.as_view()),      
    path("member/", MemberView.as_view())     

]