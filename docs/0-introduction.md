# Part 0: Introduction

As the pressure of university is slowly chipping away at my soul, leaving nothing behind in its path, I've decided to take a short break. In the spirit of not wanting to be productive, I've decided to write a step-by-step guide on how to create a small, fun little interpreter.

In this part, we will focus on creating some scaffolding around our interpreter, so we have a nicer experience later on.



## The language

Before we get started, lets introduce all characters that our interpreter should accept:

```
abcdefghijklmnopqrstuvwxyz
```

You're reading that right, we're working with the alphabet only baby! Simple stuff that you've hopefully learned as a little kid! 

Here's the wildest part: **Each character is a unique operation.** This means that `abc` is the same as `a b c` or `a bc`. Note that the order of the characters does matter.

Great! We now know what we're working with. Simple, good ol' letters. But, they don't have any meaning yet! Don't worry, we will get to that in due time.

Realize that a program like `htxux` is fairly understandable (in the sense that you only have to know what 4 letters do), whilst something like `avdqvdmavvqmiqiiifvdlfbffiiiflblblfbqviiifbfiiifwdfwwiif` is not readable, at all.

What if we wanted to document our ~~madness~~ code? What if we wanted to come back to it later and understand what it does without understanding the code fully?

For this reason, we might want to add **comments** to our language.

```js
let a = 6; // this part is commented out!
let b = () => {return 5}; // lambda

b(); // 5!

// you definitely needed comments to understand this code, don't lie

```

As demonstrated by the JS code snippet above, comments are crucial to understanding complex operations. This is very much noticeable if all your operations are one character long.

Therefore, the goal for this week is to make our interpreter:

- Take in a line or a file,
- Strip all comments,
- Strip all whitespaces/newlines,

And return a single line of code.


## Assignment 1

Write a function that takes in a string.
Return:
- The same string,
- All lowercase,
- Stripped of whitespaces.

Example:

```yaml
Input: "Hello World!"
Output: "helloworld!"

Input: "this is quite a LONG sentence, is it not?"
Output: "thisisquitealongsentence,isitnot?"
```

## Assignment 2

Write a function that takes in a string.
Return:
- The same string,
- All lowercase,
- Stripped of whitespaces,
- Without any comments.


Example:

```yaml
Input: "Hello World! //commented out"
Output: "helloworld!"

Input: "This is quite a long sentence, // Is it not?"
Output: "thisisquitealongsentence,"
```

## Assignment 3

Return:
- The same string,
- All lowercase,
- Stripped of whitespaces,
- Without any comments.

If the final result contains any characters that aren't part of our language (a-z), **throw an error.**

Example:

```yaml
Input: "Apple Pear Banana // Comment on the morality of fruit as a pizza topping. Or do something else with your time"
Output: "applepearbanana"

Input: "this is quite a long sentence, // is it not?"
Output: [Some Error]
```

## Assignment 4

Write a function that takes in a file name.

Return a single string, with each line in the file concatenated.
For each line in the file, apply the function that you got from Assignment 3.

Example file: program.txt
```
avdqvdmavvqmiqiii // init
f
vdlf

bff
iiif
lblblf
bqviiif //blablalabla some random comment
bf
iiif
wdf
wwiif // end
```

```yaml
Input: "program.txt"
Output: "avdqvdmavvqmiqiiifvdlfbffiiiflblblfbqviiifbfiiifwdfwwiif"
```

## Final Assignment

Write a function that takes in two strings as arguments.
If the first item is equal to "run", call the function that you wrote in Assignment 3 using the second argument.

Else if the first item is equal to "file", call the function that you wrote in Assignment 4 using the second argument.

Else, throw an error.

```yaml
Input: file program.txt
Output: "avdqvdmavvqmiqiiifvdlfbffiiiflblblfbqviiifbfiiifwdfwwiif"

Input: run "hqdtmldubx //top secret info"
Output: "hqdtmldubx"

Input: decipher "hqdtmldubx // top secret info"
Output: [Some Error]
```


## Wrapping Up

Well, we haven't really interpreted much, have we? We've only removed stuff from our input.

However, realize that this is an important step for later. Being able to document your steps is a crucial part of learning and developing.

Next part: [Creating memory](1-creating-memory.md)