# Vanity Plates

A small Python program that checks whether a vanity license plate is valid.

The program asks the user to enter a license plate and then checks whether it follows the vanity plate rules used in Massachusetts. If the plate meets all requirements, the program outputs `Valid`. Otherwise, it outputs `Invalid`.

## Task

Implement a program in `plates.py` that:

* prompts the user for a vanity plate
* checks that the plate starts with at least two letters
* checks that the plate has at least 2 characters
* checks that the plate has no more than 6 characters
* allows only letters and numbers
* rejects spaces, periods, and punctuation marks
* checks that numbers appear only at the end
* checks that the first number is not `0`
* outputs `Valid` if the plate meets all requirements
* outputs `Invalid` if the plate does not meet all requirements

## Example

Input:

```text id="q3m8za"
CS50
```

Output:

```text id="f7k2pn"
Valid
```

Input:

```text id="x9v4dk"
CS05
```

Output:

```text id="n2b6rt"
Invalid
```

Input:

```text id="h5s8lw"
CS50P
```

Output:

```text id="m9q1ce"
Invalid
```

Input:

```text id="r6t2vb"
PI3.14
```

Output:

```text id="k4n7yp"
Invalid
```
