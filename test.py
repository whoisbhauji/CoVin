import requests
import json
import datetime

pincode = '600004'
today = datetime.date.today()

url1 = 'https://cdn-api.co-vin.in/api'
url2 = "/v2/appointment/sessions/public/findByPin"
url3 = "/v2/appointment/sessions/public/findByPin"

q1 = '?pincode='+pincode+'&date='+today.strftime("%d/%m/%Y")

resp = requests.get(url1+url2+q1)
data = json.loads(resp.text)

print("Center Name      ", " Available capacity",
      " Min Age", " vaccine", " Fee type ")

for session in data['sessions']:

    print(session['name'], end=' | ')
    print(session['available_capacity'], end=' | ')
    print(session['min_age_limit'], end=' | ')
    print(session['vaccine'], end=' | ')
    print(session['fee_type'], end=' | ')
    print()

    if session['min_age_limit'] < 45 and session['available_capacity'] > 0:
        # Add code to notify
        pass
