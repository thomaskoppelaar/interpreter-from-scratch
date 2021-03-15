
Author's note: "participant" is a long word, I'm replacing it with Bob.

# Goal

Create an interpreter for https://esolangs.org/wiki/StupidStackLanguage

Additions: `//` will be used as a single line comment.

Allow people to run their interpreter in (one of) three ways:

- By giving a string of characters (e.g. `ssl run hqqmmx`)
- By giving a file (e.g. `ssl file cube.ssl`)
- Or, by interpreting using a live console (`$: {input of characters here}`)


# CoL specific stuff

- Points per part division
- bonus points
- perhaps a showcase of interpreters?

# Parts

## 0. Introduction, setting up

- Explain the general idea
- Explain approach of the parts


### Assignment
Bob's interpreter can take:
- A line, or a file

And strip away comments, and spaces from it.
End result: a single line of characters.

## 1. Creating a single item stack (Storing a value, iterating through operations)

- Explain memory, explain program flow
- Introduce first operator(s): a,d,i,x,y,z

### Assignment

Bob's interpreter can take a line or a file, and interpret the following commands:

| Character | Operation                                |
|-----------|------------------------------------------|
| a         | Add/Overwrite the value in memory by 0.  |
| d         | Decrement the value in memory by 1.      |
| i         | Increment the value in memory by 1.      |
| x         | Print the value in memory as an integer. |
| y         | Remove the value in memory.              |
| z         | Exit the program.                        |

## 2 Expanding to a stack (pushing, popping)

Bob's interpreter can take a line or a file, and interpret the following commands:

| Character | Operation                                  |
|-----------|--------------------------------------------|
| a         | Pushes 0 to the top of the stack.          |
| **b**         | **Pops the top item from the stack.**          |
| d         | Decrements the top item of the stack by 1. |
| i         | Increments the top item of the stack by 1. |
| **q**         | **Duplicates the top item on the stack.**      |
| **v**         | **Increments the top item on the stack by 5.** |
| **w**         | **Decrements the top item on the stack by 5.** |
| x         | Prints the top item on the stack as an integer.   |
| y         | Deletes the entire stack.                  |
| z         | Exits the program.                         |


## 3. More operations (User input, arithmetic)

Bob's interpreter can take a line or a file, and interpret the following commands:

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

## 4 Final stretch (conditionals)

Bob's interpreter can take a line or a file, and interpret the following commands:

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


## 5. Wrapping things up (Bonus)

Bob's interpreter can take a line or a file, and interpret all characters.

Furthermore, it can be called as follows: `ssl {program} {list of inputs}`


- Creating a brainfuck to SSL interpreter: Create a brainfuck program, have the interpreter translate it to SSL.

- SQL? (Stupid Queue Language)

- Duplicate number checking program (take in N numbers (+ N as input) and print 0 if there is a duplicate, 1 if there isnt)





