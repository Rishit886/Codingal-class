def shut_down():
    choice = input("Are you sure you want to shut down the system? Yes or No: ")
    if choice == "Yes":
        print("Shutting down the system...")
        # Add code here to perform the shutdown operation
    elif choice == "No":
        print("Shutdown cancelled.")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")