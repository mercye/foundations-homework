# EJ (Mercy) Emelike
# May 26, 2016
# Homework 2

#LISTS
# 0) make list
numbers = [22, 90, 0, -10, 3, 22, 48]

# 1) print list
print(numbers)

# 2) print 4th element of list
print(numbers[3])

# 3) print sum of 2nd and 4th element
print(numbers[1] + numbers[3])

# 4) print 2nd largest value
numbers_sorted = sorted(numbers)
print (numbers_sorted[5])

# 5) print last element of the original unsorted list
print(numbers[6])

# 6)
for number in numbers:
    if number < 10 and number % 2 == 0 and number != -10:
        new_number = ((number * 30) + 6) - 1
        print(new_number)
    elif number < 10 and number % 2 != 0 and number != -10:
        new_number = (number*30) - 1
        print(new_number)
    elif number < 10 and number % 2 == 0 and number == -10:
        new_number = ((number * 30) + 6)
        print(new_number)
    elif number > 10 and number < 50 and number != -10:
        new_number = (number - 1)
        print(new_number)
    elif number > 50 and number != -10:
        new_number = (number - 10) - 1
        print(new_number)
    else:
        print(number)

# 7) sum the result of each of the numbers divided by two
new_numbers = [number/2 for number in numbers]
sum_numbers = sum(new_numbers)
print (sum_numbers)

# 8) DICTIONARIES
movie = {'title': 'Finding Nemo', 'year': '2003', 'director': 'Andrew Stanton', 'budget': 94000000, 'revenue': 936700000 }
print ('My favorite movie is', movie['title'], 'which was released in', movie['year'], 'and was directed by', movie['director'])

#9
difference = movie['revenue'] - movie['budget']
print(difference)

# 10)
if movie['revenue'] < movie['budget']:
    print ('it was a flop.')
elif movie['revenue'] >= movie['budget'] * 5:
    print ('that was a good investment')

# 11)
populations = {'Manhattan': 1600000, 'Brooklyn': 2600000, 'Bronx': 1400000, 'Queens': 2300000, 'Staten Island': 470000}

# 12)
print(populations['Brooklyn'])

# 13)
tot_pop = sum(populations.values())
print (tot_pop)

# 14)
pct_Mnhttn = (populations['Manhattan'] / tot_pop)*100
print(pct_Mnhttn)
