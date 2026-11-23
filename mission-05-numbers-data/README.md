# Mission 05 — Number Systems and Data

## Objective
Understand number systems, perform conversions, and learn about text encoding.

## Work Completed
Documented examples of decimal, binary, octal, and hexadecimal numbers. Created a Python number converter.

## Commands/Tools Used
- `python3 number_converter.py` — runs the converter.

## What I Learned
Decimal uses digits 0–9 and has base 10.
Binary uses 0 and 1 and has base 2.
Octal uses digits 0–7 and has base 8.
Hexadecimal uses 0–9 and A–F and has base 16.

Examples:
- Decimal 10 = Binary 1010
- Decimal 10 = Octal 12
- Decimal 10 = Hexadecimal A

Text encoding represents characters as numbers. ASCII represents a basic set of characters. Unicode supports characters from many languages.

## Difficulties
Understanding why different number systems represent the same value differently.

## How I Resolved Them
Compared the value 10 in four number systems.

## Evidence/Files
- `number_converter.py`

## Commit Details
This mission documentation was included in commit 2c7a113 on the main branch. Additional updates were included in commit 2c3bdfe on update-about and merged into main.

## Manual Number Conversion Examples

### Example 1: Decimal 10 to Binary
10 ÷ 2 = 5 remainder 0
5 ÷ 2 = 2 remainder 1
2 ÷ 2 = 1 remainder 0
1 ÷ 2 = 0 remainder 1

Read the remainders from bottom to top.
Answer: 1010

### Example 2: Decimal 10 to Octal
10 ÷ 8 = 1 remainder 2
1 ÷ 8 = 0 remainder 1

Read the remainders from bottom to top.
Answer: 12

### Example 3: Decimal 10 to Hexadecimal
10 in hexadecimal is A.
Answer: A

### Verification
The Python converter returned the same results:
Binary: 1010
Octal: 12
Hexadecimal: A
