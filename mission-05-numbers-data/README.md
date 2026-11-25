# Mission 05 — Number Systems and Data

## Objective
Understand different number systems, perform conversions, and learn how computers represent text.

## Work Completed
Studied decimal, binary, octal, and hexadecimal number systems. Practised manual conversions and verified the results using Python. Also explored character encoding.

## Commands/Tools Used

| Command | Purpose |
|---|---|
| `python3 number_converter.py` | Runs the number conversion program |

## What I Learned

### 1. Number Systems

| Number System | Base | Digits Used |
|---|---:|---|
| Decimal | 10 | 0–9 |
| Binary | 2 | 0–1 |
| Octal | 8 | 0–7 |
| Hexadecimal | 16 | 0–9 and A–F |

### 2. Manual Conversion

I converted decimal number 10 into other number systems.

- Binary: 1010
- Octal: 12
- Hexadecimal: A

**Binary conversion using repeated division:**

10 ÷ 2 = 5 remainder 0  
5 ÷ 2 = 2 remainder 1  
2 ÷ 2 = 1 remainder 0  
1 ÷ 2 = 0 remainder 1  

Reading the remainders from bottom to top gives `1010`.

### 3. Python Verification

I used Python to verify the conversions:

```python
number = 10

print(bin(number))
print(oct(number))
print(hex(number))
