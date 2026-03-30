# Password Generator and Manager

A Python-based password manager that demonstrates secure password storage, authentication, and password generation.
This project showcases fundamental cybersecurity concepts such as hashing, authentication, and password policy enforcement.

---

## Features

* Secure password input using `getpass`
* Password hashing using **SHA-256**
* Strong password generation
* Password strength validation
* Username-based authentication system
* Simple CLI interface

---

## Technologies Used

* Python
* hashlib
* getpass
* random

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/DIVYAthakur-DT/password-manager.git
cd password-manager
```

---

### 2. Run the Program

```
python password_manager.py
```

---

## Usage

After running the program, you will see:

```
====== Password Manager ======
1. Create Account
2. Login
0. Exit
```

### Create Account

* Enter a username
* Choose to generate a strong password or enter manually
* Password is validated and securely hashed before storage

### Login

* Enter your username and password
* Password is hashed and compared with stored credentials

---

## Example Output

```
====== Password Manager ======
1. Create Account
2. Login
0. Exit

Enter your choice: 1
Enter your username: admin
Generate random password? (yes/no): yes
Generated password: A8#s2F!kL0z
Account created successfully!
```

---

## Security Concepts Demonstrated

| Concept           | Implementation                         |
| ----------------- | -------------------------------------- |
| Confidentiality   | Passwords stored using SHA-256 hashing |
| Integrity         | Hash comparison during login           |
| Authentication    | Username/password validation           |
| Password Security | Strength validation rules              |
| Secure Input      | Hidden password entry using `getpass`  |

These concepts align with the **CIA Triad (Confidentiality, Integrity, Availability)**.

---

## Project Structure

```
password-manager
│
├── password_manager.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Disclaimer

This project is for **educational purposes only** and demonstrates basic cybersecurity concepts.

---

## Author

DIVYA

GitHub: https://github.com/DIVYAthakur-DT
