# Felipe's Taqueria

A small Python program that simulates placing an order from a restaurant menu.

The program asks the user to enter menu items one by one. After each valid item, it updates and displays the total cost of the order. Input continues until the user sends an EOF signal, usually with `Ctrl + D`.

The program treats user input case-insensitively and ignores anything that is not on the menu.

## Task

Implement a program in `taqueria.py` that:

* prompts the user for menu items, one item per line
* treats input case-insensitively
* matches user input to titlecased menu items
* keeps track of the total order cost
* displays the running total after each valid item
* formats the total with a dollar sign
* shows the total with exactly two decimal places
* ignores any input that is not on the menu
* stops when the user sends EOF

## Menu

```python id="z7xk2m"
{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
```

## Example

Input:

```text id="q8m4dn"
burrito
taco
BOWL
```

Output after each valid item:

```text id="n6p91v"
$7.50
$10.50
$19.00
```
