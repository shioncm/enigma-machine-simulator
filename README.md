<!-- See: https://github.com/othneildrew/Best-README-Template/ -->
<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h1 align="center">Enigma Machine Simulator</h3>
  <p align="center">
    Simulation of the Enigma 1, the first Enigma machine used by the German army.
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The enigma machine is a cipher machine that was used by Germany during the Second World War. It was used extensively throughout the entirety of the conflict, and the Allies devoted considerable resources into cracking the machine, while the Germans worked to ensure it stayed out of enemy hands and updated the security of the system. The Enigma machine is well known for the large number of settings that can be used with the Machine, making decryption difficult. At the same time, flaws in its design and operational use allowed the Allies to eventually crack the enigma machine.  

This program seeks to simulate the Enigma 1 machine in Python. The Enigma 1 had five rotors and room for three, with the operator swapping the rotors, location, and
starting position. Our rotors have the same sequences as those used for Enigma 1. Our program allows a user to input a sequence of letters, choose three rotors out of five provided, receive an encrypted sequence, and then decrypt it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python.com]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

To run this program, you need Python 3 installed on your system.
* To install python3 on a Linux/UNIX system:
  ```sh
  sudo apt-get update
  sudo apt-get install python3.6
  ```
* To install python3 on another system, follow instructions on [the official Python website](https://www.python.org/downloads/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/shioncm/enigma-machine-simulator
   ```
2. Run the script inside the cloned repo
   ```sh
   python3 main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The plugboard is represented by two sequences of 10 letters. The plugboard does not swap every letter, and generally only 10 plugboard connections were made in Enigma 1 operations. Letters in the same position in both sequences are swapped, so B is swapped with Q and vice versa.

```python
plugboard_a = "BCDEKMOPUG"
plugboard_b = "QRIJWTSXZH"
```

The reflector is represented by a string of the 26 letters of the alphabet. Letters are simply swapped based on position. 

```python
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT" #Reflector B
```

The rotors are represented by a rotor class. They are initialized by inputting the letter sequence of the rotor. To simulate the rotor and its shifting functionality, the class has a letter sequence that maps to the alphabet (A-Z, ordered) and its corresponding alphabet sequence are set for each rotor. In other words, the two sequences mirror each other and represent a mapping. The class also includes functions to shift the position of the rotor, get the position of a letter in the letter sequence, return the letter at a position, gets the position of a letter in the alphabet sequence, and returns the letter at a position in the alphabet sequence.

```python
class Rotor:
def __init__(self, letters, alphabet):
  self.letters = letters #Letters that the rotor maps to the alphabet (A-Z, ordered)
  self.alphabet = alphabet #The alphabet (A-Z, ordered) of the particular rotor
def shiftRotor(self):
  """Function to shift the rotor by one letter"""
2
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
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Shion Mizuguchi: [![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [https://github.com/shioncm/enigma-machine-simulator](https://github.com/shioncm/enigma-machine-simulator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/shioncm/
[product-screenshot]: images/screenshot.png
[Python.com]: https://img.shields.io/badge/-Python-05122A?style=flat&logo=python
[Python-url]: https://www.python.org
