#Darren Chau, Shion Mizuguchi
#ECE-455 Final Project
#Enigma Machine Simulator
#Simulating Enigma 1, with choice of five rotors

#imports
import string

#Class to represent each individual rotor
class Rotor:
  def __init__(self, letters, alphabet):
    self.letters = letters #Letters that the rotor maps to the alphabet (A-Z, ordered)
    self.alphabet = alphabet #The alphabet (A-Z, ordered) of the particular rotor

  def shiftRotor(self):
    """Function to shift the rotor by one letter"""
    #Shifts the mapped letters of the rotor by one position
    self.letters = self.letters[1:] + self.letters[0]
    #Shifts the corresponding alphabet (A-Z, ordered) of the rotor by one position
    self.alphabet = self.alphabet[1:] + self.alphabet[0]

  def getLetterAtPos(self, position):
    """Function to return the letter from self.letters given a position"""
    return self.letters[position]

  def getAlphabetAtPos(self, position):
    """Function to return the letter from self.alphabet given a position"""
    return self.alphabet[position]

  def getLetterPos(self, letter):
    """Function to return the position of a letter from self.letters"""
    return self.letters.index(letter)

  def getAlphabetPos(self, letter):
    """Function to return the position of a letter from self.alphabet"""
    return self.alphabet.index(letter)

#String containing all alphabet letters
alphabet = string.ascii_uppercase

#Strings containing the letters that each rotor maps to the alphabet (A-Z, ordered)
    #maps to "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
str_rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
str_rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
str_rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
str_rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"

def start(rotorRnum, rotorMnum, rotorLnum):
  """Function to start a new session of encryption/decryption by choosing and resetting rotors"""
  #Creates all five rotors
  rotor1 = Rotor(str_rotor1, alphabet)
  rotor2 = Rotor(str_rotor2, alphabet)
  rotor3 = Rotor(str_rotor3, alphabet)
  rotor4 = Rotor(str_rotor4, alphabet)
  rotor5 = Rotor(str_rotor5, alphabet)

  #default three rotorset
  rotorR = rotor1
  rotorM = rotor2
  rotorL = rotor3

  #Assigns the right rotor, middle rotor, and left rotor based on user's choice
  #rotorRnum: right rotor choice, rotorMnum: middle rotor choice, rotorLnum: left rotor choice
  if rotorRnum == "1": rotorR = rotor1
  elif rotorRnum == "2": rotorR = rotor2
  elif rotorRnum == "3": rotorR = rotor3
  elif rotorRnum == "4": rotorR = rotor4
  elif rotorRnum == "5": rotorR = rotor5
  if rotorMnum == "1": rotorM = rotor1
  elif rotorMnum == "2": rotorM = rotor2
  elif rotorMnum == "3": rotorM = rotor3
  elif rotorMnum == "4": rotorM = rotor4
  elif rotorMnum == "5": rotorM = rotor5
  if rotorLnum == "1": rotorL = rotor1
  elif rotorLnum == "2": rotorL = rotor2
  elif rotorLnum == "3": rotorL = rotor3
  elif rotorLnum == "4": rotorL = rotor4
  elif rotorLnum == "5": rotorL = rotor5

  return rotorR, rotorM, rotorL

#plugboard_a and plugboard_b represent one plugboard together.
#plugboard_a[i] == plugboard_b[i]
#plugboard_a and plugboard_b together map to "bq cr di ej kw mt os px uz gh"
plugboard_a = "BCDEKMOPUG"
plugboard_b = "QRIJWTSXZH"
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT" #Reflector B

