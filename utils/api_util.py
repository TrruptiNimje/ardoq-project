import requests


class ApiUtil:

    def get(url, headers=None, params=None):
        # Makes a GET request to the given URL.
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            raise AssertionError(f"GET request to {url} failed: {e}")

    def verify_status_code(response, expected_status_code):
        # Verifies the response status code.
        assert response.status_code == expected_status_code, \
            f"Expected status code {expected_status_code}, but got {response.status_code}"
