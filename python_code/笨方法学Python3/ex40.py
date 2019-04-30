# 本章要点：字典 key - values
# 1. dict = {"key":"value"}
# 2. get： dict["key"]
# 3. set:  dict = {"key":"value"}  or  stuff[“1”] = "20"
# 4. 删除： del(dict["key"])
# 5. 
stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}

print(stuff["name"])
print(stuff["age"])

stuff["city"] = "San Francisco"

print(stuff)


stuff[1] = "20"

print(stuff)


stuff["2"] = "2"

print(stuff)


del(stuff["2"])

print(stuff)


cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'New York' 
cities['OR'] = 'Portland'

def find_city(themap, state): 
	if state in themap:
		return themap[state] 
	else:
		return "Not found."


print(cities)

while True:
	print("State? (ENTER to quit)") 
	state = input("> ")


