# Fuel Gauge

A small Python program that converts a fuel fraction into a percentage.

The program asks the user to enter a fraction in the format `X/Y`, where `X` is a non-negative integer and `Y` is a positive integer. It then calculates how full the fuel tank is and prints the result as a rounded percentage.

If the tank is almost empty, the program outputs `E`. If the tank is almost full, it outputs `F`.

## Task

Implement a program in `fuel.py` that:

* prompts the user for a fraction in the format `X/Y`
* checks that both `X` and `Y` are integers
* checks that `X` is not greater than `Y`
* checks that `Y` is not zero
* converts the fraction into a percentage
* rounds the percentage to the nearest integer
* outputs `E` if the result is 1% or less
* outputs `F` if the result is 99% or more
* prompts the user again if the input is invalid

## Example

Input:

```text
3/4
```

Output:

```text
75%
```

Input:

```text
1/100
```

Output:

```text
E
```

Input:

```text
99/100
```

Output:

```text
F
```
