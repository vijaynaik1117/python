a = "kamalini"
print(a.capitalize()) # it will change first letter to be capital
print(a.upper())
print(a.lower()) 

b = '7'
print(b.isnumeric())
print(b.isalpha())

c = ' Mike is good boy'
print(c.startswith( 'Mike'))
print(c.endswith( 'Mike'))
print(c.replace('Mike', 'Nick'))
print(c.find('g'))
print(c.lstrip())
print(c.split())
print(c.splitlines())
d = 'Mike', 'Nick'
print(d)
e = ','
print(e.join(d))