# Outdated

A Python program that converts dates written in the common United States format into the ISO 8601 standard format.

The program accepts dates written either numerically or with the month written as a word.

## Accepted date formats

The program accepts dates in the following formats:

```text
MM/DD/YYYY
```

Example:

```text
9/8/1636
```

Or:

```text
Month DD, YYYY
```

Example:

```text
September 8, 1636
```

## Output format

Valid dates are converted to the ISO 8601 format:

```text
YYYY-MM-DD
```

Years, months, and days are formatted with leading zeroes when necessary.

Example:

```text
Date: 9/8/1636
1636-09-08
```

```text
Date: September 8, 1636
1636-09-08
```

## Input validation

The program prompts the user again when the entered date is invalid.

An input is considered invalid when:

* the month number is outside the range from `1` to `12`
* the day is outside the range from `1` to `31`
* the written month is not a valid English month name
* the input does not follow one of the supported formats

The task assumes that every month can have up to 31 days, so the program does not validate the exact number of days in individual months.

## How to run

Make sure Python is installed, then run:

```bash
python outdated.py
```

Enter a date when prompted:

```text
Date:
```

## Example

```text
Date: 13/8/2020
Date: September 32, 2020
Date: September 8, 2020
2020-09-08
```
