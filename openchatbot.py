import random
import json
import time
import math

print('OpenChatBot 0.1.0 (github.com/BotNC/openchatbot)\n')

responses = []

with open('responses.json', 'r') as f:
    responses = json.loads(f.read())

while True:
    try:
        chat = input('Talk to OpenChatBot: ')
    except KeyboardInterrupt:
        print('Oh well. Goodbye. I hope I can see you again...')
        break

    try:
        print(random.choice(responses[chat]))
    except KeyError:
        print(random.choice(responses['error']))
