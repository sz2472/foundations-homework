# Grade: 12.5 / 15

#shengying
#05/25/2016
#Homework 2

numbers = [22,90,0,-10,3,22,48]

# TA-COMMENT: (-0.5) This question actually asked you to print the number of elements in your list (which is 7).
print(numbers)

print(numbers[3])
print((numbers[1]) + numbers[3])
print(sorted(numbers))
#sort doesn't last in another line
print(sorted(numbers)[5])
print(numbers[6])

# TA-COMMENT: (-1) You don't want to look through every number every time and perform just one calculation and then print; theoretically, you should structure your if-statements in such a manner as to follow the logic stated in the question. 

for number in numbers:
    if number < 10:
        print(number*30)
for number in numbers:
    if number < 10 and number % 2 == 0:
        print(number+6)

for number in numbers:
    if number > 50:
        print (number-10)

for number in numbers:
    if number > -10:
        print (number-1)

# TA-COMMENT: Here's an alternate solution to Question 6:

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

# TA-COMMENT: Let me know if you have any questions about the alternate code above.

total=0
for number in numbers:
    new_number= number/2
    total= new_number+total
print("Our answer", total)
movie_info = {'movie title':'English Patient','Year': 1996, 'director name': 'Anthony Minghella','Budget':'35', 'Box office': '232'}

# TA-COMMENT: (-0.5) We can add entries to a dictionary AFTER making it. We wanted to see:
# movie['budget'] = 94000000
# rather than "hard coding" budget and revenue into the initial dictionary.


print("My favorite movie is",movie_info['movie title'],"which was released in", movie_info['Year'],"and was directed by", movie_info['director name'])
print (int(movie_info['Box office'])-int(movie_info['Budget']),"million")

if int(movie_info['Budget'])*5 > int(movie_info['Box office']):
    print("That was a good investment")

# TA-COMMENT: (-0.5) This isn't exactly what the question asked for. The directions state: If the movie cost more to make than it made in theaters, print "It was a flop". If the film's revenue was more than five times the amount it cost to make, print "That was a good investment."

if int(movie_info['Budget'])*5 < int(movie_info['Box office']):
    print("It was a flop")

NYCpopulation = {'Manhattan':1.6,'Brooklyn':2.6,'Bronx':1.4,'Queens':2.3,'Staten Island':0.47}
print(NYCpopulation['Brooklyn'],'million')
print('The combined  population is', NYCpopulation['Manhattan']+NYCpopulation['Brooklyn']+NYCpopulation['Bronx']+NYCpopulation['Queens']+NYCpopulation['Staten Island'],'million')

total=NYCpopulation['Manhattan']+NYCpopulation['Brooklyn']+NYCpopulation['Bronx']+NYCpopulation['Queens']+NYCpopulation['Staten Island']
print(round(NYCpopulation['Manhattan']/total*100.2),'percent')
