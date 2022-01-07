import unittest
from operations import validate, Color


class TestsValidate(unittest.TestCase):
    def setUp(self) -> None:
        zero1 = {
            "name": "zero1",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.GREEN, Color.RED, Color.YELLOW, Color.MAGENTA]
            },
            "output": (0, 4)
        }
        zero2 = {
            "name": "zero2",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE]
            },
            "output": (0, 0)
        }
        zero3 = {
            "name": "zero3",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.MAGENTA, Color.MAGENTA, Color.YELLOW, Color.MAGENTA]
            },
            "output": (0, 2)
        }
        zero4 = {
            "name": "zero4",
            "input": {
                "sc": [Color.RED, Color.RED, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.MAGENTA, Color.MAGENTA, Color.YELLOW, Color.MAGENTA]
            },
            "output": (0, 2)
        }
        zero5 = {
            "name": "zero5",
            "input": {
                "sc": [Color.RED, Color.RED, Color.RED, Color.RED],
                "user_colors": [Color.MAGENTA, Color.MAGENTA, Color.YELLOW, Color.MAGENTA]
            },
            "output": (0, 0)
        }
        zero6 = {
            "name": "zero6",
            "input": {
                "sc": [Color.MAGENTA, Color.RED, Color.BLUE, Color.RED],
                "user_colors": [Color.GREEN, Color.GREEN, Color.MAGENTA, Color.BLUE]
            },
            "output": (0, 2)
        }
        zero7 = {
            "name": "zero7",
            "input": {
                "sc": [Color.RED, Color.BLUE, Color.YELLOW, Color.YELLOW],
                "user_colors": [Color.BLUE, Color.RED, Color.RED, Color.RED]
            },
            "output": (0, 2)
        }

        zero8 = {
            "name": "zero8",
            "input": {
                "sc": [Color.GREEN, Color.GREEN, Color.BLUE, Color.GREEN],
                "user_colors": [Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE]
            },
            "output": (0, 2)
        }
        zero9 = {
            "name": "zero9",
            "input": {
                "sc": [Color.YELLOW, Color.RED, Color.YELLOW, Color.BLUE],
                "user_colors": [Color.BLUE, Color.YELLOW, Color.RED, Color.YELLOW]
            },
            "output": (0, 4)
        }
        zero10 = {
            "name": "zero10",
            "input": {
                "sc": [Color.YELLOW, Color.RED, Color.YELLOW, Color.BLUE],
                "user_colors": [Color.BLUE, Color.YELLOW, Color.RED, Color.YELLOW]
            },
            "output": (0, 4)
        }
        zero11 = {
            "name": "zero11",
            "input": {
                "sc": [Color.RED, Color.RED, Color.YELLOW, Color.BLUE],
                "user_colors": [Color.BLUE, Color.YELLOW, Color.RED, Color.YELLOW]
            },
            "output": (0, 3)
        }
        zero12 = {
            "name": "zero12",
            "input": {
                "sc": [Color.RED, Color.RED, Color.GREEN, Color.BLUE],
                "user_colors": [Color.BLUE, Color.YELLOW, Color.RED, Color.YELLOW]
            },
            "output": (0, 2)
        }
        zero13 = {
            "name": "zero13",
            "input": {
                "sc": [Color.RED, Color.BLUE, Color.GREEN, Color.BLUE],
                "user_colors": [Color.BLUE, Color.YELLOW, Color.RED, Color.YELLOW]
            },
            "output": (0, 2)
        }
        one1 = {
            "name": "one1",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.BLUE, Color.GREEN, Color.YELLOW, Color.MAGENTA]
            },
            "output": (1, 2)
        }
        one2 = {
            "name": "one2",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.RED, Color.MAGENTA, Color.YELLOW, Color.MAGENTA]
            },
            "output": (1, 2)
        }


        one2 = {
            "name": "one2",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.GREEN, Color.GREEN, Color.YELLOW, Color.MAGENTA]
            },
            "output": (1, 2)
        }
        one3 = {
            "name": "one3",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.RED, Color.MAGENTA, Color.YELLOW, Color.BLUE]
            },
            "output": (1, 2)
        }
        one4 = {
            "name": "one4",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.RED, Color.MAGENTA, Color.YELLOW, Color.RED]
            },
            "output": (1, 2)
        }
        one5 = {
            "name": "one5",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.RED, Color.MAGENTA, Color.YELLOW, Color.GREEN]
            },
            "output": (1, 3)
        }

        one6 = {
            "name": "one6",
            "input": {
                "sc": [Color.RED, Color.RED, Color.RED, Color.RED],
                "user_colors": [Color.MAGENTA, Color.RED, Color.YELLOW, Color.MAGENTA]
            },
            "output": (1, 0)
        }
        one7 = {
            "name": "one7",
            "input": {
                "sc": [Color.RED, Color.BLUE, Color.YELLOW, Color.YELLOW],
                "user_colors": [Color.RED, Color.RED, Color.RED, Color.RED]
            },
            "output": (1, 0)
        }
        one8 = {
            "name": "one8",
            "input": {
                "sc": [Color.RED, Color.BLUE, Color.YELLOW, Color.YELLOW],
                "user_colors": [Color.BLUE, Color.MAGENTA, Color.YELLOW, Color.RED]
            },
            "output": (1, 2)
        }
        one9 = {
            "name": "one9",
            "input": {
                "sc": [Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.BLUE],
                "user_colors": [Color.BLUE, Color.YELLOW, Color.RED, Color.YELLOW]
            },
            "output": (1, 2)
        }
        one10 = {
            "name": "one10",
            "input": {
                "sc": [Color.GREEN, Color.YELLOW, Color.BLUE, Color.GREEN],
                "user_colors": [Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE]
            },
            "output": (1, 2)
        }

        one11 = {
            "name": "one11",
            "input": {
                "sc": [Color.BLUE, Color.GREEN, Color.BLUE, Color.YELLOW],
                "user_colors": [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]
            },
            "output": (1, 2)
        }

        two1 = {
            "name": "two1",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.RED, Color.MAGENTA, Color.YELLOW, Color.YELLOW]
            },
            "output": (2, 1)
        }

        two2 = {
            "name": "two2",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.RED, Color.GREEN, Color.YELLOW, Color.GREEN]
            },
            "output": (2, 1)
        }
        two3 = {
            "name": "two3",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.RED, Color.GREEN, Color.YELLOW, Color.MAGENTA]
            },
            "output": (2, 2)
        }
        two4 = {
            "name": "two4",
            "input": {
                "sc": [Color.GREEN, Color.GREEN, Color.BLUE, Color.BLUE],
                "user_colors": [Color.GREEN, Color.BLUE, Color.GREEN, Color.BLUE]
            },
            "output": (2, 2)
        }
        two5 = {
            "name": "two5",
            "input": {
                "sc": [Color.RED, Color.BLUE, Color.GREEN, Color.BLUE],
                "user_colors": [Color.BLUE, Color.BLUE, Color.GREEN, Color.YELLOW]
            },
            "output": (2, 1)
        }
        two6 = {
            "name": "two6",
            "input": {
                "sc": [Color.YELLOW, Color.BLUE, Color.GREEN, Color.BLUE],
                "user_colors": [Color.MAGENTA, Color.BLUE, Color.RED, Color.BLUE]
            },
            "output": (2, 0)
        }
        three1 = {
            "name": "three1",
            "input": {
                "sc": [Color.YELLOW, Color.BLUE, Color.GREEN, Color.BLUE],
                "user_colors": [Color.MAGENTA, Color.BLUE, Color.GREEN, Color.BLUE]
            },
            "output": (3, 0)
        }

        three2 = {
            "name": "three2",
            "input": {
                "sc": [Color.RED, Color.RED, Color.RED, Color.RED],
                "user_colors": [Color.RED, Color.RED, Color.YELLOW, Color.RED]
            },
            "output": (3, 0)
        }
        three3 = {
            "name": "three3",
            "input": {
                "sc": [Color.GREEN, Color.RED, Color.YELLOW, Color.RED],
                "user_colors": [Color.RED, Color.RED, Color.YELLOW, Color.RED]
            },
            "output": (3, 0)
        }
        three4 = {
            "name": "three4",
            "input": {
                "sc": [Color.GREEN, Color.MAGENTA, Color.YELLOW, Color.BLUE],
                "user_colors": [Color.GREEN, Color.MAGENTA, Color.YELLOW, Color.RED]
            },
            "output": (3, 0)
        }
        three5 = {
            "name": "three5",
            "input": {
                "sc": [Color.GREEN, Color.GREEN, Color.GREEN, Color.BLUE],
                "user_colors": [Color.GREEN, Color.GREEN, Color.GREEN, Color.RED]
            },
            "output": (3, 0)
        }
        three6 = {
            "name": "three6",
            "input": {
                "sc": [Color.GREEN, Color.GREEN, Color.BLUE, Color.RED],
                "user_colors": [Color.GREEN, Color.GREEN, Color.GREEN, Color.RED]
            },
            "output": (3, 0)
        }
        three7 = {
            "name": "three7",
            "input": {
                "sc": [Color.MAGENTA, Color.YELLOW, Color.BLUE, Color.RED],
                "user_colors": [Color.GREEN, Color.YELLOW, Color.BLUE, Color.RED]
            },
            "output": (3, 0)
        }
        three8 = {
            "name": "three8",
            "input": {
                "sc": [Color.MAGENTA, Color.MAGENTA, Color.BLUE, Color.YELLOW],
                "user_colors": [Color.MAGENTA, Color.MAGENTA, Color.BLUE, Color.RED]
            },
            "output": (3, 0)
        }
        four1 = {
            "name": "four1",
            "input": {
                "sc": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW],
                "user_colors": [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW]
            },
            "output": (4, 0)
        }
        four2 = {
            "name": "four2",
            "input": {
                "sc": [Color.RED, Color.RED, Color.RED, Color.RED],
                "user_colors": [Color.RED, Color.RED, Color.RED, Color.RED]
            },
            "output": (4, 0)
        }

        four3 = {
            "name": "four3",
            "input": {
                "sc": [Color.GREEN, Color.GREEN, Color.BLUE, Color.BLUE],
                "user_colors": [Color.GREEN, Color.GREEN, Color.BLUE, Color.BLUE]
            },
            "output": (4, 0)
        }
        four4 = {
            "name": "four4",
            "input": {
                "sc": [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN],
                "user_colors": [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN]
            },
            "output": (4, 0)
        }
        four5 = {
            "name": "four5",
            "input": {
                "sc": [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE],
                "user_colors": [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE]
            },
            "output": (4, 0)
        }
        four6 = {
            "name": "four6",
            "input": {
                "sc": [Color.MAGENTA, Color.MAGENTA, Color.MAGENTA, Color.MAGENTA],
                "user_colors": [Color.MAGENTA, Color.MAGENTA, Color.MAGENTA, Color.MAGENTA]
            },
            "output": (4, 0)
        }
        four7 = {
            "name": "four7",
            "input": {
                "sc": [Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW],
                "user_colors": [Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW]
            },
            "output": (4, 0)
        }
        four8 = {
            "name": "four8",
            "input": {
                "sc": [Color.YELLOW, Color.RED, Color.YELLOW, Color.YELLOW],
                "user_colors": [Color.YELLOW, Color.RED, Color.YELLOW, Color.YELLOW]
            },
            "output": (4, 0)
        }

        self.zero_tests_data = (zero1, zero2, zero3, zero4, zero5, zero6,
                                zero7, zero8, zero9, zero10, zero11, zero12, zero13)
        self.one_tests_data = (one1, one2, one3, one4, one5, one6, one7, one8, one9, one10, one11)

        self.two_tests_data = (two1, two2, two3, two4, two5, two6)
        self.three_tests_data = (three1, three2, three3, three4, three4, three5, three6, three7, three8)
        self.four_tests_data = (four1, four2, four3, four4, four5, four6, four7, four8)

    def test_zero_data(self):
        for count, test in enumerate(self.zero_tests_data):
            print(f"[ TEST NUMBER] {count + 1} [ NAME ] {test['name']}")
            print(f"SECRET: {test['input']['sc']}")
            print(f"USER_C: {test['input']['user_colors']}")
            print(f"EXPECTED OUTPUT: {test['output']}")
            self.assertEqual(validate(**test["input"]), test["output"], f"Output doesn't match")
            print("=" * 120)

    def test_one_data(self):
        for count, test in enumerate(self.one_tests_data):
            print(f"[ TEST NUMBER] {count + 1} [ NAME ] {test['name']}")
            print(f"SECRET: {test['input']['sc']}")
            print(f"USER_C: {test['input']['user_colors']}")
            print(f"EXPECTED OUTPUT: {test['output']}")
            self.assertEqual(validate(**test["input"]), test["output"], f"Output doesn't match")
            print("=" * 120)

    def test_two_data(self):
        for count, test in enumerate(self.two_tests_data):
            print(f"[ TEST NUMBER] {count + 1} [ NAME ] {test['name']}")
            print(f"SECRET: {test['input']['sc']}")
            print(f"USER_C: {test['input']['user_colors']}")
            print(f"EXPECTED OUTPUT: {test['output']}")
            self.assertEqual(validate(**test["input"]), test["output"], f"Output doesn't match")
            print("=" * 120)

    def test_three_data(self):
        for count, test in enumerate(self.three_tests_data):
            print(f"[ TEST NUMBER] {count + 1} [ NAME ] {test['name']}")
            print(f"SECRET: {test['input']['sc']}")
            print(f"USER_C: {test['input']['user_colors']}")
            print(f"EXPECTED OUTPUT: {test['output']}")
            self.assertEqual(validate(**test["input"]), test["output"], f"Output doesn't match")
            print("=" * 120)

    def test_four_data(self):
        for count, test in enumerate(self.four_tests_data):
            print(f"[ TEST NUMBER] {count + 1} [ NAME ] {test['name']}")
            print(f"SECRET: {test['input']['sc']}")
            print(f"USER_C: {test['input']['user_colors']}")
            print(f"EXPECTED OUTPUT: {test['output']}")
            self.assertEqual(validate(**test["input"]), test["output"], f"Output doesn't match")
            print("=" * 120)

