# Frank, Ian and Glen’s Letters

A Python command-line program that converts ordinary text into large ASCII art using the `pyfiglet` library.

The program can display the entered text using either:

* a randomly selected FIGlet font
* a specific font provided through command-line arguments

This project was completed as part of Harvard's **CS50's Introduction to Programming with Python** course.

## How the program works

The program accepts either zero or two command-line arguments.

### Random font

When the program is executed without additional arguments, it randomly selects one of the available FIGlet fonts.

```bash
python figlet.py
```

The program then prompts the user to enter text:

```text
Input: Hello
```

### Specific font

A specific font can be selected using either the `-f` or `--font` option followed by the font name.

```bash
python figlet.py -f slant
```

or:

```bash
python figlet.py --font slant
```

The entered text is then rendered using the selected font.

## Invalid arguments

The program exits with an error message when:

* an unsupported number of command-line arguments is provided
* the first argument is not `-f` or `--font`
* the specified font does not exist

Example of an invalid command:

```bash
python figlet.py -f nonexistent_font
```

## Requirements

* Python 3
* `pyfiglet`

Install the required module with:

```bash
pip install pyfiglet
```

## Example

```bash
python figlet.py -f slant
```

```text
Input: Python
```

Example output:

```text
    ____        __  __
   / __ \__  __/ /_/ /_  ____  ____
  / /_/ / / / / __/ __ \/ __ \/ __ \
 / ____/ /_/ / /_/ / / / /_/ / / / /
/_/    \__, /\__/_/ /_/\____/_/ /_/
      /____/
```

