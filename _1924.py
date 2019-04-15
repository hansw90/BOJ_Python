x,y= map(int,input().split())
a = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
date = 0 
for i in range(x-1) :
    date += a[i]

print(day[(date+y)%7])
