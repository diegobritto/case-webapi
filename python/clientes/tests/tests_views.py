from django.test import TestCase
from django.urls import reverse
from ..models import  Cliente

class ClienteViewTestCase(TestCase):

    def setUp(self):
        Cliente.objects.create(
            nome_completo="Diego Britto",
            email="diego@example.com"
        )
        Cliente.objects.create(
            nome_completo="Diego Britto",
            email="diegobritto@example.com"
        )

    def test_get_cliente_status_code_200(self):
        response = self.client.get('http://127.0.0.1:8000/cliente/')
        self.assertEqual(response.status_code,200)

    def test_get_cliente_por_email_status_code_200(self):
        response = self.client.get('http://127.0.0.1:8000/cliente/diego@example.com/')
        self.assertEqual(response.status_code, 200)

    def test_get_cliente_por_email_status_code_404(self):
        response = self.client.get('http://127.0.0.1:8000/cliente/esteemail@naoexiste.com/')
        self.assertEqual(response.status_code, 404)

    def test_post_cliente_status_code_201(self):
        cliente = {'nome_completo': 'john', 'email': 'emailvalido@example.com'}
        response = self.client.post('http://127.0.0.1:8000/cliente/', cliente)
        self.assertEqual(response.status_code, 201)

    def test_post_cliente_status_code_400(self):
        cliente ={'nome_completo': 'john', 'email': 'diego@example.com'}
        response = self.client.post('http://127.0.0.1:8000/cliente/',cliente)
        self.assertEqual(response.status_code, 400)

    def test_put_cliente_por_email_status_code_200(self):
        cliente = {'nome_completo': 'diego britto', 'email': 'diegosouza@example.com'}
        response = self.client.put('http://127.0.0.1:8000/cliente/diego@example.com/',data=cliente,content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_put_cliente_por_email_status_code_400(self):
        cliente = {'nome_completo': 'john', 'email': 'diegobritto@example.com'}
        response = self.client.put('http://127.0.0.1:8000/cliente/diego@example.com/',data=cliente,content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_delete_cliente_por_email_status_code_204(self):
        response = self.client.delete('http://127.0.0.1:8000/cliente/diego@example.com/')
        self.assertEqual(response.status_code, 204)

    def test_delete_cliente_por_email_status_code_404(self):
        response = self.client.delete('http://127.0.0.1:8000/cliente/esteemail@naoexiste.com/')
        self.assertEqual(response.status_code, 404)

# Create your tests here.
