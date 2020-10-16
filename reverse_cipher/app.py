message = "Hello World"

print(f"Original message: {message}")

encrypted_message = "".join(reversed(list(message)))

print(f"Encrypted message: {encrypted_message}")
