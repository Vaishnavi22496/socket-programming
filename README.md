Overview
This repository contains a Python-based client application for socket programming. The client is designed to connect to a specified server using a given IP address and port number. It primarily handles arithmetic expressions sent by the server, evaluates them, and sends back the results. The application demonstrates fundamental concepts of network communication, error handling, and data exchange over sockets.

Features
Connection Setup: Initiates a socket connection to a server with predefined IP and port.
Authentication: Sends an introductory message containing a unique identifier (NU ID) for server authentication.
Expression Evaluation: Receives arithmetic expressions from the server, evaluates them, and returns the results.
Result Validation: Continuously processes expressions sent by the server until an incorrect result is submitted, upon which the server sends a failure message and terminates the connection.
Success Acknowledgment: On successful evaluation of all expressions, receives a success message with a unique secret flag.
Error Handling: Manages various potential errors, including invalid expressions and unexpected message formats.
Resource Management: Ensures proper closing of the socket connection after communication ends, regardless of success or failure.
Configuration
To connect to a different server, modify the server_hostname and server_port variables in the script with the appropriate IP address and port number.

Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License.

Authors
Vaishnavi Rajendran
