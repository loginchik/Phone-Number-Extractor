import re
from typing import Generator, AnyStr

from .phone_number import PhoneNumber


class PhoneNumberExtractor(object):
    """
    Phone number extractor

    Processes all phone numbers that somehow can be converted to pattern (+)?X(XXX)XXX-XX-XX.
    Can process different body patterns: separated by spaces, by dots, by dashes, etc. -
    or without any separator. Currently, extracts only Russia zone phone numbers: those
    that start with 7 or 8.
    """

    def process_text(self, text: str) -> Generator[PhoneNumber, None, None]:
        """
        Extract phone numbers from text

        Args:
            text (str): Text to process

        Yields:
            PhoneNumber: Extracted phone numbers
        """
        if not isinstance(text, str):
            raise TypeError('text must be a string')
        elif text.strip() == '':
            raise ValueError('text must not be empty')

        for match in self.pattern.finditer(text):
            # Skip empty results
            if match is None:
                continue
            # Compile phone number from extracted parts
            yield PhoneNumber(code=match.group(2), prefix=match.group(4), body=match.group(5).strip('- .'))

    @property
    def pattern(self) -> re.Pattern[AnyStr]:
        """
        Phone number prefix

        Returns:
            re.Pattern: Regex pattern to extract phone numbers from string
        """
        return re.compile(r'\b(\+?\s*([78]))([\s\-(.]*(\d{3})[\s\-).]*)((\d+[\s\-.]*){,10})\b')
