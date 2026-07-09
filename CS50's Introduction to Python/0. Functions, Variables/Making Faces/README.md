# Faces

A small Python program that converts text emoticons into emoji.

The program asks the user to enter a string of text. It then replaces any happy or sad emoticons with matching emoji, while leaving the rest of the text unchanged.

## Task

Implement a program in `faces.py` that:

* defines a function called `convert`
* accepts a string as input
* replaces `:)` with `🙂`
* replaces `:(` with `🙁`
* returns the converted string
* defines a function called `main`
* prompts the user for input
* calls `convert` on the user’s input
* prints the converted result
* calls `main` at the bottom of the file

## Function Requirement

The `convert` function should take text as input and return the same text with supported emoticons replaced by emoji.

```text id="h8v3qm"
:)
```

should become:

```text id="r5x9la"
🙂
```

```text id="k2m7zn"
:(
```

should become:

```text id="p9d4cw"
🙁
```

## Example

Input:

```text id="q6n8tb"
Hello :)
```

Output:

```text id="v4c2ys"
Hello 🙂
```

Input:

```text id="m7x3ra"
Goodbye :(
```

Output:

```text id="z9k5lp"
Goodbye 🙁
```

Input:

```text id="b2w8qn"
Hello :) Goodbye :(
```

Output:

```text id="s3v6md"
Hello 🙂 Goodbye 🙁
```

