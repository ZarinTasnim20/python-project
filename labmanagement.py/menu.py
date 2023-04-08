from PC_Function import *
from Store import *
while True:
    print("\nPC Lab Management System")
    print("1. Add a new PC")
    print("2. Update PC information")
    print("3. Remove a PC")
    print("4. Display all PCs")
    print("5. Display a PC")
    print("6. Search for a PC")
    print("7. Store all PCs to file")
    print("8. Quit")
    choice = input("Enter your choice (1-8): ")
    if choice == "1":
        add_pc()
    elif choice == "2":
        update_pc()
    elif choice == "3":
        remove_pc()
    elif choice == "4":
        display_all()
    elif choice == "5":
        display_pc()
    elif choice == "6":
        search_pc()
    elif choice == "7":
        store()
    elif choice == "8":
        break
    else:
        print("Invalid Number choosen.Enter your choice (1-8)")