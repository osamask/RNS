import csv

with open("task1.csv") as f:
  r = csv.reader(f)
  list = []
  for line in r:
    list += line

s, t = list[0], list[1]
a, b = list[2], list[3]
m , n = list[4], list[5]
ana_red = 0
ana_blue = 0
red_dist = []
blue_dist = []
red_dist += list[6:9]
blue_dist += list[9:]

'''
n = int(input("Enter number of elements for red : "))
print("Enter red distances: ")

for i in range(0, n): 
    ele = int(input()) 
    red_dist.append(ele)
    
n = int(input("Enter number of elements for blue : "))
print("Enter blue distances: ")

for i in range(0, n): 
    ele = int(input()) 
    blue_dist.append(ele)

'''
res_red = [x + a for x in red_dist]
  
res_blue = [x + b for x in blue_dist]

#print(res_red)
#print(res_blue)

for x in res_red:
  if s <= x <= t:
    ana_red += 1
    
for x in res_blue:
  if s <= x <= t:
    ana_blue += 1

print(ana_red)
print(ana_blue) 
