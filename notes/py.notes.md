# python

logs:

```py
print("Hi, my name is Sam")
```

run this simple code file using `python3 app.py` to run from the terminal or use VSCode shortcuts `F5`

python is a case-sensitive language that also uses camel case like JavaScript

# Getting input on the terminal

we use the `input()` function. This function takes in a string as the first argument for what it should display. Whatever the user inputs will be what the function returns

# type coercion in python

sometimes we need to change a type. This can be done with functions like `int(number as string like "1988")` returns int or `str(number as int like 1988)` returns string.

`input()` always returns string

# strings

strings have indices in python.
`my_string = "This is my first string"`
and access is `my_string[0]` which returns `T`.

There are also negative indices which proceed from the end of the string.
`my_string[-2]` which returns `n`. The end is `-1` or `g` and one off is `-2` or `n`. When used to look within a string, this will be where the string stops.

we can also access ranges or substrings using `print(my_string[0:6])` which prints `This i`. This is because python is wack and doesn't print the last one. smh fenceposting

another example could be `print(my_string[0:3])` which returns `Thi`

# lacking indexes

substrings can be taken with only a starting or ending value.

`print(my_string[0:])` which returns the entire string since we've started from the beginning
`print(my_string[:])` which returns the entire string since we've started from the beginning

python assumes the start is the first value and the end of string is the end value.

`print(my_string[1:])` which removes the first character: `his is my first string`
`print(my_string[:3])` which returns `Thi` and has the same fenceposting as before

What about getting fancy with negative indices?

`print(my_string[1:-1])` which returns `his is my first strin` as it removes first and last characters

# formatted strings vs. string concatenation

`first_name = "Sam"`
`last_name = "Bick"`

`message = first_name + " [" + last_name + "] " + "knows python"`
this is the frustrating way, JS uses template literals and python has it's own party trick

this `f` stands for format and allows us to use curly braces to handle variables
msg = f"{first} [{last}] is a coder"

# string length

Py's length function is `len(string)` and can be used on obj, array, str etc

`print(len(my_string))` will return `23`. The `g` on the end of string is the 23rd character, no funny fenceposting.

# string methods

Why is length a separate function? Some mix of old programming languages. We're got uppers, we've got lowers, center, etc. these all create new strings, without modifying the original

`print(my_string.upper())` returns `THIS IS MY FIRST STRING`
`print(my_string.title())` returns `This Is My First String`
`print(my_string.lower())` returns `this is my first string`
`print(my_string.find("T"))` returns `0` as that is the index of the uppercase T
`print(my_string.find("X"))` returns `-1` as it is not in the string
`print(my_string.find("string"))` returns `17` as that is where the s of string starts
`print(my_string.replace("string", "python method"))` returns `This is my first python method` as that has string replaced with python method. replace takes two arguments: (old, new)
`print("first" in my_string)` returns `True` as that expression evaluates to boolean using the `in` operator and in this case true

# arithmetic

`print(10 / 3)` returns 3.33333
`print(10 // 3)` returns 3 as it rounds down. returns int
`print(10 % 3)` returns 1 as that is the remainder
`print(10 ** 3)` returns 1000 as that 10^3 or exponent
`print(10 ** 3)` returns 1000 as that 10^3 or exponent

we also have the same `x += 3` which adds the to the current value of x

there are also functions like `x=2.9` and `round(x) = 3` and `abs()` absolute value

There are more math operators that are built in but must be imported.
`import math` which imports the math object that has a zillion methods like math.ceil(2.1) and math.floor(2.9) and both are 2.

# conditionals

```py
if is_hot:
  print("It's a hot day")
  print("Drink plenty of water")
elif is_wet:
  print("It's a wet, hot day")
else:
  print("It's a cold, dry day")
```
