from rest_framework.viewsets import ModelViewSet
from clientes.api.serializers import ClienteSerializer
from clientes.models import Cliente

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    lookup_field = 'email'
    lookup_value_regex = '[^/]+'

