def main():
    # Get file name and user info
    file_name = input("Enter your file name: ")
    user = input("Enter your name: ")
    address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")  # Keep it as string to preserve formatting

    # Open the file for writing
    with open(file_name, 'w') as file:
        file.write(f'Name: {user}\n')
        file.write(f'Address: {address}\n')
        file.write(f'Phone: {phone_number}\n')

    print(f"Data written to {file_name}")

# Call the main function.
if __name__ == '__main__':
    main()
