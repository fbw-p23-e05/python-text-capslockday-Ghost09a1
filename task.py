def normalize_sentence(input_string):
    if input_string.isupper():
        normalized_string = input_string.lower() + "!"
    else:
        normalized_string = input_string.capitalize()

    return normalized_string
user_input = input("Enter string: ")# Input
output = normalize_sentence(user_input)
print(output)
