import math
ab=float(input())
bc=float(input())
h=math.sqrt(ab**2+bc**2)

c=math.atan(ab/bc)

mc=h/2
mb=math.sqrt(bc**2+mc**2-(2*bc*mc*math.cos(c)))
mbc=math.asin(mc*(math.sin(c)/mb))
output=round(math.degrees(mbc))

output=str(output)
print(output+u"\N{DEGREE SIGN}")
