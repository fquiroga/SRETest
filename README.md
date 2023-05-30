# BADSEC User Retrieval Script

This script retrieves a list of users from the BADSEC server.
Usage

Run the script from the command line with optional arguments:

```
python badsec_users.py [--base_url BASE_URL] [--max_retries MAX_RETRIES]
Arguments
```

--base_url: The base URL of the BADSEC server. Default is http://localhost:8888.
--max_retries: The maximum number of retries for each request. Default is 2.
## How it works

    The script first calls the /auth endpoint to get an authentication token.
    It then calculates a checksum using the token and the request path (/users).
    It sends a GET request to the /users endpoint, including the checksum in the X-Request-Checksum header.
    If any of these operations fail, the script retries them up to MAX_RETRIES times, waiting for 1 second between each attempt.
    The script prints the list of users to stdout in JSON format and logs any error messages to stderr. It also exits with a non-zero status code if it fails to retrieve the user list.

## Requirements

Python 3 and the requests library are required to run this script.

You can install requests using pip from command line:

```
pip install requests
```

If you don't have Python installed, you can download it from the official Python website (https://www.python.org/). Make sure to choose the appropriate version for your operating system.
Unpacking

To run this script, save it to a file named badsec_users.py. You can then run it from the command line as described in the Usage section.

If you've received this script as part of an archive (such as a .zip or .tar.gz file), you'll need to extract the archive first. You can do this using tools like unzip or tar on Unix-like systems, or by using the extraction functionality built into your operating system on Windows.