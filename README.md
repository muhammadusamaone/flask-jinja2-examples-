# Flask Jinja2 Examples

This repository contains beginner-friendly Flask examples demonstrating how to use Jinja2 templates.

## Examples Included

### 1. Dictionary Example (`dictionary.py`)

* Pass a Python dictionary to an HTML template.
* Display object properties using Jinja2 variables.

### 2. List Example (`list.py`)

* Pass a Python list to an HTML template.
* Display multiple items using a Jinja2 `for` loop.

## Project Structure

```text
Jinja2 for Loop/
│
├── templates/
│   ├── index1.html
│   └── index2.html
│
├── dictionary.py
└── list.py
```

## Technologies Used

* Python
* Flask
* Jinja2
* HTML5

## How to Run

Install Flask:

```bash
pip install flask
```

Run the dictionary example:

```bash
python dictionary.py
```

Run the list example:

```bash
python list.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Learning Outcomes

* Flask routing
* Template rendering with `render_template()`
* Passing variables from Python to HTML
* Working with dictionaries in Jinja2
* Working with lists in Jinja2
* Using `for` loops in Jinja2 templates
