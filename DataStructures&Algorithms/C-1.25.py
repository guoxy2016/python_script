"""

"""

from string import ascii_letters, digits, whitespace

match = ascii_letters + digits + whitespace

s = r"Let's try, Mike"
r = ''
for i in s:
    if i in match:
        r += i

print(r)