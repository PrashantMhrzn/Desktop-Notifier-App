import requests
from datetime import date
import time
from plyer import notification

data = None
try:
    data = requests.get("https://nepalcorona.info/api/v1/data/nepal")
except:
    print('Check your internet connection!')

if data != None:
    text = data.json()


tested_total = text['tested_total']
tested_positive = text['tested_positive']
tested_negative = text['tested_negative']
recovered = text['recovered']
deaths = text['deaths']


while True:
    notification.notify(
        title=f'COVID-19 status of Nepal on {date.today()}',
        message=f'Total Tested:{tested_total}\nTotal Positive:{tested_positive}\nTotal Negative:{tested_negative}\nRecovered:{recovered}\nDeaths:{deaths}',
        # Shows notification for 45 seconds
        timeout=45
    )

    # Shows notification after every 3 hours
    time.sleep(60*60*3)  