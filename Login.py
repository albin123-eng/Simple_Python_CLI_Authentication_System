
class AuthSystem:
    def __init__(self, filename="user.txt"):
        self.filename = filename
        self.credentials = self.load_credentials()

    def load_credentials(self):

        credentials = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    data = line.strip()
                    if data:
                        # Split each line into user, pin, and password
                        part = [x.strip() for x in data.split(",")]
                        if len(part) == 3:
                            user, pin, password = part
                            credentials.append((user, pin, password))
        except FileNotFoundError:
            print("Error: Credential file not found.")
            return []
        except ValueError:
            print("Error: Malformed line found in credential file. Check file format.")
            return []
        return credentials

    def get_attempt(self, prompt, correct_value):
        attempt = 0
        while attempt < 3:
            in_value = input(prompt)
            if in_value == correct_value:
                return True
            else:
                print('Invalid value. Try again')
                attempt += 1
        return False

    def login(self):
        print()
        print('Login to AE Labs')
        print()

        all_credictional = self.load_credentials()
        if not all_credictional:
            print("Login Failed.")

        user_id = input('Enter your User ID: ').strip()
        found = None
        for user, pin, password in all_credictional:
            if user == user_id:
                found = (user, pin, password)
                break
        if found is None:
            print('Invalid User ID.')

        else:
            correct_user, correct_pin, correct_password = found

            if not self.get_attempt('Please enter your PIN: ', correct_pin):
                print('Invalid Pin. Access Denied')
                return
            if not self.get_attempt('Please enter your Password: ', correct_password):
                print('Invalid Password.Access Denied')
                return
            print(f'Welcome back, {correct_user}! Access Accepted.')

    def create_account(self):
        userID = input('Enter your User ID: ').strip()
        password = input('Enter your Password: ').strip()

        while True:
            pin = input('Enter your Pin: ').strip()
            if len(pin) == 4:
                break
            else:
                print('Pin must be 4 digits.')

        try:
            with open('user.txt', 'a') as file1:
                 file1.write(f"{userID}, {pin}, {password}\n")
            print("Account created successfully!")

        except FileNotFoundError:
            print(f"An error occurred while creating the account: ")

    def main(self):
        while True:
            print('Welcome to AE Labs')
            print('Press 1 for Login: ')
            print('Press 2 for Create account: ')
            print('Press 3 for Exit: ')
            choice = input('Enter your choice: ').strip()
            if choice == '1':
                self.login()
            elif choice == "2":
                self.create_account()
            elif choice == '3':
                break
            else:
                print("Invalid choice.")




