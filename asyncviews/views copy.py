# import time
from django.http import JsonResponse

# def api(request):
#     time.sleep(1)
#     payload = {"message": "Hello from Crowbotics!"}

#     if "task_id" in request.GET:
#         payload["task_id"] = request.GET["task_id"]
#     return JsonResponse(payload)

def home(request):
    return JsonResponse({"message": "Bem-vindo à API!"})


from time import sleep
import asyncio
import httpx
#from django.http import JsonResponse
from django.http import HttpResponse

async def http_call_async():
    # Simula uma operação assíncrona
    # payload = {"message": "Hello from Crowbotics!"}

    # if "task_id" in request.GET:
    #     payload["task_id"] = request.GET["task_id"]
        
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)

    # Faz uma chamada HTTP assíncrona
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/")
        # payload["http_status"] = response.status_code
        print(response)

# Faz uma chamada HTTP síncrona
def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    response = httpx.get("https://httpbin.org/")
    print(response)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-bloking HTTP request")


def sync_view(request):
    http_call_sync()
    return HttpResponse("Bloking HTTP request")