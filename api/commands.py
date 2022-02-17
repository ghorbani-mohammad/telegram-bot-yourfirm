import requests

from django.conf import settings


class Message:
    def __init__(self, chat_id, text, **kwargs):
        self.message = dict(chat_id=chat_id, text=text, **kwargs)

    @classmethod
    def process_data(cls, data):
        # THIS IS LAME :), PLEASE PROPOSE A BETTER APPROACH
        message = data['message']
        cmd = Command(message)

        if message['text'].lower() == 'ping':
            cmd.ping()
        else:
            cmd.unknown()

    def send_response(self):
        url = settings.TELEGRAM_URL + 'sendMessage'
        r = requests.post(url, json=self.message)
        if r.status_code != 200:
            #  TODO: check if response is correct
            pass

    def prepare_message(self, user_id, text):
        pass


class Command:
    def __init__(self, message):
        self.message = message

    def subscribe(self):
        pass

    def unsubscribe(self):
        pass

    def list_subscribes(self):
        pass

    def ping(self):
        message = Message(chat_id=self.message['chat']['id'], text='PONG')
        message.send_response()

    def unknown(self):
        message = Message(chat_id=self.message['chat']['id'], text='unkown command')
        message.send_response()
