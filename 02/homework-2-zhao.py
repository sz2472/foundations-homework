#shengying
#05/25/2016
#Homework 2

numbers = [22,90,0,-10,3,22,48]
print(numbers)
print(numbers[3])
print((numbers[1]) + numbers[3])
print(sorted(numbers))
#sort doesn't last in another line
print(sorted(numbers)[5])
print(numbers[6])
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
total=0
for number in numbers:
    new_number= number/2
    total= new_number+total
print("Our answer", total)
movie_info = {'movie title':'English Patient','Year': 1996, 'director name': 'Anthony Minghella','Budget':'35', 'Box office': '232'}
print("My favorite movie is",movie_info['movie title'],"which was released in", movie_info['Year'],"and was directed by", movie_info['director name'])
print (int(movie_info['Box office'])-int(movie_info['Budget']),"million")

if int(movie_info['Budget'])*5 > int(movie_info['Box office']):
    print("That was a good investment")
if int(movie_info['Budget'])*5 < int(movie_info['Box office']):
    print("It was a flop")

NYCpopulation = {'Manhattan':1.6,'Brooklyn':2.6,'Bronx':1.4,'Queens':2.3,'Staten Island':0.47}
print(NYCpopulation['Brooklyn'],'million')
print('The combined  population is', NYCpopulation['Manhattan']+NYCpopulation['Brooklyn']+NYCpopulation['Bronx']+NYCpopulation['Queens']+NYCpopulation['Staten Island'],'million')

total=NYCpopulation['Manhattan']+NYCpopulation['Brooklyn']+NYCpopulation['Bronx']+NYCpopulation['Queens']+NYCpopulation['Staten Island']
print(round(NYCpopulation['Manhattan']/total*100.2),'percent')
