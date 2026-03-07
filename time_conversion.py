second = int(input("Give time in seconds for conversion into hour and minute: "))

minute = 0
hour = 0

if second >= 3600:
    hour = second // 3600
    second = second % 3600

if second >= 60:
    minute = second // 60
    second = second % 60

print("Hour =", hour)
print("Minute =", minute)
print("Second =", second)