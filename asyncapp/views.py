import asyncio
from time import sleep
import httpx
from django.http import HttpResponse

# View assíncrona com um contador de tempo
async def timer_view(request):
    for num in range(1, 6):
        await asyncio.sleep(1)  # Contagem de tempo simulada
        print(f"Timer: {num}")
    return HttpResponse("Contagem de tempo concluída!")

# View assíncrona de exemplo
async def async_view(request):
    async with httpx.AsyncClient() as client:
        r = await client.get('https://httpbin.org/')
        print(r.text)
    return HttpResponse("Non-blocking HTTP request realizada!")

# View síncrona de exemplo
def sync_view(request):
    sleep(5)  # Simula uma chamada bloqueante
    return HttpResponse("Blocking HTTP request realizada!")

# View da página inicial
def home_view(request):
    return HttpResponse("Bem-vindo à página inicial!")
