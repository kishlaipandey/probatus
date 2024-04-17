import requests
import sys

def execute_tests(config):
    test_results = []
    for test in config['tests']:
        url = config['environment']['base_url'] + test['endpoint']
        headers = {**config['environment']['headers'], **test.get('headers', {})}

        method = test['method'].lower()  # lowercase for easy comparison
        body = test.get('body', {})
        params = test.get('params', {})

        try:
            if method == 'get':
                response = requests.get(url, headers=headers, params=params)
            elif method == 'post':
                response = requests.post(url, json=body, headers=headers)
            elif method == 'put':
                response = requests.put(url, json=body, headers=headers)
            elif method == 'delete':
                response = requests.delete(url, headers=headers)
            elif method == 'patch':
                response = requests.patch(url, json=body, headers=headers)
            elif method == 'options':
                response = requests.options(url, headers=headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
        except requests.exceptions.RequestException as e:
            # Log network-related errors and continue with the next test
            print(f"Network error occurred while attempting to perform {method} request: {e}", file=sys.stderr)
            continue

        response_data = response.json() if 'application/json' in response.headers.get('Content-Type', '') else response.text
        result = {
            'name': test['name'],
            'status_code': response.status_code,
            'response': response_data
        }
        test_results.append(result)
    return test_results