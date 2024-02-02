
# for loop
squares = []                        # instantiate empty list
for number in range(10):
    squares.append(number * number)
print(squares)

# functional programming: map
prices = [1.09, 23.56, 57.84, 4.56, 6.78]  # iterable
TAX_RATE = .08
def get_price_with_tax(price):
    return price * (1 + TAX_RATE)

final_prices = map(get_price_with_tax, prices)  # map returns an iterator \
                                    # that yields transformed items on demand
                                    # first argument is function object and \
                                    # not a function call therefore no parentheses
print(final_prices)                 # prints map object
print(list(final_prices))           # prints list of final prices
# map() is written in C and faster than a for loop
# memory efficient since you can access objects on demand without storing the full list

# lambda functions are useful with map
final_prices = map(lambda price: price * (1 + TAX_RATE), prices)
print(final_prices)

# list comprehensions
squares = [number * number for number in range(10)]
final_prices = [get_price_with_tax(price) for price in prices]
# returns list instead of map object

## conditional
sentence = "the rocket came back from mars"
vowels = [char for char in sentence if char in "aeiou"] 
print(vowels)

## complex conditional
sentence = (
    "The rocket, who was named Ted, came back "
    "from Mars because he missed his friends"
)
def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels

consonants = [char for char in sentence if is_consonant(char)]
print(consonants)

## new list with condition (condition at beginning)
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [price if price > 0 else 0 for price in original_prices]
print(prices)
## same as
def get_price(price):
    return price if price > 0 else 0
prices = [get_price(price) for price in original_prices]
print(prices)

## can also do set comprehensions and dict comprehensions
squares = {number: number * number for number in range(10)}
print(squares)

## example walrus operator :=
import random
def get_weather_data():
    return random.randrange(90, 110)

print(
    [temp for _ in range(20) if (temp:= get_weather_data()) >= 100]
)

# List comprehensions
# can be clean and easy to read and debug
# but can be slow, or harder to read if too complex

## nested comprehensions
cities = ["Austin", "Tacoma", "Topeka", "Sacramento", "Charlotte"]
high_temp_per_city = {city: [0 for _ in range(7)] for city in cities}
print(high_temp_per_city)

a_matrix = [[number for number in range(5)] for _ in range(6)]
print(a_matrix)

## not intuitive nested comprehensions
## flattening a matrix
lcomp_flat = [number for row in a_matrix for number in row]
print(lcomp_flat)

forl_flat = []
for row in a_matrix:
    for number in row:
        forl_flat.append(number)
print(forl_flat)
## much more intuitive

## list comprehensions are slow with very large lists 1000<<<<
## use generators to create iterator that can generate next value
## using next(), uses lazy evaluation

#print(sum([number * number for number in range(1000)])) # list comp
#print(sum(number * number for number in range(1_000_000_000))) # generator
## map() also uses lazy evaluation

# question: does performance matter?
# if not, choose approach for cleanest code
# if it does: use profiling and time the approaches

