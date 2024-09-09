import asyncio
from django.http import HttpResponse

# View assíncrona com contador de tempo
async def timer_view(request):
    for i in range(1, 6):
        await asyncio.sleep(1)
        print(f"Contador: {i}")
    return HttpResponse("Contagem finalizada!")
