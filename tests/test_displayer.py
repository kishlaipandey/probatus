import unittest
from probatus import displayer
from colorama import Fore, Style

class TestDisplayResults(unittest.TestCase):
    def setUp(self):
        self.verified_results_pass = [
            {'name': 'Test 1', 'passed': True},
            {'name': 'Test 2', 'passed': True}
        ]
        self.verified_results_fail = [
            {'name': 'Test 3', 'passed': False},
            {'name': 'Test 4', 'passed': False}
        ]
        self.verified_results_mixed = [
            {'name': 'Test 5', 'passed': True},
            {'name': 'Test 6', 'passed': False}
        ]

    def test_all_passing_results(self):
        output = displayer.display_results(self.verified_results_pass)
        self.assertTrue(f"{Fore.GREEN}PASS{Style.RESET_ALL}" in output)
        self.assertFalse(f"{Fore.RED}FAIL{Style.RESET_ALL}" in output)

    def test_all_failing_results(self):
        output = displayer.display_results(self.verified_results_fail)
        self.assertTrue(f"{Fore.RED}FAIL{Style.RESET_ALL}" in output)
        self.assertFalse(f"{Fore.GREEN}PASS{Style.RESET_ALL}" in output)

    def test_mixed_results(self):
        output = displayer.display_results(self.verified_results_mixed)
        self.assertTrue(f"{Fore.GREEN}PASS{Style.RESET_ALL}" in output and f"{Fore.RED}FAIL{Style.RESET_ALL}" in output)

    def test_missing_keys(self):
        incomplete_results = [{'name': 'Test 7'}]
        with self.assertRaises(ValueError):
            displayer.display_results(incomplete_results)

if __name__ == '__main__':
    unittest.main()