import pytest

from phone_number_extractor.phone_number import PhoneNumber


@pytest.mark.parametrize(['obj', 'expected_string'], [
    (PhoneNumber(prefix='123', body='234 23 23', code='7'), '+7(123)234-23-23'),
    (PhoneNumber(prefix='123', body='234-23-23', code='7'), '+7(123)234-23-23'),
    (PhoneNumber(prefix='123', body='2342323', code='8'), '+7(123)234-23-23'),
])
def test_str(obj: PhoneNumber, expected_string: str) -> None:
    assert str(obj) == expected_string