# secret = [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW]
#
# color1 = [Color.BLUE, Color.GREEN, Color.YELLOW, Color.MAGENTA]  # 1, 2
# assert validate(**test1["input"]) == test1["output"]
#
# color2 = [Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE]        # 0, 0
# assert validate(secret, color2) == (0, 0)
#
# color3 = [Color.RED, Color.MAGENTA, Color.YELLOW, Color.YELLOW]  # 2, 1 # WRONG
# assert validate(secret, color3) == (2, 1)
#
# color7 = [Color.RED, Color.MAGENTA, Color.YELLOW, Color.BLUE]    # 1, 2 #
# assert validate(secret, color7) == (1, 2)
#
# secret = [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW]
# color8 = [Color.RED, Color.MAGENTA, Color.YELLOW, Color.RED]    # 1, 2
# assert validate(secret, color8) == (1, 2)
#
# color9 = [Color.RED, Color.MAGENTA, Color.YELLOW, Color.GREEN]    # 1, 3
# assert validate(secret, color9) == (1, 3)
#
# color4 = [Color.RED, Color.GREEN, Color.MAGENTA, Color.YELLOW]  # 4, 0
# assert validate(secret, color4) == (4, 0)
# color5 = [Color.GREEN, Color.RED, Color.YELLOW, Color.MAGENTA]    # 0, 4
# assert validate(secret, color5) == (0, 4)
# color6 = [Color.GREEN, Color.GREEN, Color.YELLOW, Color.MAGENTA]    # 1, 3
# assert validate(secret, color6) == (1, 3)


if __name__ == "__main__":
    unittest.main()


