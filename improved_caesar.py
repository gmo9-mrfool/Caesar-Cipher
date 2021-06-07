
from logo import logo
print(logo)
from data import alphabet,direction,text,shift


def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    for letter in start_text:

        position = alphabet.index(letter)
        if cipher_direction =='decode':
            end_text += alphabet[(position - shift_amount) % 26]
        elif cipher_direction == 'encode':
            end_text += alphabet[(position + shift_amount) % 26]
    print(f"The {cipher_direction}d text is {end_text}")    

should_end=False

while not should_end:

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")

