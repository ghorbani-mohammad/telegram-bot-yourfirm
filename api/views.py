import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from api.commands import Message


@csrf_exempt
@require_POST
def push_data(request):
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponse(status=400)
    Message.process_data(data)
    return HttpResponse(status=204)
