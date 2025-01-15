alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        print(alphabet.index(letter))
        # 1st solution using if/else
        #
        # index = alphabet.index(letter)
        # if index + shift_amount > len(alphabet) - 1 :
        #     encrypted_text += alphabet[shift_amount - 1]
        # else:
        #     encrypted_text += alphabet[index + shift_amount]

        # 2nd solution using the modulus
        # eg: letter=z shift_amount=2
        # shifted_position = 25 + 2 = 27
        # 27 % 26 = 1
        # 27 / 26 = 1.03846153846 rounded down to 1
        # 26 * 1 = 26
        # 27 - 26 = 1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        encrypted_text += alphabet[shifted_position]

    print(f"Your encode text is: {encrypted_text}")

def decrypt(encrypted_word, shift_amount):
    decrypted_text = ""
    for letter in encrypted_word:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        decrypted_text += alphabet[shifted_position]

    print(f"Your decoded text is: {decrypted_text}")

def ceasar(action, word, shift_amount):
    if action == 'encode':
        encrypt(word, shift_amount)
    else:
        decrypt(word, shift_amount)

ceasar(direction, text, shift)