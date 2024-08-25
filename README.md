<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/he/thumb/1/15/Ministry_of_Education.svg/1200px-Ministry_of_Education.svg.png" width="100" />
</p>
<p align="center">
    <h1 align="center">Ithamar Kaplan's Bagrut Project</h1>
</p>
<p align="center">
    <em><code>► Caesar, Rail Fence and AES encryption using Python and a Flask website</code></em>
</p>
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=flat&logo=visualstudiocode&logoColor=white" alt="Visual Studio Code IDE">
	<img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub">
	<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white" alt="Flask">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/CSS-239120?&style=flat&logo=css3&logoColor=white" alt="CSS">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [Running python-encryption-bagrut](#-running-python-encryption-bagrut)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

<code>► A demo project written in Python 3.12 to demonstrate encryption and decryption of English text with 3 algorithems: Caesar, Rail Fence (Zigzag) and AES. If you don't supply an encryption key for Caesar or Rail Fence, all possible options will be displayed as bruteforce encryption/decryption. The code is exposed as a webpage through Flask framework.</code>

---

##  Features

<details closed><summary>Caesar</summary>
<ul>
  <li>Encryption, supplying an integer numerical key</li>
  <li>Decryption, supplying an integer numerical key</li>
  <li>Encryption/Decryption, without supplying a key - displaying all possible 25 options</li>
</ul>
</details>
<details closed><summary>Rail Fence (Zigzag)</summary>
<ul>
  <li>Encryption, supplying an integer numerical key</li>
  <li>Decryption, supplying an integer numerical key</li>
  <li>Encryption/Decryption, without supplying a key - displaying all possible 25 options</li>
</ul>
</details>
<details closed><summary>AES</summary>
<ul>
  <li>Encryption, using a random key and pre-generated password</li>
  <li>Decryption, extracting the key from the message using the pre-generated password</li>
</ul>
</details>

---

##  Repository Structure

```sh
└── python-encryption-bagrut/
    ├── README.md
    ├── __pycache__
    │   └── function.cpython-311.pyc
    ├── Server-Start.py
    ├── function.py
    ├── static
    │   └── css
    │       └── main.css
    │   └── js
    │       └── script.js
    └── templates
        ├── data.html
        └── form.html
```

---

##  Modules

<details closed><summary>Code Elements</summary>

| File                                                                                                | Summary                         |
| ---                                                                                                 | ---                             |
| [function.py](https://github.com/ithamarkap/python-encryption-bagrut/blob/master/function.py)       | <code>► Main file that holds all the encryption/decryption functions</code> |
| [Server-Start.py](https://github.com/ithamarkap/python-encryption-bagrut/blob/master/Server-Start.py) | <code>► Flask container that handles HTTP requests and distributes them to functions in function.py</code> |

</details>

<details closed><summary>Templates</summary>
| File                                                                                                | Summary                         |
| ---                                                                                                 | ---                             |
| [form.html](https://github.com/ithamarkap/python-encryption-bagrut/blob/master/templates/form.html) | <code>► Input form</code> |
| [data.html](https://github.com/ithamarkap/python-encryption-bagrut/blob/master/templates/data.html) | <code>► Result output</code> |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.x.x` Use the install instructions on their website

###  Installation

1. Clone the python-encryption-bagrut repository or download and extract the zip file

2. Change to the project directory:

```sh
cd python-encryption-bagrut
```

3. Activate the virtual environment:

```sh
pip install cryptography
.\flask2\Scripts\activate
```

###  Running `python-encryption-bagrut`

Use the following command to run python-encryption-bagrut:

```sh
python3 Server-Start.py
```

###  Tests

Use the following command to run tests:

```sh
> INSERT-TEST-COMMANDS
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
