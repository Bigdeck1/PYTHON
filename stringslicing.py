#string slicing

name = "itang pogi"

first_name = name[:5]
last_name = name[6:]

pang_name = name[0::2]
reversed_name = name[::-1]
print(first_name)
print (last_name)
print(pang_name)
print(reversed_name)

website = "http://facebook.com"
website1 = "http://pangit.com"
slice = slice(7,-4)
print(website[slice])
print(website1[slice])
