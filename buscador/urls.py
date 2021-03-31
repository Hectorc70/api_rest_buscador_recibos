from django.urls import path, re_path
from .views import ReciboRecordView, EmpleadoRecordView

app_name = 'buscador'
urlpatterns = [
    path('recibo/<control>/<periodo>', ReciboRecordView.as_view(), name='recibo-periodo'),
    path('recibo/', ReciboRecordView.as_view(), name='recibo-periodo'),
]