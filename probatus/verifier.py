from colorama import Fore, Style

def verify_responses(test_results, expected_results):
    verified_results = []
    if len(test_results) != len(expected_results):
        raise ValueError("The number of test results and expected results must match.")

    for test, expected in zip(test_results, expected_results):
        # Check for required keys in both test and expected results to avoid KeyError
        if not {'response', 'status_code', 'name'}.issubset(test.keys()) or not {'response_body', 'status_code'}.issubset(expected.keys()):
            raise KeyError("Missing required keys in the test or expected results dictionaries.")

        if test['response'] == expected['response_body'] and test['status_code'] == expected['status_code']:
            result = {
                'name': test['name'],
                'passed': True,
                'message': f"{Fore.GREEN}PASS{Style.RESET_ALL}: {test['name']} - Received expected results."
            }
        else:
            result = {
                'name': test['name'],
                'passed': False,
                'message': f"{Fore.RED}FAIL{Style.RESET_ALL}: {test['name']} - Expected {expected['response_body']} but got {test['response']}."
            }
        verified_results.append(result)
    return verified_results