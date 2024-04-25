# 0x10-python-network_0
This repository contains a collection of Bash scripts for performing various HTTP requests using `curl`.

## Scripts

1. **0-body_size.sh**: Sends a request to a URL and displays the size of the body of the response.
2. **1-body.sh**: Sends a GET request to a URL and displays the body of the response if the status code is 200.
3. **2-delete.sh**: Sends a DELETE request to a URL and displays the body of the response.
4. **3-methods.sh**: Takes in a URL and displays all HTTP methods the server will accept.
5. **4-header.sh**: Sends a GET request to a URL with a custom header and displays the body of the response.
6. **5-post_params.sh**: Sends a POST request to a URL with specified parameters and displays the body of the response.
7. **100-status_code.sh**: Sends a request to a URL and displays only the status code of the response.
8. **101-post_json.sh**: Sends a JSON POST request to a URL with the contents of a file as the request body and displays the body of the response.
9. **102-catch_me.sh**: Makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing "You got me!" in the body of the response.

## Usage

To use any of the scripts, simply run them in your terminal and follow the instructions provided in the script's documentation.

For example:
```bash
./0-body_size.sh 0.0.0.0:5000
