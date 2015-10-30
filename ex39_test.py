import hashmap


# creat a mapping of state ot abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'DCity')
hashmap.set(cities, 'FL', 'Miami')

# add some more cities
hashmap.set(cities, 'NY', 'NYC')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print '-' * 10
print "NY state has %s" % hashmap.get(cities, 'NY')
print "OR state has %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan abbres is %s" % hashmap.get(states, 'Michigan')


print '-' * 10
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreve
print '-' * 10
hashmap.list(states)

# print every city in states
print '-' * 10
hashmap.list(cities)


print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry no tx"

city = hashmap.get(cities, "TX", 'Does not exist')
print "The city for the state of tx is %s" % city
