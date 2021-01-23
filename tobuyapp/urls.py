from django.urls import path, include
from .views import ToBuyList, InquiryView

app_name="tobuyapp"
urlpatterns = [
    path('', ToBuyList.as_view(), name="index"),
    path('inquiry/', InquiryView.as_view(), name="inquiry"),
    
]
