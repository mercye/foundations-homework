# EJ (Mercy) Emelike
# May 23, 2016
# Homework 1

yob = input("What year were you born?")
age = 2016 - int(yob)

#do not allow year of birth to be in the future
if age < 0:
    print("Impossible! Try a year in the PAST. One more time.")
    yob = input("What year were you born?")
#if year of birth is not in the future
elif age >= 0:
    print("So, you're about", age, "years old.")

# how many times their heart has beaten
# heartbeats = average bpm * minutes in a year * age
heartbeat = 72*525600*age
print("And your heart has beaten", heartbeat, "times.")

#blue whale heart beats (6 bpm)
heartbeat_blwhale = 6*525600*age
print("This is more than a blue whale's heart, which has beaten", heartbeat_blwhale, "times.")


# rabbit heart beats (205 bpm)
heartbeat_rabbit = 140*525600*age
hb_rb_divided = heartbeat_rabbit/1000000000
print("And less than a rabbit's, which has beaten", hb_rb_divided, "billon times.")

# age on venus
# 225 days in an earth year on Venus
age_venus = (age*365)/225
print("If you lived on Venus then you'd be approximately", "%.2f" % age_venus, "years old.")

# age on neptune
# 165 years in an earth year on Neptune
age_neptune = age/165
print("And if you lived on Neptune, you'd be about", "%.2f" % age_neptune, "years old.")

# older, younger, or same age
if age > 26:
    print("I'm 26, so you're older than me.")
elif age < 26:
    print("I'm 26, so you're younger than me.")
elif age == 26:
    print("We're the same age!")

difference = abs(26 - age)

if age != 26:
    print("We are", difference, "years apart.")

#born in an even or odd year
if int(yob) % 2 == 0:
    print("You were born in an EVEN year.")
elif int(yob) % 2 != 0:
    print("You were born in an ODD year.")

# Steelers have won the superbowl in 2008, 2005, 1979, 1978, 1975, 1974
if int(yob) <= 1974:
    print("The Pittsburgh Steelers have won 6 super bowls since you were born.")
elif int(yob) == 1975:
    print("The Pittsburgh Steelers have won 5 super bowls since you were born.")
elif 1976 <= int(yob) <= 1978:
    print("The Pittsburgh Steelers have won 4 super bowls since you were born.")
elif int(yob) == 1979:
    print("The Pittsburgh Steelers have won 3 super bowls since you were born.")
elif 1979 < int(yob) <= 2005:
    print("The Pittsburg Steelers have won 2 super bowls since you were born.")
elif 2006 <= int(yob) <= 2008:
    print("The Pittsburg Steelers have won 1 super bowls since you were born.")
else:
    print("The Pittsburg Steelers haven't won any superbowls since you were born.")

#which president in office when they were born
if int(yob) < 1933:
    print ("Sorry, couldn't tell you who the president was when you were born.")
elif 1933 <= int(yob) < 1945:
    print ("And the president was Franklin D. Roosevelt when you were born")
elif 1945 <= int(yob) < 1953:
    print ("And the president was Harry S. Truman when you were born")
elif 1953 <= int(yob) < 1961:
    print ("And the president was Dwight D. Eisenhower when you were born")
elif 1961 <= int(yob) <= 1963:
    print ("And the president was John F. Kennedy when you were born")
elif 1963 < int(yob) < 1969:
    print ("And the president was Lyndon B. Johnson when you were born")
elif 1969 < int(yob) <= 1974:
    print ("And the president was Richard Nixon when you were born")
elif 1974 < int(yob) < 1977:
    print ("And the president was Gerald Ford when you were born")
elif 1977 <= int(yob) < 1981:
    print ("And the president was Jimmy Carter when you were born")
elif 1978 <= int(yob) < 1989:
    print ("And the president was Ronald Reagan when you were born")
elif 1989 <= int(yob) < 1993:
    print ("And the president was George H. W. Bush when you were born")
elif 1993 <= int(yob) < 2001:
    print ("And the president was Bill Clinton when you were born")
elif 2001 <= int(yob) < 2009:
    print ("And the president was George W. Bush when you were born")
elif int(yob) >= 2009:
    print ("And the president was Barack Obama when you were born")
