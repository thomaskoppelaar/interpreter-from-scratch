# Part 4: Conditionals and jumps


In the [last part](3-more-operations.md), we added a new set of operaters that were able to utilize the stack effectively.
In this part, we want to add the final few operators into our language that allow us to jump within the program.

## The new operators


| Character | Operation                                                                                                          |
|-----------|--------------------------------------------------------------------------------------------------------------------|
| a         | Pushes 0 to the top of the stack.                                                                                  |
| b         | Pops the top item from the stack.                                                                                  |
| c         | Subtracts the 2nd item on the stack from the top item and pushes the result to the stack.                          |
| d         | Decrements the top item of the stack by 1.                                                                         |
| e         | Pushes the top item mod the 2nd item onto the stack.                                                               |
| f         | Prints the top item on the stack as an ASCII character.                                                            |
| g         | Adds the first 2 stack items together and pushes the result to the stack.                                          |
| h         | Gets input from the user as a number and pushes to the stack.                                                      |
| i         | Increments the top item of the stack by 1.                                                                         |
| j         | Gets input from the user as a character and pushes that characters ASCII code onto the stack.                      |
| **k**         | **Skips the next command if the top item on the stack is 0.**                                                          |
| l         | Swaps the 1st and 2nd items on the stack.                                                                          |
| m         | Multiplies the first 2 stack items together and pushes the result onto the stack.                                  |
| **o**         | **Pops the (top item on the stack)th item on the stack.**                                                            |
| p         | Divides the top item on the stack by the 2nd item and pushes the result onto the stack.                            |
| q         | Duplicates the top item on the stack.                                                                              |
| r         | Pushes the total length of the stack onto the stack.                                                               |
| **s**         | **Swaps the 1st and (top item on the stack)th items on the stack.**                                                  |
| **t**         | **If the top item on the stack is 0, jumps to the corresponding 'u' in the program, otherwise does nothing.**          |
| **u**         | **If the top item on the stack is not 0, jumps back to the corresponding 't' in the program, otherwise does nothing.** |
| v         | Increments the top item on the stack by 5.                                                                         |
| w         | Decrements the top item on the stack by 5.                                                                         |
| x         | Prints the top item on the stack as an integer.                                                                           |
| y         | Deletes the entire stack.                                                                                          |
| z         | Exits the program.                                                                                                 |

## Assignment 1: Nth item on the stack.

0. take a look at the `o` and the `s` operator.
1. Implement them. 

A couple of notes:
- Your stack should be 0-indexed. This means that the top item has index 0, the one below that 1, etc etc.
- If the nth item of the stack doesn't exist, throw an error.

For example:

program.txt:
```js
av // init 5
aii // init 2
ai // init 1
aaa // init 3 * 0
// the stack looks as follows: 0,0,0,1,2,5
vd s // add 4, swap top item with 5th item on stack
// the stack looks as follows: 2,0,0,1,4,5
xb xb xb xb xb xb // print everything
z
```
`file program.txt` should print `200145`.


## Assignment 2: Conditionals

0. Take a look at the `k`, `t`, and `u` operators.
1. Implement them.

A couple of notes:
- If you encounter a `t` whilst the top item on the stack is 0 and there is no `u`, you should exit the program.
- If you encounter a `u` whilst the top item on the stack is not 0 and there is no `t`, you should go back to the beginning.
- If there are no items to read on the stack whilst you encounter a `t`, `u`, or `k`: throw an error.
- You do not have to worry about infinite looping programs (e.g. `aiu`).
- "Corresponding" t or u means that loops can be nested. For example: `t...t...u...u` means that the inner `t` should jump to the inner `u`, and the outer `t` to the outer `u` (should the conditions hold).

For example:
factorial.txt
```js

h // take number input (x)
q // duplicate
d // decrement (y = x - 1) -- stack: y,x
t // begin loop if top item != 0
	m // push result = y * x
	l // swap result and y
	d // decrement y -- stack: y,result,x
u // end loop if top item == 0 -- stack: 0, result, x
b // pop top item -- stack: result, x
x // print
```
`file factorial.txt` should print `x!`, or the factorial of the given input number.
(Note that the program doesn't work with input 0. You could try and do that as a bonus assignment).

## Wrapping up

It's time to congratulate yourself on what you've done: You've created a fully fledged interpreter for hopefully the weirdest language you'll ever come across!
I hope you found this to be a neat little task and walk through making an interpeter. 
Although we did not cover much formally, I hope that you still learned something. Seeing as we have now implemented all the operators, there is not much to add to our interpreter other than some extra features, which will be the topic of the final part.

Next part: `Not yet done`



