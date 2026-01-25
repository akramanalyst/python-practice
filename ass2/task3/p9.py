#importing tempconv file

import tempconv
c = int(input(" enter celsius value : "))
f = int(input(" enter fahrenheit value : "))

print(tempconv.ctof(c))

print(tempconv.ftoc(f))