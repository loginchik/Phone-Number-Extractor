# 📞 Phone number extractor

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()

[README — ru version](./README_RU.md)

A simple Python tool for extracting and formatting phone numbers from text.

---

## 🚀 Features

- Extracts phone numbers in different patterns (with spaces, dashes, brackets, etc.)
- Currently, extracts only phones starting with +7/8 codes
- Reformats extracted phone numbers to pattern: `+7(900)999-99-99`
- Supports `pytest`

---

## 📦 Installation 

```bash
pip install git+https://github.com/loginchik/Phone-Number-Extractor
```

--- 

## Example usage

```python
from phone_number_extractor.extractor import PhoneNumberExtractor

text = "Позвони мне по номеру +7 (900) 999-99-99"
extractor = PhoneNumberExtractor()
phones = list(extractor.process_text(text))

for phone in phones:
    print(phone)  # +7(900)999-99-99
```
