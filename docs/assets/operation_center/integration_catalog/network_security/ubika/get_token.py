# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///
import json
import os
import tempfile

import requests


def get_device_code() -> dict:
    """
    Get device code for Ubika API authentication.
    """

    url = "https://login.ubika.io/auth/realms/main/protocol/openid-connect/auth/device"
    payload = {
        "client_id": "rest-api",
        "grant_type": "device",
        "scope": "offline_access"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=payload, headers=headers)
    return response.json()


def get_token(device_code: str) -> dict:
    """
    Get access token using device code.
    """

    url = "https://login.ubika.io/auth/realms/main/protocol/openid-connect/token"
    payload = {
        "client_id": "rest-api",
        "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
        "device_code": device_code
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=payload, headers=headers)
    return response.json()


def save_in_file(file_path: str, data: dict):
    """
    Save data in a file.
    """

    with open(file_path, "w+") as f:
        json.dump(data, f, indent=4)


def main():
    """
    Main function to get device code and then access token.
    """

    with tempfile.TemporaryDirectory(delete=False) as tempdir:
        print(f"The progression of this script will be saved in {tempdir}")

        # Step 1: Get device code
        device_code_response = get_device_code()

        # Create a temporary file to store the device code
        device_code_file = os.path.join(tempdir, "device_code.txt")
        save_in_file(device_code_file, device_code_response)

        # Print the device code and verification URL
        print("Please copy the following user code and visit the URL to authorize:")
        print("User Code:", device_code_response['user_code'])
        print("Verification URL:", device_code_response['verification_uri'])
        print("Or visit the following URL to authorize:")
        print(f"\x1b]8;id=verification_uri;{device_code_response['verification_uri_complete']}\x1b\\{device_code_response['verification_uri_complete']}\x1b]8;;\x1b\\")
        input("Press Enter after authorizing...")

        # Step 2: Get access token using device code
        access_token_response = get_token(device_code_response['device_code'])

        # Create a temporary file to store the token
        token_file = os.path.join(tempdir, "access_token.txt")
        save_in_file(token_file, access_token_response)

        # Print the access token and refresh token
        print(f"refresh_token: {access_token_response['refresh_token']}")


if __name__ == "__main__":
    main()

