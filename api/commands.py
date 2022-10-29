import logging
import requests

from django.conf import settings

from .models import Profile, Subscription
from .models import Message as SentMessage

logger = logging.getLogger(__name__)


class Message:
    def __init__(self, chat_id, text, **kwargs):
        self.message = dict(chat_id=chat_id, text=text, parse_mode='Markdown', **kwargs)
        self.profile = self.get_profile(chat_id)

    @classmethod
    def get_profile(cls, user_id):
        return Profile.objects.get_or_create(user_id=user_id)[0]

    def process_data(self, data):
        message = data['message']
        message_term = message['text'].lower().replace('/', '').split()
        if not len(message_term):
            # if command was empty
            cmd = Command(self.profile, None, None)
            cmd.unknown()
            return
        command = message_term[0]
        term = ' '.join(message_term[1:])
        cmd = Command(self.profile, command, term)

        if command == 'start':
            cmd.start()
        elif command == 'ping':
            cmd.ping()
        elif command == 'subscribe':
            cmd.subscribe()
        elif command == 'unsubscribe':
            cmd.unsubscribe()
        elif command == 'show':
            cmd.list_subscribes()
        else:
            cmd.unknown()

    def send_response(self):
        url = settings.TELEGRAM_URL + 'sendMessage'
        r = requests.post(url, json=self.message)
        if r.status_code != 200:
            error = f"r_code: {r.status_code},\nr_text: {r.text}\nmessage: {self.message}"
            logger.error(error)
            return
        SentMessage.objects.create(profile=self.profile, text=self.message['text'])


class Command:
    def __init__(self, profile, command, term=None):
        self.term = term
        self.profile = profile
        self.command = command

    def start(self):
        self.create_message(text='Hello!')

    def empty_term(self):
        if self.term == '':
            self.create_message(text='Please specify your interested term like python.')
            return True

    def subscribe(self):
        if self.empty_term():
            return
        if not Subscription.objects.filter(profile=self.profile, term=self.term).exists():
            Subscription.objects.create(profile=self.profile, term=self.term)
        self.create_message(text='Subscribed')

    def ping(self):
        self.create_message(text='PONG')

    def unsubscribe(self):
        if self.empty_term():
            return
        Subscription.objects.filter(profile=self.profile, term=self.term).delete()
        self.create_message(text='Unsubscribed')

    def list_subscribes(self):
        subscriptions = Subscription.objects.filter(profile=self.profile)\
            .values_list('term', flat=True)
        if len(subscriptions) == 0:
            self.create_message(text='You are not subscribed to any term')
            return
        self.create_message(text='\n'.join(subscriptions))

    def unknown(self):
        self.create_message(text='Unknown Command')

    def create_message(self, text):
        response = Message(chat_id=self.profile.user_id, text=text)
        response.send_response()
