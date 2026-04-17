# program to check age using exception

age = int(input("Enter your age: "))

try:
    if age:
         Exception("Not eligible (Age must be 18+)")
    else:
        print("Eligible")
  

except ValueError as e:

      print(e)