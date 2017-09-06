import requests
import sys
import datetime
import json

from subprocess import call
import requests

TOKEN = json.loads(open('config.json', 'r').read())


def send_notification():
    call(['notify-send', 'MENUSY! MENUSY! MENUSY! MENUSY! MENUSY!', '--urgency=critical'])

def get_feed():
    response = requests.get(
        'https://graph.facebook.com/v2.10/1735305803424923/feed?access_token=268353497010712%7CkGpy1aemxt3oA81WMW-QEUvfGuU'
    )
    post = response.json()['data'][0]
    post_time = datetime.datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S%z')
    if post_time.date() == datetime.datetime.now().date():
        if 'tu zjesz' in post['message'].lower():
            send_notification()
            sys.exit(0)
    sys.exit(1)

get_feed()