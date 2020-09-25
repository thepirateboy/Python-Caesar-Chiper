######## CAESAR CHIPHER, SUPPORT ENCRYPTION & DECRYPTION ########
#This Code is genuine coded by Ahmad Rafi Wiratmoko
#Author     : Ahmad Rafi Wiratmoko
#Version    : 1.1
#Date       : 20 August 2020
#Email      : mail@yaeyx.com
#Instagram  : yaeyx
#visit https://yaeyx.com and https://shit.yaeyx.com for more.


# Make a list of alphabet (why don't i use isalpha() or declare area a-z like before? because that won't be a list).
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# Make some variables and ask their value.
str = input('Input your sentence ')
print('Your sentence:',str)
# why did i use while loop? for keep asking the user if they don't put number. (as protection)
key = None
while key is None:
    input_value = input("Please input the shift key: ")
    try:
        key = int(input_value)
    except ValueError:
        print("{input} is not a number, please enter a number only".format(input=input_value))


# Make define function as a loop
def encode(str):
  str = str.lower()
  result_encode = ''
  for char in str:
    # This is why i use manual alphabet list instead. Because we can locate the order of them.
    if char in alphabet:
      index_old = alphabet.index(char)
      index_new = (index_old + key ) % len(alphabet)
      alphabet_new = alphabet[index_new]
      result_encode = result_encode + alphabet_new 
    else:
       result_encode = result_encode + ' '
  # Send this back as a result.
  return result_encode

str_result = encode(str)
# Make sure, everything on result should be uppercase.
result_final= str_result.upper()

# Make define function as a loop
def decode(str):
  str = str.lower()
  result_decode = ''
  for char in str:
    # This is why i use manual alphabet list instead. Because we can locate the order of them.
    if char in alphabet:
      index_old = alphabet.index(char)
      index_new = (index_old + key *-1 ) % len(alphabet)
      alphabet_new = alphabet[index_new]
      result_decode = result_decode + alphabet_new 
    else:
       result_decode = result_decode + ' ' 
# Send this back as a result.
  return result_decode

str_result = decode(str)
# Make sure, everything on result should be uppercase.
result_final1= str_result.upper()

# why did i use while loop? for keep asking the user if they put something outside e or d. (as protection)
while 1:
    format = input("Do you want encription or decrytption? (type e or d) ").lower()
    if format == "e" or format == "d":
        break
    else:
        print("I'm sorry. only d or e ")

# why i use replace function when print it? because i'm not sure it will remove the space, so did it manually.
if format == "e":
    print('The result of encryption using caesar chiper with key:',key, 'is', result_final.replace(" ",''))
elif format == "d":
    print('The result of decryption using caesar chiper with key:',key, 'is', result_final1.replace(' ', ''))
else:
    print("umm i think you put the wrong input.")
