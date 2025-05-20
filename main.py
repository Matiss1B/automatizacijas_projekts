from linkedList import LinkedList
from excel import update_excel, create_email_linked_list, mark_emails_as_sent
from seleniumFunctions import send_email
import os
import re

def is_email(line):
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_pattern, line) is not None
def read_emails(template_name):
    file_path = f"address_lists/{template_name}"
    if not os.path.exists(file_path):
        print(f"No such file or directory: {file_path}")
        return LinkedList()
    with open(file_path, "r") as file:
        lines = file.readlines()
    email_linked_list = LinkedList()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if ' ' in stripped:
            print("Wrong file format")
            return False
        if not is_email(stripped):
            print("Wrong email format :"+stripped)
            return False
        email_linked_list.append(stripped)

    return email_linked_list


def print_emails(template_name):
    file_path = f"address_lists/{template_name}"
    if not os.path.exists(file_path):
        print(f"No such file or directory: {file_path}")
        return LinkedList()
    print(f'Emails in address_lists/{template_name} :')
    with open(file_path, "r") as file:
        lines = file.readlines()
    for line in lines:
        print(line.strip())

if __name__ == '__main__':
    while True:
        command = input("Please enter command (print_file / update_excel / send_email / exit): ").strip()
        if command == "print_file":
            file_name = input("Enter the name of the file:").strip()
            print_emails(file_name)

        elif command == "update_excel":
            file_name = input("Enter the name of the file to update Excel from:").strip()
            if not os.path.exists(f"address_lists/{file_name}"):
                print(f"File not found: address_lists/{file_name}")
                continue
            email_list = read_emails(file_name)
            if email_list:
                update_excel(email_list)
                print("New emails added!")

        elif command == "send_email":
            file_name = input("Enter path to filename to take content. ").strip()
            if not os.path.exists(f"content/{file_name}"):
                print(f"File not found: content/{file_name}")
                continue
            email_listFromExel = create_email_linked_list('mails.xlsx')
            if email_listFromExel.length > 0:
                if send_email(email_listFromExel, file_name):
                    mark_emails_as_sent(email_listFromExel)
            else:
                print("Emails already are sent to all addresses!")

        elif command == "exit":
            print("Exiting program.")
            break
        else:
            print("Unknown command. Try again.")


