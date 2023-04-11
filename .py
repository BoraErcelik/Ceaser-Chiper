alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def ceaser(d, t, s):
  plain_text = t
  cipher_text = t
  if d == "encode":
    cipher_text = ''
    for letter in plain_text:
      position = alphabet.index(letter)
      new_positon = position + s
      new_letter = alphabet[new_positon]
      cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
  elif d == "decode":
    plain_text = ''
    for letter in cipher_text:
      position = alphabet.index(letter)
      new_position = position - s
      plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  ceaser(d=direction, t=text, s=shift)
  start_over = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if start_over == 'no':
    should_continue = False
    print("Goodbye")
