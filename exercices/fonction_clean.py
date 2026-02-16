import unittest
from dataclasses import dataclass
from typing import List


MINIMUM_LENGTH_EXCLUSIVE: int = 7


@dataclass(frozen=True)
class FirstName:
    value: str

    def has_more_than_minimum_length(self) -> bool:
        return len(self.value) > MINIMUM_LENGTH_EXCLUSIVE


def count_long_first_names(first_names: List[FirstName]) -> int:
    return sum(
        first_name.has_more_than_minimum_length()
        for first_name in first_names
    )


class TestCountLongFirstNames(unittest.TestCase):

    def test_count_long_first_names(self) -> None:
        first_names: List[FirstName] = [
            FirstName("Guillaume"),
            FirstName("Gilles"),
            FirstName("Juliette"),
            FirstName("Antoine"),
            FirstName("François"),
            FirstName("Cassandre"),
        ]

        result: int = count_long_first_names(first_names)

        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
