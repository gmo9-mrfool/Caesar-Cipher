
from data import alphabet,direction,text,shift
from logo import logo
print(logo)




# defining encrypt block
def encrypt(t,s):
  t.split()
  cipher_text=''
  for i in t:
      position= alphabet.index(i)
      cipher_text += alphabet[(position + s) % 26]
    
    # cipher_text += alphabet[new_position]
  print(f'The encoded text is {cipher_text}')
def decode(t,s):
  t.split()
  plain_text=''
  for i in t:
      position= alphabet.index(i)
      plain_text += alphabet[(position - s) % 26]
  print(f'The encoded text is {plain_text}')  

if direction=='encode':
    encrypt(t=text,s=shift)
elif direction =='decode':
    decode(t=text,s=shift)    


