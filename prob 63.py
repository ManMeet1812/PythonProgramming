country_code = {'India': '0092' , 'Australia': '0097', 'Nepal': '0094'}
print(country_code.get('India', 'Not Found'))
print(country_code.get('Japan', 'Not Found'))

##############################################################################
country_code = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
 
# Set a default value for Japan
country_code.setdefault('Japan', 'Not Present')
print(country_code['Australia'])
print(country_code['Japan'])


#############################################################################
import collections
defd = collections.defaultdict(lambda: 'key not found')
defd['a'] = 45
defd['b'] = 60

print(defd['a'])
print(defd['c'])
