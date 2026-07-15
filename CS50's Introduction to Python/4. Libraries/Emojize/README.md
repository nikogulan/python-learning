# Emojize

A simple Python command-line program that converts emoji codes and aliases into their corresponding emoji characters using the `emoji` library.

This project was completed as part of Harvard's **CS50's Introduction to Programming with Python** course.

## How the program works

The program prompts the user to enter a string in English.

```text
Input: Python is :thumbs_up:
```

It then converts any recognized emoji codes or aliases into their corresponding emoji.

```text
Output: Python is 👍
```

The program supports standard emoji codes such as:

```text
:thumbs_up:
```

It also supports shorter aliases such as:

```text
:thumbsup:
```

Both codes produce the same emoji:

```text
👍
```

## Usage

Run the program from the terminal:

```bash
python emojize.py
```

Enter a string containing one or more emoji codes when prompted:

```text
Input: I love Python :snake: :red_heart:
```

Example output:

```text
Output: I love Python 🐍 ❤️
```

## Requirements

* Python 3
* `emoji` Python library

Install the required library with:

```bash
pip install emoji
```

## Example

```bash
python emojize.py
```

```text
Input: Great job :thumbsup:
Output: Great job 👍
```

Another example:

```text
Input: Hello, world :globe_showing_Europe-Africa:
Output: Hello, world 🌍
```

