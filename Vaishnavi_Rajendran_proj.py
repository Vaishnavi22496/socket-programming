"""
 High-level Description:
 This client program designed to connect to the server at the specified server port and IP address.
 After successful connection it sends an Introductory message containing the NU ID to authenticate.
 server receives the arithmetic expression for the client to evaluate, the client evaluate each
 expression and send back the result to the server.
 If the result is correct, the client continues to receive and evaluate the expression.
 If the result is incorrect, the server sends a failure message and the connection is closed.
 Upon successful evaluation of all expressions, server sends a successful message with the unique
 flag, which is extracted and displayed. The client program handle both server message and user Input,
 to ensure smooth communication.

 NU ID: 002826489
 Secret Flag: cec5ef7d055e6243c7d52074aa4a3da8052c69ea50dd7f29744eab5f5e99d69e

 Author: Vaishnavi Rajendran


 """



import socket

# Define the server's hostname and port number
server_hostname = "129.10.132.64"
server_port = 5206 # We can try different port numbers within the range [5203, 5212]

# create a socket to connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # connect to the server
    client_socket.connect((server_hostname, server_port))
    print("Connected to the server successfully")

    nuid = "002826489" # replace 'NUID' with my actual NU ID

    # Create the introductory message
    intro_message = f"EECE7374 INTR {nuid}"

    # Send the introductory message to the server
    client_socket.sendall(intro_message.encode())

    while True:
        # Receive the expression message from the server
        modified_sentence = client_socket.recv(1024).decode()
        if not modified_sentence:
            break  # No more data from the server

        print(f"Received expression message: {modified_sentence}")
        if modified_sentence.startswith("EECE7374 EXPR"):

            # Extract the expression from the message
            expression = " ".join(modified_sentence.split(" ")[2:])

            try:
                # Evaluate the expression
                result = eval(expression)

                # create the result message
                result_message = f"EECE7374 RSLT {result}"
                # Send the result message back to the server
                client_socket.sendall(result_message.encode())

            except Exception as e:
                # Handle evaluation errors (e.g., invalid expressions)
                error_message = "EECE7374 FAIL"
                client_socket.sendall(error_message.encode())
                print(f"Error evaluating expression: {expression}")

        # This is a success message the received message starts with the expected format "EECE7374 SUCC"
        elif modified_sentence.startswith("EECE7374 SUCC"):
            parts = modified_sentence.split(" ") # Split the message to extract the secret flag
            if len(parts) == 3:
                secret_flag = parts[2]
                print(f"Secret Flag: {secret_flag}")
            else:
                # Handle unexpected message format (not enough parts)
                print("Received success message with unexpected format.")
        else:
            # Handle unexpected message format (neither "EXPR" nor "SUCC")
            print("Received message with unexpected format.")

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close the client socket, whether there was an error or not
    client_socket.close()








