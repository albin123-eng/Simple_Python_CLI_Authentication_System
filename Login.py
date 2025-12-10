def load_credentials():

    credentials = []
    try:
        with open("user.txt", "r") as f:
            for line in f:
                data = line.strip()
                if data:
                    # Split each line into user, pin, and password
                    user, pin, password = [x.strip() for x in data.split(",")]
                    credentials.append((user, pin, password))
    except FileNotFoundError:
        print("Error: Credential file not found.")
        return []
    except ValueError:
        print("Error: Malformed line found in credential file. Check file format.")
        return []
    return credentials

def get_attempt(prompt, correct_value):
    attempt = 0
    while attempt < 3:
        in_value = input(prompt)
        if in_value == correct_value:
            return True
        else:
            print('Invalid value. Try again')
            attempt += 1
    return False

def login():
    print()
    print('Login to AE Labs')
    print()

    all_credictional = load_credentials()
    if not all_credictional:
        print("Login Failed.")

    user_id = input('Enter your User ID: ').strip()
    found = None
    for user, pin, password in all_credictional:
        if user == user_id:
            found = (user, pin, password)
            break
    if found is None:
        print('Invaild User ID.')

    else:
        correct_user, correct_pin, correct_password = found

        if not get_attempt('Please enter your PIN: ', correct_pin):
            print('Invalid Pin. Access Denied')
            return
        if not get_attempt('Please enter your Password: ', correct_password):
            print('Invalid Password.Access Denied')
            return
        print(f'Welcome back, {correct_user}! Access Accepted.')

def create_accounct():
    UserID = input('Enter your User ID: ').strip()
    Password = input('Enter your Password: ').strip()

    while True:
        Pin = input('Enter your Pin: ').strip()
        if len(Pin) == 4:
            break
        else:
            print('Pin must be 4 digits.')

    try:
        with open('user.txt', 'a') as file1:
             file1.write(f"{UserID}, {Pin}, {Password}\n")
        print("Account created successfully!")

    except FileNotFoundError:
        print(f"An error occurred while creating the account: ")

def main():
    while True:
        print('Welcome to AE Labs')
        print('Press 1 for Login: ')
        print('Press 2 for Create account: ')
        print('Press 3 for Exit: ')
        choice = input('Enter your choice: ').strip()
        if choice == '1':
            login()
        elif choice == "2":
            create_accounct()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


main()


