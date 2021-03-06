import requests
import sys
import datetime
import json

from subprocess import call

checkPhrases = ['tu zjesz', 'na wynos']


with open('config.json', 'r') as config_file:
    TOKEN = json.loads(config_file.read())['access_token']

def send_notification():
    call(['notify-send', 'MENUSY! MENUSY! MENUSY! MENUSY! MENUSY!', '--urgency=critical'])

def get_feed():
    response = requests.get(
        'https://graph.facebook.com/v2.10/1735305803424923/feed?access_token={}'.format(TOKEN))
    post = response.json()['data'][0]
    post_time = datetime.datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S%z')
    if post_time.date() == datetime.datetime.now().date():
        if any(phrase in post['message'].lower() for phrase in checkPhrases):
            with open('/tmp/menu.txt', 'w') as menu_file:
                menu_file.write(post['message'])
            send_notification()
            sys.exit(0)
    sys.exit(1)

if __name__ == '__main__':
    get_feed()
