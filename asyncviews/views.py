import asyncio
from django.http import JsonResponse
from django.http import HttpResponse


def home(request):
    return JsonResponse({"message": "Bem-vindo à API!"})


async def async_counter():
    for i in range(1, 6):
        await asyncio.sleep(1)
        print(f"Contando: {i}")

async def async_counter_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(async_counter())  # executa em segundo plano
    return HttpResponse("Contador iniciado (não bloqueante)")

