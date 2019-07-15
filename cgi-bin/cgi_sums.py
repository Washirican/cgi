#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()

form = cgi.FieldStorage()
# stringval = form.getvalue('a', None)
listval = form.getlist('operand')


print('Operands: {}'.format(str(listval)))
# print(type(listval))

try:
    sum = 0
    for operand in listval:
        sum += int(operand)
        # print(sum)
        # print(type(sum))
    print('Your total is: {}'.format(str(sum)))

except (ValueError, TypeError):
    print('Unable to calculate')