def encrypt(message, rotorRnum, rotorMnum, rotorLnum):
  """Function to encrypt (or decrypt) a given message"""
  message = message.upper()
  encrypted_message = ""

  #Creates right, middle, and left rotors based on user input
  rotorR, rotorM, rotorL = start(rotorRnum, rotorMnum, rotorLnum)
  #Counts if the right rotor and middle rotor made a full rotation
  count_rotorR_shifts = 9 #Initial position/offset of right rotor
  count_rotorM_shifts = 22 #Initial position/offset of middle rotor

  for letter in message:
    #Checks if letter in message string is an alphabet
    #If a user inputs a character that is not an
    #alphabet, it will be kept as is (e.g. spaces)
    if letter in alphabet:
      #Shift right rotor with every key entered
      rotorR.shiftRotor()
      count_rotorR_shifts += 1
      #Shift middle rotor when right rotor fully rotates
      if count_rotorR_shifts == 26:
        rotorM.shiftRotor()
        count_rotorM_shifts += 1
        count_rotorR_shifts = 0 #Reset right rotor's shifts
      #Shifts middle and left rotor when middle rotor fully rotates
      elif count_rotorM_shifts == 26:
        rotorM.shiftRotor()
        rotorL.shiftRotor()
        count_rotorM_shifts = 1 #Since middle rotor shifts, set to 1

      #First checks if inputted letter can be swapped with the plugboard letters
      if letter in plugboard_a:
        letter = plugboard_b[plugboard_a.index(letter)]
      elif letter in plugboard_b:
        letter = plugboard_a[plugboard_b.index(letter)]

      position = alphabet.index(letter)

      #Letter through the three rotors, from the right rotor to left rotor
      letter = rotorR.getLetterAtPos(position)
      position = rotorR.getAlphabetPos(letter)
      letter = rotorM.getAlphabetAtPos(position)
      position = rotorM.getAlphabetPos(letter)
      letter = rotorM.getLetterAtPos(position)
      position = rotorM.getAlphabetPos(letter)
      letter = rotorL.getAlphabetAtPos(position)
      position = rotorL.getAlphabetPos(letter)
      letter = rotorL.getLetterAtPos(position)

      #Letter through the reflector
      position = rotorL.getAlphabetPos(letter)
      letter = reflector[position]

      #Letter through the three rotors, now in the opposite direction from left
      #to right rotor
      position = alphabet.index(letter)
      letter = rotorL.getAlphabetAtPos(position)
      position = rotorL.getLetterPos(letter)
      letter = rotorL.getAlphabetAtPos(position)
      position = rotorL.getAlphabetPos(letter)
      letter = rotorM.getAlphabetAtPos(position)
      position = rotorM.getLetterPos(letter)
      letter = rotorM.getAlphabetAtPos(position)
      position = rotorM.getAlphabetPos(letter)
      letter = rotorR.getAlphabetAtPos(position)
      position = rotorR.getLetterPos(letter)
      letter = rotorR.getAlphabetAtPos(position)
      position = rotorR.getAlphabetPos(letter)
      letter = alphabet[position]

      #Checks if outputted letter from right rotor can be swapped with the
      #plugboard letters
      if letter in plugboard_a:
        letter = plugboard_b[plugboard_a.index(letter)]
      elif letter in plugboard_b:
        letter = plugboard_a[plugboard_b.index(letter)]

      encrypted_message += letter
  return encrypted_message

#Loop to ask user for input message, and check if input is valid
while(True):
  message = input('Enter Message: ')
  if len(message) == 10000:
    print("Your message exceeded the character limit of 10000 characters")
  else: break

#Prints out options in rotorset to user
print("Enigma 1 uses three rotors. You can choose from rotors 1 to 5.")
print("[1] Rotor 1: EKMFLGDQVZNTOWYHXUSPAIBRCJ")
print("[2] Rotor 2: AJDKSIRUXBLHWTMCQGZNPYFVOE")
print("[3] Rotor 3: BDFHJLCPRTXVZNYEIWGAKMUSQO")
print("[4] Rotor 4: ESOVPZJAYQUIRHXLNFTGKDCMWB")
print("[5] Rotor 5: VZBRGITYUPSDNHLXAWMJQOFECK")
print("Enter number corresponding to rotor choice.")

#Loop to ask user's choice of the three rotors, and check if each input is valid
while(True):
  rotorRnum = input("Choose right rotor (1-5): ")
  if rotorRnum.isnumeric()==False or int(rotorRnum) < 1 or int(rotorRnum) > 5:
    print("Right rotor number invalid, enter number between 1 to 5." + "\n")
  else: break
while(True):
  rotorMnum = input("Choose middle rotor (1-5): ")
  if rotorMnum.isnumeric()==False or int(rotorMnum) < 1 or int(rotorMnum) > 5:
    print("Middle rotor number invalid, enter number between 1 to 5." + "\n")
  else: break
while(True):
  rotorLnum = input("Choose left rotor (1-5): ")
  if rotorLnum.isnumeric()==False or int(rotorLnum) < 1 or int(rotorLnum) > 5:
    print("Left rotor number invalid, enter number between 1 to 5" + "\n")
  else: break

#Encrypts message with user's chosen rotorset
encrypted_message = encrypt(message, rotorRnum, rotorMnum, rotorLnum)
print(f"Encrypted message: {encrypted_message}")

#If user wishes to decrypt message, loop takes user's choice and checks if valid
while(True):
  answer = input('Would you like to decrypt the message? (Y/N): ').upper()
  if answer=="Y" or answer=="YES":
    decrypted_message = encrypt(encrypted_message, rotorRnum, rotorMnum, rotorLnum)
    print(f"Decrypted message: {decrypted_message}")
    break
  if answer=="N" or answer=="NO":
    print("Goodbye")
    break
  else:
    print("Invalid input, try again")