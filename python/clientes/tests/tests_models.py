from django.test import TestCase
from ..models import  Cliente

class ClienteTestCase(TestCase):

    def setUp(self):
        Cliente.objects.create(
            nome_completo="Diego Britto",
            email="diego@example.com"
        )

    def test_retorno_str(self):
        c1 = Cliente.objects.get(email="diego@example.com")
        self.assertEqual(c1.__str__(),'diego@example.com')