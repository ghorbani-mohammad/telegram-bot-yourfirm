# Telegrambot

You need python 3.8.x or higher

## Development Setup
* Create a virtual environment `python -m venv venv`
* Activate virtual environment
* Update pip just in case `pip install -U pip`
* Install requirements `pip install -r requirements.txt`
* Run migrations `python manage.py migrate`
* Start django dev server `python manage.py runserver`

## Ngrok Tunnel and Telegram Bot Setup
1. Download ngrok
2. Start django dev server 0.0.0.0:8000
3. Run ngrok:
	- ngrok authtoken <yourtoken>
	- ngrok http localhost:8000
4. Create a bot in telegram @Botfather.
5. Register your websocket to telegram by calling:
	- `https://api.telegram.org/bot{TOKEN}/setWebhook?url={NGROK_URL}/api/push_data`
	If all goes well the enpoint returns: `{'ok': ture, 'result': true, 'description': "Webhook was set"}`
6. Update settings.py `TELEGRAM_AUTH_TOKEN`.
