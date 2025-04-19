from dataclasses import dataclass
import re


@dataclass(frozen=True)
class PhoneNumber:
    """
    Extracted phone number wrapper to format it according to desired pattern:
    +7(XXX)-XXX-XX-XX

    - `code` is country code, defaults to +7
    - `prefix` is region code, typically something like (900) or (4XX)
    - `body` is the main part of a phone number, typically contains of 7 digits

    String representation of object formats code (adds +) and body (converts into XXX-XX-XX).
    """
    prefix: str
    body: str
    code: str = '7'

    def __str__(self) -> str:
        """
        String representation of PhoneNumber object

        Returns:
            str: String representation of the phone number
        """
        return f'{self.format_code()}({self.prefix}){self.format_body(self.body)}'

    def format_code(self) -> str:
        """
        Adds + to all codes, besides 8.
        If initial code is 8, then returns +7

        Returns:
            str: New code
        """
        if self.code == '8':
            return f'+7'

        code = self.code if isinstance(self.code, str) else str(self.code)
        return '+' + re.sub(r'\D', '', code)

    @staticmethod
    def format_body(body: str) -> str:
        """
        Formats body of phone number

        Args:
            body (str): Body of phone number

        Returns:
            str: Body in format XXX-XX-XX
        """
        cleared_body = re.sub(r'\W', '', body)
        groups = re.match(r'(\w{3})(\w{2})(\w+)\b', cleared_body).groups()
        return '-'.join(groups)
