from django.http.response import FileResponse
from django.shortcuts import render
from django.views.generic import base

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from wsgiref.util import FileWrapper
from django.http import HttpResponse

from .models import Recibo
from .serializers import ReciboSerializer


# Create your views here.

class ReciboRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new Recibo.
    """
    #permission_classes = [IsAdminUser]

    def get(self, request, control, periodo, format=None):
        recibo = Recibo.objects.filter(no_control=control, periodo=periodo)
        serializer = ReciboSerializer(recibo, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = ReciboSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, 
                            status= status.HTTP_201_CREATED)

        return Response(serializer.errors, 
                            status= status.HTTP_400_BAD_REQUEST)

class ReciboFileRecordView(APIView):
    from django.http import FileResponse
    import traceback

    def get(self, request, id_recibo):
        import base64

        recibo = Recibo.objects.get(id_recibo=id_recibo)
        """ 
        
        
        response['Content-Disposition'] = 'inline'
        """
        ruta = recibo.ruta_archivo
        document = open(ruta, 'rb')
        document_encoded = base64.b64encode(document.read())

        return Response(document_encoded)
        
      


""" class EmpleadoRecordView(APIView):
    
    #permission_classes = [IsAdminUser]

    def get(self, request, control):
        recibos = Empleado.objects.filter(no_control=control)

        serializer = EmpleadoSerializer(recibos, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmpleadoSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, 
                            status= status.HTTP_201_CREATED)

        return Response(serializer.errors, 
                            status= status.HTTP_400_BAD_REQUEST) """


""" class EmpleadoRecordNameView(APIView):

    def get(self, request, nombre, ape_p, ape_m):
        empleado = Empleado.objects.get(nombre=nombre,  apellido_p=ape_p, apellido_m=ape_m)
        control = empleado.no_control

        return Response(control) """


