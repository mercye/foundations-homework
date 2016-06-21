# EJ (Mercy) Emelike
# Homework 9
# June 22, 2016

#imports
import pandas as pd
import dateutil.parser

#sample dictionary
earthquake = {
      'rms': '1.85',
      'updated': '2014-06-11T05:22:21.596Z',
      'type': 'earthquake',
      'magType': 'mwp',
      'longitude': '-136.6561',
      'gap': '48',
      'depth': '10',
      'dmin': '0.811',
      'mag': '5.7',
      'time': '2014-06-04T11:58:58.200Z',
      'latitude': '59.0001',
      'place': '73km WSW of Haines, Alaska',
      'net': 'us',
      'nst': '',
      'id': 'usc000rauc'}

# PART ONE

def depth_to_words(depth):
    int_depth = int(depth)
    if int_depth > 0 and int_depth < 70:
        return "shallow"
    if int_depth >= 70 and int_depth < 300:
        return "intermediate"
    if int_depth >= 300 and int_depth < 700:
        return "deep"

def power_to_words(magnitude):
    flt_magnitude = float(magnitude)
    if flt_magnitude > 0 and flt_magnitude < 5:
        return "small"
    if flt_magnitude >= 5 and flt_magnitude < 7:
        return "moderate"
    if flt_magnitude >= 7 and flt_magnitude < 8:
        return "major"
    if flt_magnitude >= 8 and flt_magnitude < 9.5:
        return "great"
    if flt_magnitude >= 9.5:
        return "super"

def day_in_words(time):
    timestring = time
    eq_day = dateutil.parser.parse(timestring)
    return eq_day.strftime("%A")

def time_in_words(time):
    timestring = time
    eq_time = dateutil.parser.parse(timestring)
    if eq_time.hour >= 0 and eq_time.hour < 12:
        return "morning"
    if eq_time.hour >= 12 and eq_time.hour < 17:
        return "afternoon"
    if eq_time.hour >= 17 and eq_time.hour < 21:
        return "evening"
    if eq_time.hour >= 21 and eq_time.hour < 24:
        return "night"

def date_in_words(time):
    timestring = time
    eq_date = dateutil.parser.parse(timestring)
    return eq_date.strftime("%b %d")

# PART TWO

def eq_to_sentence(earthquake):
    print("A",  depth_to_words(earthquake['depth']), power_to_words(earthquake['mag']), earthquake['mag'], "earthquake was reported", day_in_words(earthquake['time']), time_in_words(earthquake['time']), "on", date_in_words(earthquake['time']), earthquake['place'])

eq_to_sentence(earthquake)

# PART THREE

earthquakes_df = pd.read_csv("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv")

# [eq_to_sentence(row) for index, row in earthquakes_df.iterrows() if earthquakes_df.ix[row, ['mag']] >= 4]

# for index, row in earthquakes_df.iterrows():
#     if earthquakes_df['mag'] >= 4:
#         eq_to_sentence(row)

earthquakes = earthquakes_df.to_dict('records')
[eq_to_sentence(item) for item in earthquakes if item['mag'] >= 4]


# PART FOUR

for item in earthquakes:
    if item['type'] != 'earthquake':
        print("There was also a magnitude", item['mag'], item['type'], "on", date_in_words(item['time']), item['place'])
