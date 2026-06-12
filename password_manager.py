passwords = {
    "gmail":"aditya@123",
    "you tube": "qwerty@123",
    "discord" : "qwerty_aditya@123",
}

shift_value = 3

def encryption_text(plain_text):
    encrypted = ""
    for ch in plain_text:
        if ch.islower():
            new_char =chr(((ord(ch)-97+shift_value)%26)+97)
            encrypted+= new_char

        elif ch.isupper():
            new_char = chr(((ord(ch)-65+shift_value)%26)+65)
            encrypted += new_char
        else:
            encrypted += ch
    return encrypted

def decrypt_text(cipher_text):
    decrypted= ""
    for ch in cipher_text:
        if ch.islower():
            new_char= chr(((ord(ch)-97 - shift_value)%26)+97)
            decrypted +=new_char
        elif ch.isupper():
            new_char = chr(((ord(ch)-65 - shift_value)%26)+65)
            decrypted += new_char
        else:
            decrypted += ch
    return decrypted
def view_accounts():
    print("\n ==========SAVED ACCOUNTS==========")
    print("-----------------------------------------")
    for account in passwords:
        print("-", account)

def add_password():
    account = input("\n Enter account name:").lower()
    if account in passwords:
        print("Account already exists.")
        return
    password =input("Enter a password:")
    encrypted_pass = encryption_text(password)
    passwords[account] = encrypted_pass
    print("Password saved successfully.")

def search_password():
    account = input("\n Enter acc name to search:").lower()
    if account in passwords:
        encrypted_pass= passwords[account]
        decrypted_pass = decrypt_text(encrypted_pass)
        print("\n Account Found")
        print("-------------------")
        print("Services:", account)
        print("Encrypted password:", encrypted_pass)
        print("Decrypted password:", decrypted_pass)
    else:
        print("Account not found")
    
def view_passwords():
    if len(passwords) == 0:
        print ("\n No passwords stored.")
        return
    print("\n stored passwords.")
    print("-----------------------------")
    for account, encrypted_pass in passwords.items():
        decrypt_pass = decrypt_text(encryption_text)
        print("Service:", account)
        print("Decrypted:",decrypt_pass)
        print("Encrypted:",encrypted_pass)
        
while True:
    print("\n========================================")
    print("Cryptography & Password Manager")
    print("==========================================")

    print("1. View Saved Accounts")
    print("2. Add New Password")
    print("3. Search Account Password")
    print("4. View Decrypted Passwords")
    print("5. Exit")   

    choice=int(input("Enter your choice:"))

    if choice ==1:
        view_accounts()
    elif choice ==2:
        add_password()
    elif choice == 3:
        search_password()
    elif choice ==4:
        view_passwords()
    elif choice ==5:
        print("\nExiting program....")
        print("\n Program exited successfully!")
        break
    else:
        print("/n INVALID CHOICE. Please try again...")