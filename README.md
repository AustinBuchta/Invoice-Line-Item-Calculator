# CLI Invoice Line Item Calculator

A Python command-line financial tool that calculates individual invoice line items and tracks running totals across user sessions. Integrates custom type casting, value bounds checking, explicit exception raising, and string formatting for accurate financial display.

## Technical Highlights

* **Input Type Enforcement & Bounds Checking:** Uses procedural helper functions (`get_price`, `get_quantity`) to parse `float` and `int` values while explicitly raising `ValueError` exceptions for negative inputs ($\text{value} < 0$).
* **Explicit Exception Control Flow:** Demonstrates custom exception handling using manual `raise ValueError` statements to redirect invalid inputs into retry prompts.
* **Running Total State Accumulation:** Tracks session-level aggregate totals (`total += line_total`) alongside individual line-item calculations (`price * quantity`).
* **Formatted Financial Output:** Formats monetary output to two decimal places using legacy string formatting (`"Price: ${:.2f}".format(price)`) alongside round operations.

## Technical Requirements

* **Python Version:** Built using pure standard Python 3.x (requires zero external `pip` dependencies).

## Usage

```bash
python main.py
