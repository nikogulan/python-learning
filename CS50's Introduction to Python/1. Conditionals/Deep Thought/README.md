# Deep Thought

A small Python program that checks the answer to the Great Question of Life, the Universe and Everything.

The program asks the user to enter an answer. If the user enters `42`, `forty-two`, or `forty two`, the program outputs `Yes`. Any other input results in `No`.

## Task

Implement a program in `deep.py` that:

* prompts the user for an answer
* accepts `42` as a valid answer
* accepts `forty-two` as a valid answer
* accepts `forty two` as a valid answer
* treats text input case-insensitively
* outputs `Yes` if the answer is correct
* outputs `No` if the answer is incorrect

## Example

Input:

```text id="p4x8lm"
42
```

Output:

```text id="v9n2qa"
Yes
```

Input:

```text id="k7d3rs"
Forty Two
```

Output:

```text id="m5c8tz"
Yes
```

Input:

```text id="a2q9vb"
forty-two
```

Output:

```text id="h8x4np"
Yes
```

Input:

```text id="r6y1kd"
41
```

Output:

```text id="j3w7fs"
No
```
