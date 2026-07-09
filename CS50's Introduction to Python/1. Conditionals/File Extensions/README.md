# File Extensions

A small Python program that determines a file’s media type based on its extension.

The program asks the user to enter a file name. It then checks the file extension and outputs the corresponding media type. The extension is treated case-insensitively, so `.GIF`, `.gif`, and similar variations are handled the same way.

If the file has an unknown extension or no extension at all, the program outputs the default media type: `application/octet-stream`.

## Task

Implement a program in `extensions.py` that:

* prompts the user for a file name
* checks the file extension case-insensitively
* outputs `image/gif` for `.gif`
* outputs `image/jpeg` for `.jpg` and `.jpeg`
* outputs `image/png` for `.png`
* outputs `application/pdf` for `.pdf`
* outputs `text/plain` for `.txt`
* outputs `application/zip` for `.zip`
* outputs `application/octet-stream` for unknown or missing extensions

## Example

Input:

```text id="k8m2vx"
cat.gif
```

Output:

```text id="q6n9pa"
image/gif
```

Input:

```text id="t4z7jw"
photo.JPG
```

Output:

```text id="r5c1dk"
image/jpeg
```

Input:

```text id="a9x3lp"
document.pdf
```

Output:

```text id="v2h8mn"
application/pdf
```

Input:

```text id="n7q4sy"
archive
```

Output:

```text id="p1w6zb"
application/octet-stream
```
