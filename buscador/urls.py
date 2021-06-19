from django.urls import path
from .views import ReciboRecordView, ReciboFileRecordView

app_name = 'buscador'
urlpatterns = [
    path('recibo/<control>/<periodo>', ReciboRecordView.as_view(), name='recibo-periodo'),
    path('recibo-file/<id_recibo>', ReciboFileRecordView.as_view(), name='recibo-file'),
    path('recibo/', ReciboRecordView.as_view(), name='recibo')
]