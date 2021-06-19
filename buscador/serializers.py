from rest_framework.validators import UniqueTogetherValidator


from rest_framework import serializers
from buscador.models import Recibo, Empleado

""" class ReciboSerializer(serializers.ModelSerializer):


    class Meta:
        model = Recibo
        fields = '__all__'
"""

""" class EmpleadoSerializer(serializers.ModelSerializer):

    recibos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Empleado
        fields = '__all__' """


class ReciboSerializer(serializers.ModelSerializer):


    class Meta:
        model = Recibo
        fields = '__all__'



