def main():
    # Capture the full name
    full_name = input("Enter your first, middle, and last names: ")

    # Split the name into parts
    name_parts = full_name.split()

    # Check if there are exactly three parts
    if len(name_parts) == 3:
        first_initial = name_parts[0][0].upper()
        middle_initial = name_parts[1][0].upper()
        last_initial = name_parts[2][0].upper()

        # Display the initials
        print(f"{first_initial}. {middle_initial}. {last_initial}.")
    else:
        print("Please enter exactly three names (first, middle, and last).")

# Execute the main function
if __name__ == "__main__":
    main()

  
