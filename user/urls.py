from django.urls import path, re_path
from .views import UserRecordView

app_name = 'user'
urlpatterns = [
    path('usuario/<control>/', UserRecordView.as_view(), name='user'),
]