from colorama import Fore, Style

def display_results(verified_results, any_type) -> str:
    # Validate input to ensure each item has the necessary keys
    for result in verified_results:
        if not {'name', 'passed'}.issubset(result.keys()):
            raise ValueError(f"Missing required keys in the results; each item must have 'name' and 'passed' keys.")

    output = ""
    for result in verified_results:
        if result['passed']:
            output += f"{Fore.GREEN}PASS{Style.RESET_ALL}: {result['name']} - Received expected results.\n"
        else:
            output += f"{Fore.RED}FAIL{Style.RESET_ALL}: {result['name']} - Expected results did not match actual results.\n"
    return output
