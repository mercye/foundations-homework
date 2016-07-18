import requests
import datetime

response = requests.get("https://api.forecast.io/forecast/a197f06e1906b1a937ad31d4378b8939/40.8116,-73.9465")
data = response.json()
# print(data.keys())

curr_data = data['currently']
daily_data = data['daily']['data'][0]

# print(daily_data)

temperature = curr_data['temperature']
daily_temp = daily_data['apparentTemperatureMax']
summary = curr_data['summary'].lower()
high_temp = daily_data['temperatureMax']
low_temp = daily_data['temperatureMin']
precipProbability = daily_data['precipProbability']

def temp_feeling(daily_temp):
    if daily_temp <= 32:
        return "freezing"
    if daily_temp > 32 and daily_temp <= 50:
        return "cold"
    if daily_temp > 50 and daily_temp <= 75:
        return "moderate"
    if daily_temp > 75 and daily_temp <= 85:
        return "warm"
    if daily_temp > 85:
        return "hot"

def rain_warning(precipProbability):
    if precipProbability >= 0 and precipProbability < 25:
        return "Leave the umbrella at home."
    if precipProbability >= 25 and precipProbability < 50:
        return "You could bring an umbrella, and it wouldn't be a terrible idea."
    if precipProbability >= 50 and precipProbability < 70:
        return "It'll probably rain. Strongly suggest an umbrella"
    if precipProbability >= 70:
        return "Bring your umbrella!"

# date is in unix timestamp
curr_time = int(curr_data['time'])
datestring = datetime.datetime.fromtimestamp(curr_time).strftime('%Y-%m-%d-%H-%M')
hour = datetime.datetime.fromtimestamp(curr_time).strftime('%H')
date = datetime.datetime.fromtimestamp(curr_time).strftime('%B %d, %Y')
filename = "forecast" + datestring + ".txt"
# print(filename)

msg = "Right now, it is " + str(temperature) + " degrees out and " + summary + ". Today will be " + temp_feeling(daily_temp) + " with a high of " + str(high_temp) + " and a low of " + str(low_temp) + ". " +      str(rain_warning(precipProbability))

sbj = hour + 'AM Weather Forecast: ' + date

key = 'key-5dd9bd308dc0ec27fc59315428752db9'
sandbox = 'sandboxd3b7978e5d4c4a62afbb4f83e74cbbd4.mailgun.org'
recipient = 'mercy.emelike@gmail.com'

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), data={
    'from': 'Mailgun Sandbox <postmaster@sandboxd3b7978e5d4c4a62afbb4f83e74cbbd4.mailgun.org',
    'to': recipient,
    'subject': sbj,
    'text': msg
})

print('Status: {0}'.format(request.status_code))
print('Body:   {0}'.format(request.text))
