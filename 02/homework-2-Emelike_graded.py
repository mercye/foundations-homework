# Grade: 14 / 15

# EJ (Mercy) Emelike
# May 26, 2016
# Homework 2

#LISTS
# 0) make list
numbers = [22, 90, 0, -10, 3, 22, 48]

# 1) print list
print(numbers) # TA-COMMENT: (-0.5) We were looking for the number of elements in the list -- len(numbers).

# 2) print 4th element of list
print(numbers[3])

# 3) print sum of 2nd and 4th element
print(numbers[1] + numbers[3])

# 4) print 2nd largest value
numbers_sorted = sorted(numbers)
print (numbers_sorted[5])
# TA-COMMENT: There is a programmatic way to display the second largest value in a list (other than calling it by its index). For example: numbers_sorted[(len(numbers_sorted) - 2)] OR: numbers_sorted[-2].

# 5) print last element of the original unsorted list
print(numbers[6])
# TA-COMMENT: Same comment applies -- numbers[-1] is the most efficient way.

# 6)

# TA-COMMENT: This produces the correct output; however, you "hard-coded" every possibility in your if/elif statements. Theoretically, we would want to structure our if-statements in such a manner that we didn't have to list calculations for all possibilities and could rely on the logic of what we've written to do the "right" thing. Plus this violates our principle of Don't Repeat Yourself.

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

# TA-COMMENT: This is an alternate solution to Question 6:

for number in numbers:
	original = number

	if original < 10:
		number = number * 30

		if (original%2) == 0:
			number = number + 6

	elif original > 50:
		number = number - 10

	if original != -10:
		number = number - 1

	print(number)

# 7) sum the result of each of the numbers divided by two
new_numbers = [number/2 for number in numbers] # TA-COMMENT: Cool! We haven't gone over this syntax yet, but it definitely works! And it's one of the more efficient solutions.

sum_numbers = sum(new_numbers)
print (sum_numbers)

# 8) DICTIONARIES
movie = {'title': 'Finding Nemo', 'year': '2003', 'director': 'Andrew Stanton', 'budget': 94000000, 'revenue': 936700000 }

# TA-COMMENT: (-0.5) We can add entries to a dictionary AFTER making it. We wanted to see:
# movie['budget'] = 94000000
# rather than "hard coding" budget and revenue into the initial dictionary.

print ('My favorite movie is', movie['title'], 'which was released in', movie['year'], 'and was directed by', movie['director'])

#9
difference = movie['revenue'] - movie['budget']
print(difference)

# 10)
# TA-COMMENT: Good job reading Soma's directions carefully!
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
pct_Mnhttn = (populations['Manhattan'] / tot_pop)*100 # TA-COMMENT: Probably should have a percent sign in the print as well.
print(pct_Mnhttn)
