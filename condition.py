# CONDITIONAL STATEMENTS PRACTICE
# QUESTIONS + ANSWERS

# Q1. Check Voting Eligibility
age = int(input())
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# Q2. Positive, Negative, or Zero
num = int(input())
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Q3. Check Even or Odd
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q4. Find the Greater Number
a = int(input())
b = int(input())
if a > b:
    print("a is greater")
elif b > a:
    print("b is greater")
else:
    print("Equal")


# Q5. Divisibility by 5 and 11
n = int(input())
if n % 5 == 0 and n % 11 == 0:
    print("Divisible")
else:
    print("Not Divisible")


# Q6. Check Leap Year
year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# Q7. Alphabet Case Identifier
char = input()
if 'A' <= char <= 'Z':
    print("Uppercase")
elif 'a' <= char <= 'z':
    print("Lowercase")


# Q8. Valid Triangle Check
a = int(input())
b = int(input())
c = int(input())
if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


# Q9. Check Pass or Fail
marks = int(input())
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Q10. Find the Largest of Three Numbers
x = int(input())
y = int(input())
z = int(input())
if x >= y and x >= z:
    print(x)
elif y >= x and y >= z:
    print(y)
else:
    print(z)


# Q11. Check Temperature Category
temp = int(input())
if temp > 35:
    print("Hot")
elif temp >= 20:
    print("Normal")
else:
    print("Cold")


# Q12. Calculate Discount
amount = float(input())
if amount >= 1000:
    discount = amount * 0.10
    final_amount = amount - discount
else:
    final_amount = amount
print(final_amount)


# Q13. Grade Calculator
marks = int(input())
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")


# Q14. Electricity Bill Calculator
units = int(input())
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
print(bill)