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
    # If request is not SendMessage, we do nothing
    try:
        message = Message(data['message']['chat']['id'], data['message']['text'])
    except Exception as e:
        logger.error(f"error: {e}, data: {data}")
        return HttpResponse(status=204)
    message.process_data(data)
    return HttpResponse(status=200)
