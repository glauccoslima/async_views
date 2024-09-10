from django.test import TestCase, AsyncClient, Client
from django.urls import reverse
import httpx

class AsyncAppTests(TestCase):

    def setUp(self):
        # O Django Client é usado para testar as views síncronas
        self.client = Client()
        # O Django AsyncClient é usado para testar as views assíncronas
        self.async_client = AsyncClient()

    def test_sync_view(self):
        """
        Testa se a view síncrona retorna o código de status HTTP 200
        e se o conteúdo esperado está presente.
        """
        response = self.client.get(reverse('sync_view'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Blocking HTTP request', response.content)

    async def test_async_view(self):
        """
        Testa se a view assíncrona retorna o código de status HTTP 200
        e se o conteúdo esperado está presente.
        """
        response = await self.async_client.get(reverse('async_view'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Non-blocking HTTP request', response.content)

    def test_home_view(self):
        """
        Testa se a view da página inicial retorna o código de status HTTP 200
        e verifica se o conteúdo da página inicial é o esperado.
        """
        response = self.client.get(reverse('home_view'))
        self.assertEqual(response.status_code, 200)
        # Corrigir o conteúdo esperado para refletir a página inicial correta
        self.assertIn(b'Bem-vindo \xc3\xa0 p\xc3\xa1gina inicial!', response.content)

    async def test_http_call_async(self):
        """
        Testa uma chamada HTTP assíncrona para um serviço externo.
        Verifica se a chamada ao https://httpbin.org/get retorna um código de status 200.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get('https://httpbin.org/get')
            self.assertEqual(response.status_code, 200)

    def test_http_call_sync(self):
        """
        Testa uma chamada HTTP síncrona para um serviço externo.
        Verifica se a chamada ao https://httpbin.org/get retorna um código de status 200.
        """
        response = httpx.get('https://httpbin.org/get')
        self.assertEqual(response.status_code, 200)
