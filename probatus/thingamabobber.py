import sys
from colorama import Fore, Back, Style
from probatus.loader import load_configuration
from probatus.executor import execute_tests
from probatus.verifier import verify_responses
from probatus.displayer import display_results

class Thingamabobber:
    def thingamabob(self, config_file):
        config = self.load_config(config_file)
        test_results = self.execute(config)
        verified_results = self.verify(test_results, config)
        results = self.display(verified_results)

        print(results)
        print(f"{Back.LIGHTBLUE_EX}Results processed and displayed successfully:{Style.RESET_ALL}")

    def load_config(self, config_file):
        try:
            config = load_configuration(config_file)
            print(f"{Fore.CYAN}Configuration loaded successfully.{Style.RESET_ALL}")
            return config
        except FileNotFoundError as e:
            print(f"{Fore.RED}Configuration file not found: {e}{Style.RESET_ALL}", file=sys.stderr)
            sys.exit(1)
        except ValueError as e:
            print(f"{Fore.RED}Invalid configuration: {e}{Style.RESET_ALL}", file=sys.stderr)
            sys.exit(1)

    def execute(self, config):
        try:
            test_results = execute_tests(config)
            print(f"{Fore.CYAN}Tests executed successfully.{Style.RESET_ALL}")
            return test_results
        except Exception as e:
            print(f"{Fore.RED}Failed to execute tests: {e}{Style.RESET_ALL}", file=sys.stderr)
            sys.exit(1)

    def verify(self, test_results, config):
        try:
            expected_results = [test['expected'] for test in config['tests']]
            verified_results = verify_responses(test_results, expected_results)
            print(f"{Fore.YELLOW}Verification of responses completed successfully.{Style.RESET_ALL}")
            return verified_results
        except Exception as e:
            print(f"{Fore.RED}Failed to verify responses: {e}{Style.RESET_ALL}", file=sys.stderr)
            sys.exit(1)

    def display(self, verified_results):
        try:
            results = display_results(verified_results)
            results_list = results.split('\n')
            if len(results_list) > 1:
                results = '\n'.join(results_list[:-1])  # Join all except the last line.
            return results
        except Exception as e:
            print(f"{Fore.RED}Failed to display results: {e}{Style.RESET_ALL}", file=sys.stderr)
            sys.exit(1)