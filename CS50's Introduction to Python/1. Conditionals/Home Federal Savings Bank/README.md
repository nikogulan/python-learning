# Bank

A small Python program that assigns a bank payout based on a greeting.

The program asks the user to enter a greeting. Depending on how the greeting starts, it outputs a different dollar amount. The input is treated case-insensitively, and any leading whitespace is ignored.

## Task

Implement a program in `bank.py` that:

* prompts the user for a greeting
* ignores leading whitespace in the input
* treats the greeting case-insensitively
* outputs `$0` if the greeting starts with `hello`
* outputs `$20` if the greeting starts with `h`, but not `hello`
* outputs `$100` for any other greeting

## Example

Input:

```text id="p7k3qd"
hello
```

Output:

```text id="m4x9ra"
$0
```

Input:

```text id="z8n2vc"
hey
```

Output:

```text id="b6s1lw"
$20
```

Input:

```text id="q5t8yn"
good morning
```

Output:

```text id="r9d4kp"
$100
```
