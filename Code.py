
description = "This program turns your message into a code.\nEvery letter in your message will move up 4 spaces!"

alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "

print(description)

message = input("Enter a message to turn to code: ").lower()
translated_message = ""

for letter in message:
    if not letter in punctuation and letter.isalpha():
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value + 5) % 26]
    else:
        translated_message += letter


print(translated_message)
