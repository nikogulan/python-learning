# Camel Case

A small Python program that converts a variable name from camel case to snake case.

The program asks the user to enter a variable name written in camel case. It then converts that name into snake case, which is the recommended naming style for variables in Python.

## Task

Implement a program in `camel.py` that:

* prompts the user for a variable name in camel case
* detects uppercase letters inside the variable name
* adds an underscore before each uppercase letter
* converts all letters to lowercase
* outputs the variable name in snake case

## Example

Input:

```text id="p9k3xq"
preferredFirstName
```

Output:

```text id="t7m2la"
preferred_first_name
```

Input:

```text id="v4n8sd"
firstName
```

Output:

```text id="k6r1za"
first_name
```

Input:

```text id="c5x2mp"
name
```

Output:

```text id="m8q4bn"
name
```
