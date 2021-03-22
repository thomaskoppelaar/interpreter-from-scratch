# Part 2: Expanding memory

In the [last part](1-creating-memory.md), we added a single cell of memory to our interpreter. This week, we want to expand and allow for more than one value to be stored at a time.
To do this, we will rework some of our previous operators, add introduce some new ones.

## The Stack

(Note: you can skip this part if you know what a stack is already)

I'll briefly cover what a stack is here, know that there are plenty of other resources out there if you feel like you want a better understanding.

A stack is a(n abstract) data structure (or data type) which is commonly used in programming languages. It's a simple, yet powerful structure that allows us to store multiple values in memory.

The stack has a few special features:

- At any given time, you can only access the top item of the stack.
- Any newly inserted element is placed at the top of the stack.

Think of it as a stack of plates. when you want to store a plate on an existing stack of plates, you would place it on top. When you want to grab a plate, you grab the top one. Otherwise, you're very likely to damage your plates, and we don't want that happening.

In more technical terms, this is called a LIFO (Last In, First Out) structure. The **Last** item to be added to the stack is the **First** one to be removed. We cannot access the items in any other order.

Finally, note that inserting an item onto a stack is called **pushing** an item to the stack. Removing an item is called **popping** an item from the stack.

All of the above is a description of how a stack should behave. Now, it is up to you how you want to implement it! Feel free to also use a built-in stack from your language. E.g. Python has .append() and .pop() for lists, Java has Java.Util.Stack, etc etc.

## New/reworked operators

The old operators have been slightly rephrased, and new operators have been marked in bold:

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


## Assignment 1

0. Take your code from the previous part, and rework the memory. This time, write it such that it functions as a stack with a maximum size of 1 . For most operations, this does not mean any big changes. The `a` operator now has a chance to fail, namely when the stack is full.

1. Change your memory to be able to hold 100 (or any arbitrary large amount) of values.

2. Ensure that all old operators (`a`, `d`, `i`, `x`, `y`, `z`) still work. 


## Assignment 2

0. Take a look at the new operators listed in the above table.

1. Implement the `b` operator. Note that your interpreter should throw an error when there is no item to pop from the stack.

Example: program.txt
```
a iiiidi // init 4-1+1 = 4
a ii // init 2
b x // pop (the 2), print
z // exit
```

`file program.txt` should print `4`.

2. Implement the `v` and `w` operator. Note that when an item is decremented below 0 (e.g. the top value of the stack is a 4 and the next operation is a `w`), you should throw an error.

3. Implement the `q` operator. Note that when there is nothing to duplicate, an error should be thrown.


## Wrapping up

This part was a logical extension to last part: We took our existing memory implementation, and extended it such that we're able to work with more values at the same time.

In the next part, we will extend our interpreter once again such that we can interact with multiple values at the same time. At this point, it's a good idea to clean up / refactor your code in such a way you can easily interpret more operators, seeing as we will be **doubling** the size of our language. 

