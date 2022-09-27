import abc
import unittest

from ..src.intelligentParser import IntelligentParser
from ..src.intelligentParserCreator import IntelligentParserCreator


class AbstractTest(unittest.TestCase, abc.ABC):

    parser: IntelligentParser = None
    parserCreator: IntelligentParserCreator = None
    half_sep_length = 40
    currentResult = None

    @classmethod
    def print_sep_with_text(cls, text: str, sep: str = '*') -> None:
        with_sep_lines = sep * cls.half_sep_length + f' {text} ' + sep * cls.half_sep_length
        over_length = len(with_sep_lines) - cls.half_sep_length*2
        to_print = with_sep_lines[over_length//2 : -over_length//2]
        print(to_print)

    @classmethod
    def setUpClass(cls) -> None:
        cls.print_sep_with_text(f'Starting {cls._get_test_name()} tests!')

    def setUp(self) -> None:
        super().setUp()
        print('- ', self.get_method_name(), end=' ... ')

    def tearDown(self) -> None:
        super().tearDown()
        if self.currentResult is not None:
            errors = self.currentResult.errors
            failures = self.currentResult.failures
            ok = not (errors or failures)
            print('ok' if ok else 'ERROR' if errors else 'FAIL')
        else:
            print()

    def run(self, result: unittest.result.TestResult | None = ...) -> unittest.result.TestResult | None:
        self.currentResult = result
        unittest.TestCase.run(self, result)

    @classmethod
    @abc.abstractmethod
    def _get_test_name(cls) -> str:
        return 'unnamed'

    def get_method_name(self) -> str:
        return self.id().split('.')[-1]
