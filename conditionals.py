is_hot = False
is_wet = False

# python uses colons and indentation making space matter a lot more than in javascript. Since there are no brackets, these lines of code cannot be collapsed into one line.
if is_hot:
  print("It's a hot day")
  print("Drink plenty of water")
elif is_wet:
  print("It's a wet, hot day")
else:
  print("It's a cold day")
  print("Wear warm clothes")



price = 1000000
good_credit = True
down_payment = 0

if good_credit:
  down_payment = 0.1* price
else:
  down_payment = 0.2* price

print(f"Down payment: ${down_payment}")

has_high_income = True
has_good_credt = True

if has_high_income and has_good_credt:
  print("Eligible for loan, high income and credit")

if has_high_income or has_good_credt:
  print("got 1/2. Eligible for loan, high income or credit")
  
temp = 30

if temp > 30:
  print("It's a hot day")
elif temp > 20 and temp <= 30:
  print("It's a warm day")
else:
  print("It's a cold day")