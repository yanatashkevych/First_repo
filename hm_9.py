def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner

contacts = {}

@error_handler
def hello():
    return "How can I help you?"

@error_handler
def add(name, phone):
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."

@error_handler
def change(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} changed to {new_phone}."
    else:
        print(f"Contact {name} not found.")

@error_handler
def phone(name):
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}."
    else:
        print(f"Contact {name} not found.")

@error_handler
def show_all():
    if not contacts:
        return "No contacts available."
    result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return result

def main():
    while True:
        user_input = input("Enter a command: ").lower()

        if user_input in ['good bye', 'close', 'exit', '.']:
            print("Good bye!")
            break

        elif user_input == "hello":
            print(hello())

        elif user_input.startswith("add "):
            _, contact_info = user_input.split(' ', 1)
            name, phone = contact_info.split(' ', 1)
            print(add(name, phone))

        elif user_input.startswith("change "):
            _, contact_info = user_input.split(' ', 1)
            name, new_phone = contact_info.split(' ', 1)
            print(change(name, new_phone))

        elif user_input.startswith("phone "):
            _, name = user_input.split(' ', 1)
            print(phone(name))

        elif user_input == "show all":
            print(show_all())

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
 


