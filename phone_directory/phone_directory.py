# Function to store the contacts of people in a dictionary
def phone_directory():
    # Empty List of contacts
    contacts = []
    max_contacts = 5
    
    # Loop thorugh
    while True:
        # List of options
        print(f"""
                1. Add contact information.
                2. View contact information.
                3. Search for contact info.
                4. Delete contact information.
                5. Exit.""")
        
        
        try:
            # Prompt the user to choose an option
            users_choice = int(input("Choose an Option: "))
            
            
            # If a user chooses option 1
            if users_choice == 1:
                # User prompt for name
                name = input("Enter your name: ").upper()
                # User prompt for number
                number = input("Enter your number: ")
                
                # If the list is full
                if len(contacts) == max_contacts:
                    print("List full, can't add more contacts, Fail")
                else:
                    # Append the user info to the list
                    contacts.append({"name": name, "number": number})
                    # Alert the user
                    print("Contact added successfully.")
                
            # If a user chooses option 2
            elif users_choice == 2:
                # If the phone directory is empty,
                if not contacts:
                    print(f"List Empty")
                # If It has come content, loop thorugh
                else:
                    # Loop though all the content
                    for contact in contacts:
                        # Output the info
                        print(f"{contact['name']}->{contact['number']}")
                        
            # If a user chooses option 3
            elif users_choice == 3:
                # Prompt the user to search for info by the name
                search = input("Enter a name ot search: ").upper()
                
                # Initially set found to false (assume you have not found anything since you have not even started searching)
                found = False
                
                # Loop through each contact
                for contact in contacts:
                    # If the contact name matches the searched name
                    if contact['name'] == search:
                        print(f"Found: {contact['name']} -> {contact['number']}")
                        # Update the state to true
                        found = True
                        # Break out of the loop
                        break
                # If the contact has not been found
                if not found:
                    print("Contact not found.")
            
            # If a user chooses option 3
            elif users_choice == 4:
                print("\nContact is deleted by the name\n❗❗NAME + NUMBER WILL BE DELETED")
                # Delete by the name
                del_input= input("Enter the contact to delete: ").upper()
                # new list of contacts
                new_contacts = [c for c in contacts if c['name'] != del_input]
                
                # Update the list
                # If the length of the new_list  is less than the length of the original list
                if len(new_contacts) < len(contacts):
                    # Create a shallow copy of the new list
                    contacts[:] = new_contacts
                    print("Contact deleted successfully.")
                else:
                    print("Contact not found.")
                    
            elif users_choice == 5:
                print("Exiting phone directory, GoodBye!")
                break
            
            else:
                print("Invalid Option, Please choose a valid option.")
            
            
        except Exception as e:
            print("Error: ", e)    
    
# Ensure that It is running directly and not as an inported file
if __name__ == "__main__":
    phone_directory()
    