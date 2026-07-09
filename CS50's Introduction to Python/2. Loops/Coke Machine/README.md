# Coke Machine

A small Python program that simulates a Coke vending machine.

The machine sells one bottle of Coca-Cola for 50 cents. It accepts coins one at a time and only allows specific coin denominations. After each accepted coin, the program shows how much money is still due. Once the user has inserted at least 50 cents, the program displays how much change is owed.

## Task

Implement a program in `coke.py` that:

* prompts the user to insert one coin at a time
* accepts only coins worth `25`, `10`, or `5` cents
* ignores any integer that is not an accepted coin denomination
* keeps track of the inserted amount
* displays the remaining amount due after each valid coin
* stops once the user has inserted at least 50 cents
* outputs the amount of change owed

## Example

Input:

```text id="n7x4ks"
25
10
25
```

Output:

```text id="b3q9dv"
Amount Due: 50
Amount Due: 25
Amount Due: 15
Change Owed: 10
```

## Accepted Coins

```text id="v6a8mc"
25
10
5
```
