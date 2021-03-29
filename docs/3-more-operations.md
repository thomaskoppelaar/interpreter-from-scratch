# Part 3: More operations and user input


In the [last part](2-expanding-memory.md), we expanded our memory to make it a stack. In this part, we want to utilise more of the stack's attributes by adding more operators into our language.
Finally, we will also add the ability for a user to input text and/or numbers.


## The new operators


| Character | Operation                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------|
| a         | Pushes 0 to the top of the stack.                                                             |
| b         | Pops the top item from the stack.                                                             |
| **c**         | **Subtracts the 2nd item on the stack from the top item and pushes the result to the stack.**     |
| d         | Decrements the top item of the stack by 1.                                                    |
| **e**         | **Pushes the top item mod the 2nd item onto the stack.**                                          |
| **f**         | **Prints the top item on the stack as an ASCII character.**                                       |
| **g**         | **Adds the first 2 stack items together and pushes the result to the stack.**                     |
| **h**         | **Gets input from the user as a number and pushes to the stack.**                                 |
| i         | Increments the top item of the stack by 1.                                                    |
| **j**         | **Gets input from the user as a character and pushes that characters ASCII code onto the stack.** |
| **l**         | **Swaps the 1st and 2nd items on the stack.**                                                     |
| **m**         | **Multiplies the first 2 stack items together and pushes the result onto the stack.**             |
| **p**         | **Divides the top item on the stack by the 2nd item and pushes the result onto the stack.**       |
| q         | Duplicates the top item on the stack.                                                         |
| **r**         | **Pushes the total length of the stack onto the stack.**                                          |
| v         | Increments the top item on the stack by 5.                                                    |
| w         | Decrements the top item on the stack by 5.                                                    |
| x         | Prints the top item on the stack as an integer.                                                      |
| y         | Deletes the entire stack.                                                                     |
| z         | Exits the program.                                                                            |


## Assignment 1: Arithmetic operators

0. Take a look at the `c`,`e`,`g`,`m`, and `p`. operators.
1. Implement them.
For example:

program.txt
```js
aviii // init cell, set to 8
avvvi // init cell, set to 16
g // 8 + 16 = 24
// the current stack (from top to bottom): 24,16,8
xbxbx // 24168
z // optional exit
```
`file program.txt` should print `24168`.

## Assignment 2: Swapping, total length

0. Take a look at the `l` and `r` operators.
1. Implement them.

For example: `run arrr xb xb xb xb` should print `3210`, and `aaiiil` should print `0`.

Note that you should use integer division when dividing (i.e. you don't get a decimal number as a result).

2. Think of what could occur when:
- Trying to take two numbers off the stack when there are less than 2 on the stack
- Dividing by 0

and try to combat these cases.


## Assignment 3: User input

(Note: here's an [ASCII Cheatsheet](http://www.asciitable.com/) that you might find useful.)

0. Take a look at the `f`, `h`, and `j` operators.
1. Implement them.

For example: `jf` should print the character that was given as input.

Note that for `h`, only the characters `0` through `9` are valid input.


## Assignment 4: Hello World

Write a "Hello World!" Program! You might find the ASCII cheatsheet listed earlier useful.

## Wrapping up

This part, we made good use of our stack, and added the ability for a user to input their text. We've fleshed out our interpreter and our language by being able to do more than basic addition.

The next part will already be the final required part of our interpreter, adding conditional operators and the ability to jump through our program.

Next part: `Not yet done`
