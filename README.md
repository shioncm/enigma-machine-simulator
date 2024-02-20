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
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- ![Engima machine simulator demo gif][demo-gif] -->
<div align="center">
  <img style="border-radius: 20px" src=./demo.gif width=95% height=95% />
</div>
<br />
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
* To install python3 on another system, follow the instructions on [the official Python website](https://www.python.org/downloads/)

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



<!-- CONTACT -->
## Contact

Shion Mizuguchi: [![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [https://github.com/shioncm/enigma-machine-simulator](https://github.com/shioncm/enigma-machine-simulator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/shioncm/
[demo-gif]: /demo.gif
[Python.com]: https://img.shields.io/badge/-Python-05122A?style=flat&logo=python
[Python-url]: https://www.python.org
