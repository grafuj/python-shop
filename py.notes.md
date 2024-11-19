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




`print(my_string[0:3])`
`print(my_string[0:3])`
`print(my_string[0:3])`
`print(my_string[0:3])`



