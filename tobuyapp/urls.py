from django.urls import path, include
from .views import ToBuyList, InquiryView, DiaryListView, DiaryDetailView, DiaryCreateView, DiaryUpdateView, DiaryDeleteView

app_name="tobuyapp"
urlpatterns = [
    path('', ToBuyList.as_view(), name="index"),
    path('inquiry/', InquiryView.as_view(), name="inquiry"),
    path('diary_list/', DiaryListView.as_view(), name="diary_list"),
    path('diary_detail/<int:pk>/', DiaryDetailView.as_view(), name="diary_detail"),
    path('diary_create/', DiaryCreateView.as_view(), name="diary_create"),
    path('diary_update/<int:pk>', DiaryUpdateView.as_view(), name="diary_update"),
    path('diary_delete/<int:pk>', DiaryDeleteView.as_view(), name="diary_delete")
]
