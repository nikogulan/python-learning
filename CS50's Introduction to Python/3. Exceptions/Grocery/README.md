# Grocery List

A small Python program that builds a grocery list from user input.

The program asks the user to enter grocery items one by one. Input continues until the user sends an EOF signal, usually with `Ctrl + D`. After that, the program prints the final grocery list in alphabetical order, showing how many times each item was entered.

## Task

Implement a program in `grocery.py` that:

* accepts grocery items from the user, one item per line
* treats input case-insensitively
* counts how many times each item appears
* sorts the items alphabetically
* prints each item in uppercase
* prefixes each item with its quantity

## Example

Input:

```text id="y83qbr"
apple
banana
apple
milk
banana
apple
```

After pressing `Ctrl + D`, the program outputs:

```text id="r9m7p0"
3 APPLE
2 BANANA
1 MILK
```
