# Tip Calculator

A small Python program that calculates how much tip to leave after a meal.

The program asks the user for the meal cost and the tip percentage. It then converts both inputs into numbers, calculates the tip amount, and prints the result formatted as dollars with two decimal places.

## Task

Implement a program in `tip.py` that completes the provided tip calculator by defining two functions:

* `dollars_to_float`
* `percent_to_float`

The program should:

* prompt the user for the meal cost
* expect the meal cost in the format `$##.##`
* remove the leading dollar sign
* convert the meal cost to a float
* prompt the user for the tip percentage
* expect the tip percentage in the format `##%`
* remove the trailing percent sign
* convert the percentage to a decimal float
* calculate the tip amount
* output the tip formatted to two decimal places

## Function Requirement

The `dollars_to_float` function should convert a dollar string into a float.

```text id="q7m4xa"
$50.00
```

should become:

```text id="n9v2kp"
50.0
```

The `percent_to_float` function should convert a percentage string into a decimal float.

```text id="r5k8sd"
15%
```

should become:

```text id="m3x7lp"
0.15
```

## Example

Input:

```text id="z8p2qc"
$50.00
15%
```

Output:

```text id="v6n9ta"
Leave $7.50
```

Input:

```text id="k4w8rb"
$100.00
20%
```

Output:

```text id="x2d5mn"
Leave $20.00
```
