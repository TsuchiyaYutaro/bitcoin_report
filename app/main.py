import os, time, json
import requests
import schedule

import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv
load_dotenv('.env')
WEB_HOOK_URL = os.environ.get("WEB_HOOK_URL")

def _job():
    url = 'https://api.coin.z.com/public/v1/ticker'
    params = {'symbol': 'BTC'}
    response = requests.get(url, params=params)
    res_items = response.json()
    bitcoin_price = int(res_items['data'][0]['last'])

    message_json = json.dumps({
        'text'       : '現在の BITCOIN 価格は {bitcoin_price}円 です'.format(bitcoin_price=bitcoin_price),
        'username'   : 'BITCOIN REPORT',
        'icon_emoji' : ':bitcoin:',
        'link_names' : 1
    })

    requests.post(WEB_HOOK_URL, data=message_json)

if __name__ == '__main__':
    schedule.every(15).minutes.do(_job)

    while True:
        schedule.run_pending()
        time.sleep(1)