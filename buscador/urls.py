from django.urls import path, re_path
from .views import ReciboRecordView, ReciboFileRecordView ,EmpleadoRecordView, EmpleadoRecordNameView

app_name = 'buscador'
urlpatterns = [
    path('recibo/<control>/<periodo>', ReciboRecordView.as_view(), name='recibo-periodo'),
    path('recibo-file/<id_recibo>', ReciboFileRecordView.as_view(), name='recibo-file'),
    path('recibo/', ReciboRecordView.as_view(), name='recibo'),

    path('empleado/<control>', EmpleadoRecordView.as_view(), name='empleado-control'),
    path('empleado/', EmpleadoRecordView.as_view(), name='empleado'),
    path('empleado-control/<nombre>/<ape_p>/<ape_m>', EmpleadoRecordNameView.as_view(), name='empleado-name'),
]