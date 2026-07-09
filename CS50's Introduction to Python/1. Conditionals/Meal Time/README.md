# Meal Time

A small Python program that tells the user whether it is time for breakfast, lunch, or dinner.

The program asks the user to enter a time in 24-hour format. It then converts that time into a floating-point number and checks whether it falls within one of the defined meal time ranges. If the time does not match any meal range, the program does not output anything.

## Task

Implement a program in `meal.py` that:

* prompts the user for a time
* expects time in 24-hour format as `#:##` or `##:##`
* converts the time into hours as a floating-point number
* outputs `breakfast time` if the time is between `7:00` and `8:00`
* outputs `lunch time` if the time is between `12:00` and `13:00`
* outputs `dinner time` if the time is between `18:00` and `19:00`
* includes the start and end time of each meal range
* outputs nothing if it is not time for a meal

## Function Requirement

The program should include a `convert` function that:

* accepts a time string in 24-hour format
* converts hours and minutes into a float
* returns the corresponding number of hours

For example:

```text id="v8k2qm"
7:30
```

should be converted to:

```text id="n5x9ra"
7.5
```

## Example

Input:

```text id="m4q8zt"
7:00
```

Output:

```text id="p9c3xv"
breakfast time
```

Input:

```text id="k6r2ln"
12:30
```

Output:

```text id="d8s4wa"
lunch time
```

Input:

```text id="q7v5mc"
18:45
```

Output:

```text id="x2n9yb"
dinner time
```

Input:

```text id="z3h6lp"
10:15
```

No output.
