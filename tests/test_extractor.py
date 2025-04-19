import pytest

from phone_number_extractor.extractor import PhoneNumberExtractor
from phone_number_extractor.phone_number import PhoneNumber


@pytest.mark.parametrize(('text', 'expected'), [
    ('jeoijef +7 900 999 9 999 wewfwf', ['+7(900)999-99-99']),
    ('jeoijef +7 900 999 99 99. wfefw',  ['+7(900)999-99-99']),
    ('jeoijef +7 900-999-9-999. wfewfg', ['+7(900)999-99-99']),
    ('jeoijef +7900-999-9-999 - wefwfw', ['+7(900)999-99-99']),
    ('jeoijef +7(900)-999-9-999', ['+7(900)999-99-99']),
    ('jeoijef +7(900) 999-9-999', ['+7(900)999-99-99']),
    ('jeoijef +7 (900) 999-9-999', ['+7(900)999-99-99']),
    ('jeoijef +7 900 999 999 99', ['+7(900)999-99-999']),
    ('fekw[pfj +78008889900', ['+7(800)888-99-00']),
    ('fekw[pfj +7 912-345-67-89', ['+7(912)345-67-89']),
    ('fekw[pfj 8 (495) 123 45 67.', ['+7(495)123-45-67']),
    ('fekw[pfj +7(903) 456  78 90', ['+7(903)456-78-90']),
    ('fekw[pfj +74991234ABCD', []),
    ('fekw[pfj 8 (900) 123 45 67', ['+7(900)123-45-67']),
    ('fekw[pfj 8 (900) 123 45 67', ['+7(900)123-45-67']),
    ('fekw[pfj +7 (999) 888.77.66', ['+7(999)888-77-66']),
])
def test_success(text: str, expected: list[str]):
    """
    Test strict flag = False

    Args:
        text (str): Text to test
        expected (list[str]): Expected result in correct order and format
    """
    extractor = PhoneNumberExtractor()
    result = list(extractor.process_text(text))

    assert isinstance(result, list)
    assert len(result) == len(expected)
    for expected, actual in zip(expected, result):
        assert isinstance(actual, PhoneNumber)
        assert str(actual) == expected, f'Expected: {expected}. Actual: {actual}'


@pytest.mark.parametrize('text', ['fjewoifjwofj + 90'])
def test_no_number(text: str) -> None:
    """
    Test valid behaviour when text doest not contain any phone number

    Args:
        text (str): Text to test
    """
    extractor = PhoneNumberExtractor()

    result = list(extractor.process_text(text))

    assert isinstance(result, list)
    assert len(result) == 0
