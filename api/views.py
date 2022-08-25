import json
import logging

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from api.commands import Message
logger = logging.getLogger(__name__)


@csrf_exempt
@require_POST
def push_data(request):
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return HttpResponse(status=400)

    # We only consider SendMessage type requests that are text message
    # EditMessage or file messages will be ignored
    if ('message' in data) and ('text' in data['message']):
        message = Message(data['message']['chat']['id'], data['message']['text'])
        message.process_data(data)
        return HttpResponse(status=200)
    return HttpResponse(status=204)
