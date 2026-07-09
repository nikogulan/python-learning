# Meal Time

A small Python program that tells the user whether it is time for breakfast, lunch, or dinner.

The program asks the user to enter a time and checks whether that time falls within one of the defined meal ranges. If the time does not match any meal range, the program does not output anything.

## Task

Implement a program in `meal.py` that:

* prompts the user for a time
* accepts time in 24-hour format as `#:##` or `##:##`
* converts the time into hours as a floating-point number
* outputs `breakfast time` if the time is between `7:00` and `8:00`
* outputs `lunch time` if the time is between `12:00` and `13:00`
* outputs `dinner time` if the time is between `18:00` and `19:00`
* includes the start and end time of each meal range
* outputs nothing if it is not time for a meal

## Function Requirement

The program should include a `convert` function that:

* accepts a time string
* converts hours and minutes into a float
* returns the corresponding number of hours

For example:

```text id="t6q4mn"
7:30
```

should be converted to:

```text id="r9x2lp"
7.5
```

## Optional Challenge

The program can also support 12-hour time formats, including:

* `#:## a.m.`
* `##:## a.m.`
* `#:## p.m.`
* `##:## p.m.`

Examples of valid 12-hour inputs:

```text id="k8v3sa"
7:30 a.m.
```

```text id="m4d9yb"
12:30 p.m.
```

```text id="x2h7qc"
6:45 p.m.
```

## Example

Input:

```text id="n5w8ze"
7:00
```

Output:

```text id="p3c9lm"
breakfast time
```

Input:

```text id="v6k2ra"
12:30
```

Output:

```text id="s8q4xn"
lunch time
```

Input:

```text id="b7t5yd"
18:45
```

Output:

```text id="j2m9cw"
dinner time
```

Input:

```text id="z4r8vp"
10:15
```

No output.
