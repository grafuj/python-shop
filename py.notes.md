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
`my_string[-2]` which returns `n`. The end is `-1` or `g` and one off is `-2` or `n`.

we can also access ranges or substrings using `print(my_string[0:6])` which prints `This i`. This is because python is wack and doesn't print the last one. smh fenceposting