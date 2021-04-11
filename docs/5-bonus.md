# Part 5: Bonus features

In the [last part](4-conditionals.md), we added the final set of operators to our language. In this (optional) last part, I will be giving some final feature suggestions for your interpreter. Feel free to implement any/none of these, and definitely try to create something cool.


## Insightful error messages

As we know, some combinations of operators will crash our interpreter. For example, having a memory cell going below 0, popping from an empty memory stack, and much more. It would be great to know where in the program the interpreter crashes, and why.

- Include a proper error message explaining why the interpreter stopped.
- Include the location/index of the crash.
- Include a few of the surrounding operators as well, to give more context.


## Step-by-step interpretation

- Implement a mode in your interpreter that allows you to go through a given program step by step, allowing you to halt interpretation completely, take one step, or run until the end. Think of it as a dumbed down `gdb`, and for our own language.

- Include a command to print the remaining program, the current stack, and the next operator to interpret.

- Include the option to interpret newly given operators.

## Program optimization

Implement some simple program optimizations. For example, replace `iiiii` with a single `v`.

- Optimize for less simple cases, such as with multiplication/swapping operators. As long as there is no user input involved, a program will always result in the same output.
  
- Before even interpreting, check if anything will actually be output by the program - If there are no `x` or `f` operators in the program, you don't really need to run it, do you?


## Wrapping up

This is the final part of the series on creating your own interpreter for a language called StupidStackLanguage. You can find more about it [here](https://esolangs.org/wiki/StupidStackLanguage), along with many other esoteric languages. I hope you enjoyed the ride!