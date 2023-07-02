from rest_framework import serializers
from .models import Inquilino
from .models import Ambiente
from .models import Servicio
from .models import ServicioAmbiente
from .models import AmbienteInquilino

class InquilinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquilino
        fields = "__all__"

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = "__all__"

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = "__all__"

class ServicioAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioAmbiente
        fields = "__all__"

class AmbienteInquilinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmbienteInquilino
        fields = "__all__"