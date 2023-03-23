string="O+ve x 2,O-ve x 3"

s=string.split(',')
for x in s:
    str = x.split('x')
    print(str[0],str[1])