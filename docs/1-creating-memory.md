# Part 1: Creating memory

In the [last part](0-introduction.md), we made the foundation for our interpreter. This week, we're going to start actually start interpreting parts of our language. To do this, we're going to start with some simple operators, and work our way up.

## Program flow

First, lets talk about program flow. In a more complex language, 99% of the time, we cannot read our program from top to bottom and that we never have to backtrack. With features like functions, classes, objects, lambdas, or even goto's, its a not of hassle to try and keep track of objects and program state. For now, lets not worry about any of that, and **only worry about a single direction flow: From start to finish, without jumps.**

## Memory

For our language to be able to do anything interesting, its useful to be able to keep track of something. Since implementing variables is quite tricky in a language, lets start with creating a **single memory cell, which we can manipulate and access through operators.** Note that memory is not shared between programs, or consecutive runs of the same program. The memory should always start out uninitialized.

## The first operators

Let's introduce our first official operators: 

| Character | Operation                                |
|-----------|------------------------------------------|
| a         | Add/Overwrite the value in memory by 0.  |
| d         | Decrement the value in memory by 1.      |
| i         | Increment the value in memory by 1.      |
| x         | Print the value in memory as an integer. |

Now, what would a program like `ax` do?

That's right, it should print a 0. 

- `a` makes the interpreter store a 0 in memory.
- `x` prints the value in the memory, which in thise case is a 0.

Below are a few examples:

```yaml
Input: ax
Output: 0

Input: aax
Output: 0

Input: axx
Output: 00

Input: aix
Output: 1

Input: aixdx
Output: 10

Input: aiixxdxdxix
Output: 22101

```

Fantastic! we now have an idea of what our program should be able to do. There are of course more cases to handle, but we can get to that in the assignments.

## Assignment 1

Note: re-use your code from last week in order to read a program. We will extend it such that it is able to handle individual operators.

0. Note that, even though our interpreter doesn't know what to do with any other letter than a, d, i, or x, it should not fail on an unknown letter.
1. Implement the `a` and `x` operators. When given input program `ax`, your interpreter should now print `0`. **Your interpreter should not print the formatted program anymore!**
2. Implement the `d` and `i` operators. When given input program `aiidx`, your interpreter should now print `1`.

Examples:

file: program.txt
```js
a // initialize memory
iiiii // add 5
dd // decrease by 2
xx // print result twice
```

```yaml
Input: run "a"
Ouput: 

Input: run "ax"
Output: 0

Input: file program.txt
Output: 33
```
## Edge cases

As you might have figured out, the specification for each operator is not very well-defined. There are a lot of so-called **edge cases**. These are cases that occur when a given program is valid, but the interpreter has no defined behavior for what it should do. Therefore, we want to eliminate as many edge cases as we can think of. To do so, we need to add extra rules onto our language, and define more behavior.

## Assignment 2
If you haven't already, deal with the following edge cases:

- If no value is in our memory (i.e. no `a` operator has been seen yet), and we try to access its value (through, `i`, `d`, or `x`), throw an error.

- Note that two `a` operators after one another is fine, as the old value should just be replaced by a 0.

- If the current value in memory is a 0, and we try to decrement it (through the `d` operator or anything else), we should throw an error. **The value in our memory should stay between 0 and 1000.**


Author's note: Feel free to contact me (waterboi.#8134 on discord) if you think of another edge case for this week, and I will add it here.


## Removing from memory, exiting

Take a look at the following operators:

| Character | Operation                                |
|-----------|------------------------------------------|
| y         | Remove the value in memory.              |
| z         | Exit the program.                        |

The `y` operator can now be used to **uninitialize** memory. This does not mean setting the memory value to 0, but rather removing the value that is in memory entirely. Note that this of course, requires a value to be present. If there is no value in memory, we should throw an error.

The `z` operator does not have much use _yet_, but it is quite a simple operator to implement. If we encounter a `z` operator, we should exit the program immediately. Any operators after the z are not interpreted.

## Assignment 3

1. Implement the `y` and `z` operators.

```yaml
Input: run "aiix y aix"
Output: 21

Input: run "axiiiiii z diiiiiiiiiiiiiiiidddddx"
Output: 0

Input: run "ayy"
Output: [Some Error]
```

## Wrapping up

In this part, we've briefly talked about program flow, and we've creating a memory cell that we can store a value in. We can access the value and print it, and modify it.

In the next part, we will be expanding our memory in order to hold multiple values.

Next part: `Not yet done`
