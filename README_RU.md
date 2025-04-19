# 📞 Phone number extractor

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()

Простой Python-инструмент для извлечения и форматирования телефонных номеров из текста.  

---

## 🚀 Возможности 

- Извлекает номера телефонов в разных форматах (с пробелами, дефисами, скобками и т.п.)
- В текущей версии извлекает номера только в зоне +7/8
- Преобразует в формат: `+7(900)999-99-99`
- Поддержка `pytest`

---

## 📦 Установка

```bash
pip install git+https://github.com/loginchik/Phone-Number-Extractor
```

---

## Пример использования

```python
from phone_number_extractor.extractor import PhoneNumberExtractor

text = "Позвони мне по номеру +7 (900) 999-99-99"
extractor = PhoneNumberExtractor()
phones = list(extractor.process_text(text))

for phone in phones:
    print(phone)  # +7(900)999-99-99
```
