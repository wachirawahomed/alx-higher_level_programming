# 0x11-python-network_1

This repository contains Python scripts that demonstrate various network request functionalities using different libraries such as `urllib` and `requests`.

## Task Descriptions

### Task 0: What's my status?

- Fetches the status from https://alx-intranet.hbtn.io/status using `urllib` and displays information about the response body.

### Task 1: Response header value

- Takes a URL as input, sends a request to the URL using `urllib`, and displays the value of the `X-Request-Id` variable found in the header of the response.

### Task 2: POST an email

- Takes a URL and an email as input, sends a POST request to the URL with the email as a parameter using `urllib`, and displays the body of the response.

### Task 3: Error code

- Takes a URL as input, sends a request to the URL using `urllib`, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints "Error code:" followed by the value of the HTTP status code.

### Task 4: What's my status? #1

- Fetches the status from https://alx-intranet.hbtn.io/status using `requests` and displays information about the response body.

### Task 5: Response header value #1

- Takes a URL as input, sends a request to the URL using `requests`, and displays the value of the `X-Request-Id` variable found in the header of the response.

### Task 6: POST an email #1

- Takes a URL and an email as input, sends a POST request to the URL with the email as a parameter using `requests`, and displays the body of the response.

### Task 7: Error code #1

- Takes a URL as input, sends a request to the URL using `requests`, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints "Error code:" followed by the value of the HTTP status code.

### Task 8: Search API

- Takes a letter as input, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter using `requests`, and displays the body of the response based on the JSON format.

### Task 9: My GitHub!

- Takes GitHub credentials (username and personal access token) as input, uses the GitHub API to display the user id using Basic Authentication with a personal access token.

### Task 10: Time for an interview!

- Lists 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails” using the GitHub API.

## Usage

To run any of the scripts, simply execute them in the terminal and provide any required arguments.

```bash
./script_name.py arg1 arg2 ...
