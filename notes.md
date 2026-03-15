# Issue #17

## TASK: Split introduction messages into different lines #17

The introduce() function calls the static method say() to print the output to the console.

In introduce(), we create a formatted string by concatenating the given arguments into one variable 'intro':

```Python
intro = f"Hi, my name is {self.name}."
if self.age is not None:
    intro += f" I am {self.age} years old."
```

This produces a formatted string "Hi, my name is Joe. I am 30 years old." which is used to call the say() method with. 

```Python
self.say(intro)
```

The say() method has a param "end", that takes a string and defaults to newline ("\n").
It also has a param "sep", which defaults to " ". 

Note: the implementation does not allow the user to pass any custom arguments to say() via introduce(). 

Now, when we print the output to the console, it's printed in one line:
```Python
    p1 = Person("Joe", 30, "male", 1.70, "Austria", "PM")
    p1.introduce()  # output: Hi, my name is Joe. I am 30 years old. ...
```

This happens because after concatenating all values into "intro", we pass it as one argument to say().
say() then calls the print() function with a 1-tuple, one single argument like:

```Python
print(intro, sep=" ", end="\n")
```

So this leads to the message being printed as one liner, with a newline at the end.

If we want to print each message in one line, we can collect the attribute values into a list, 
then pass it to the say() method along with sep="\n" that tells the print() function in say() to 
override the default separator, which is " ".