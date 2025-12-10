# Simple Python CLI Authentication System

A command-line interface (CLI) application developed in Python to demonstrate fundamental concepts of user authentication, input validation, and data persistence using local file handling.

---

## 🚀 Key Features

* **User Registration:** Allows new users to create an account with a unique User ID, Password, and a 4-digit PIN.
* **User Login:** Authenticates existing users based on their stored credentials.
* **Attempt Limits:** Implements a security feature limiting login attempts for PIN and Password to three times.
* **Data Persistence:** Credentials are saved to and loaded from a local file (`user.txt`).

---

## 🛠️ Getting Started

### Prerequisites

This project requires **Python 3.x**.

### Installation and Execution

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/albin123-eng/Login_learning_FileHandling.git](https://github.com/albin123-eng/Login_learning_FileHandling.git)
    ```

2.  **Navigate to the Directory:**
    ```bash
    cd Login_learning_FileHandling
    ```

3.  **Run the Application:**
    ```bash
    python login.py
    ```

---

## 💻 Technical Details

This project is structured as a basic monolithic application to focus on core concepts.

* **Language:** Python 3.x
* **Data Storage:** Local CSV-like format in a plaintext file (`user.txt`).

> **Note on Security:** For production use, passwords would be hashed (using libraries like `hashlib` or `bcrypt`), and data would be stored in a secure database, not a local plaintext file. This project uses basic file handling for learning and demonstration purposes only.

---

