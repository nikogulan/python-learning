# Nutrition Facts

A small Python program that shows calorie information for common raw fruits.

The program asks the user to enter the name of a fruit. If the fruit is listed in the nutrition data, the program outputs the number of calories in one portion of that fruit. The input is treated case-insensitively, so the result is the same whether the user types the fruit in lowercase, uppercase, or mixed case.

If the input is not a valid fruit from the list, the program ignores it.

## Task

Implement a program in `nutrition.py` that:

* prompts the user to enter a fruit
* treats input case-insensitively
* checks whether the fruit exists in the fruit nutrition data
* outputs the number of calories for one portion of that fruit
* ignores any input that is not a fruit from the list

## Example

Input:

```text id="b8q1mz"
apple
```

Output:

```text id="m5r7tn"
Calories: 130
```

Input:

```text id="k2x9vp"
strawberries
```

Output:

```text id="q4n6sd"
Calories: 50
```

Input:

```text id="z9h3la"
pizza
```

No output.
