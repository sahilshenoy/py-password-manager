from stdiomask import getpass
import storage
from time import sleep
global count
count = 0

def signup():
    username = input("Enter your Master username: ")
    while True:
        if username in storage.users:
            username = input("Enter new Master username: ")
        else:
            break
    password = getpass("Enter your Master password: ")
    confirm = getpass("Confirm your Master password: ")
    if password == confirm:
        storage.users.append(username)
        storage.users_pass.append([username, password])
        print("Master Login Created Successfully.")
        with open("storage.py", "a") as file:
            file.write(f"users_pass={storage.users_pass}")
            file.write(f"users= {storage.users}")

        login()


def login():
    global username
    username = input('Enter your Master username: ')
    password = getpass('Enter your Master password: ')
    count+=1
    if [username, password] in storage.users_pass:
        print(f"Login Successful {username}")
        firstpage()
    else:
        while count < 3:
            if count=="1":
                print("You've two chances left.")
            elif i=="second":
                print("You have one chnace left")
            elif i=="third":
                print("You've zero chances left. Try again after 20 seconds")
                count=1
                while count<20:
                    print (count)
                    sleep(1)
                    count+=1
                login()




def firstpage():
    choice = int(input("""
    1. View all stored username and passwords (Type 1)
    2. Store new username and password (Type 2)
    3. Delete some login (Type 3)
    4. Edit some login (Type 4)
    5. Exit
    """))
    run = True
    while run:
        if choice == 1:
            view_pass()
            run = False
        elif choice == 2:
            new_pass()
            run = False
        elif choice == 3:
            delete_pass()
            run = False
        elif choice == 4:
            edit_pass()
            run = False
        elif choice == 5:
            print("Code is terminated.")
            break
        else:
            print("Wrong input! Try again!")


def view_pass():
    for item in storage.masterpass_list:
        if item[0] == username:
            print("Website Name: ", item[1])
            print("Website Username: ", item[2])
            print("Website Password: ", item[3])
            print("--------------------------------------------\n")
    print(f"All passwords under {username} are listed.")
    firstpage()


def new_pass():
    website_name = input("Enter Name of the Website: ")
    website_username = input(f"Enter the username on the {website_name}: ")
    website_password = input(f"Enter the password on the {website_name}: ")
    storage.masterpass_list.append(
        [username, website_name, website_username, website_password])
    print(
        f"Successfully added the login info about {website_name} for {username}")
    with open ("storage.py", "a") as f:
        f.write(f"masterpass_list = {storage.masterpass_list}")
    firstpage()


def delete_pass():
    for item in storage.masterpass_list:
        if item[0] == username:
            web_choice = input(
                "Enter name of the Website of the login that you want to delete: ")
            if item[1].lower() == web_choice.lower():
                storage.masterpass_list.remove(item)
    with open ("storage.py", "a") as f:
        f.write(f"masterpass_list= {storage.masterpass_list}")
    print(f"Successfully deleted the {web_choice} for {username}")
    firstpage()


def edit_pass():
    for item in storage.masterpass_list:
        if item[0] == username:
            edit_choice = int(input("""
            1. Edit Website Name (Type 1)
            2. Edit Username (Type 2)
            3. Edit Password (Type 3)
            """))
            if edit_choice == 1:
                old_web_name = input("Enter old website name: ")
                new_web_name = input("Enter new website name: ")
                item[1] = item[1].replace(old_web_name, new_web_name)
                firstpage()
            elif edit_choice == 2:
                webname = input("Enter old website name: ")
                old_username = input("Enter old username: ")
                new_username = input("Enter new username:")
                if item[1] == webname:
                    if item[2] == old_username:
                        item[2] = item[2].replace(old_username, new_username)
                firstpage()
            elif edit_choice == 3:
                old_web_name_p = input("Enter the website name")
                old_pass = input("Enter the old password: ")
                new_pass = input("Enter new password: ")
                if item[1].lower() == old_web_name_p.lower():
                    if item[3] == old_pass:
                        item[3] = item[3].replace(old_pass, new_pass)
                firstpage()
            else:
                print("Wrong Choice!")
                edit_pass()


def main():
    new_user = input("Are you a new user? (Y/N): ")
    if new_user.upper() == "Y":
        signup()
    else:
        login()


main()
