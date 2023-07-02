from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Inquilino
from .models import Ambiente
from .models import Servicio
from .models import ServicioAmbiente
from .models import AmbienteInquilino
from .serializers import InquilinoSerializer
from .serializers import AmbienteSerializer
from .serializers import ServicioSerializer
from .serializers import ServicioAmbienteSerializer
from .serializers import AmbienteInquilinoSerializer

def index(request):
    return HttpResponse("Hola, mundo")

def ambientes(request):
    ambientes = Ambiente.objects.all()
    ambientelibre = Ambiente.objects.filter(libre=True)
    return render(request, "ambientes.html", {
        "ambientes1": ambientes,
        "ambientelibre1": ambientelibre 
    })

# def ambienteslibre(request):
#     ambientes = Ambiente(libre = True)
#     return render(request, "ambientes.html", {
#         "ambientes2": ambientes
#     })

class InquilinoViewSet(viewsets.ModelViewSet):
    queryset = Inquilino.objects.all()
    serializer_class = InquilinoSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioAmbienteViewSet(viewsets.ModelViewSet):
    queryset = ServicioAmbiente.objects.all()
    serializer_class = ServicioAmbienteSerializer

class AmbienteInquilinoViewSet(viewsets.ModelViewSet):
    queryset = AmbienteInquilino.objects.all()
    serializer_class = AmbienteInquilinoSerializer

class InquilinoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Inquilino.objects.all()
    serializer_class = InquilinoSerializer

@api_view(["GET"])
def inquilino_count(request):
    try:
        cantidad = Inquilino.objects.count()
        return JsonResponse(
                {
                    "cantidad": cantidad
                },
                safe=False,
                status=200
            )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def ambientes_libres(request):
    try:
        ambiente = Ambiente.objects.filter(libre=True)
        return JsonResponse(
            AmbienteSerializer(ambiente, many=True).data,
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

