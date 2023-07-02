from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"inquilinos", views.InquilinoViewSet)
router.register(r"ambientes", views.AmbienteViewSet)
router.register(r"servicios", views.ServicioViewSet)
router.register(r"servicioambientes", views.ServicioAmbienteViewSet)
router.register(r"ambienteinquilinos", views.AmbienteInquilinoViewSet)

urlpatterns = [
    #path("", views.index, name="index")
    path("ambientes/", views.ambientes),
    path("", include(router.urls)),
    path("inquilino/crear/", views.InquilinoCreateView.as_view(), name="inquilinos_crear"),
    path("inquilino/cantidad/", views.inquilino_count, name="inquilino_count"),
    path("inquilino/filtrar/libres", views.ambientes_libres),
]