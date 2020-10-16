import string

letters = list(string.ascii_lowercase)


def encrypt(message, key, letters):
    message = message
    key = key
    modules = len(letters)

    encrypted_message = []

    for char in message:
        char_index = letters.index(char)
        encrypted_char = letters[(char_index + key) % modules]
        encrypted_message.append(encrypted_char)

    # print(encrypted_message)
    encrypted_message = "".join(encrypted_message)
    return encrypted_message


def decrypt(message, key, letters):
    message = message
    key = key
    modules = len(letters)

    decrypted_message = []

    for char in message:
        char_index = letters.index(char)
        decrypted_char = letters[(char_index - key + modules) % modules]
        decrypted_message.append(decrypted_char)

    # print(encrypted_message)
    decrypted_message = "".join(decrypted_message)
    return decrypted_message


print(encrypt("hello", 3, letters))
print(decrypt(encrypt("hello", 3, letters), 3, letters))


# def ceaser_index(i, key, modules):
#     return (i + key) % modules


# def char_to_index():
#     pass


# alpha_org_chars = list(string.ascii_lowercase)
# # alpha_org_index = [index for index, item in enumerate(alpha_org_chars)]
# alpha_org_table = {}

# for i in range(len(alpha_org_chars)):
#     alpha_org_table[str(alpha_org_chars[i]): i]

# print(alpha_org_table)


# # alpha_org_table = list(zip(alpha_org_chars, alpha_org_index))
# # modules = len(alpha_org_table)
# # key = 3
# # print(alpha_org_table)
# # print(alpha_org_table)
# # print(alpha_org_index)
