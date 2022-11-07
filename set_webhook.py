# set webhook
# https://habr.com/ru/post/486826/
import requests
import json
from config import BOT_CONFIG

auth_token = BOT_CONFIG['auth_token']
hook = 'https://chatapi.viber.com/pa/set_webhook'
headers = {'X-Viber-Auth-Token': auth_token}


sen = dict(url='https://tendra.win',
           event_types=['unsubscribed', 'conversation_started', 'message', 'seen', 'delivered'])
# sen - это body запроса для отправки к backend серверов viber
# seen, delivered - можно убрать, но иногда маркетологи хотят знать,
# сколько и кто именно  принял и почитал ваших сообщений,  можете оставить)

r = requests.post(hook, json.dumps(sen), headers=headers)
# r - это пост запрос составленный по требованиям viber
print(r.json())
# в ответном print мы должны увидеть "status_message":"ok" - и это значит,
# что вебхук установлен
