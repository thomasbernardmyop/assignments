# ################################################## #
#                                                    # 
#                                                    #
#  BIT502 Fundamentals of Programming Assessment 1   #
#  Student Name: Thomas Bernard                      #
#  Student ID: 12345678                              #
#                                                    #
# ################################################## #

import os
import math

# -----------------------------
# Utility: Clear the screen
# -----------------------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# -----------------------------
# Input Validation 
# -----------------------------

def get_menu_choice():
    while True:
        choice = input("Please select an option 1-5: ")

        if not choice.isdigit():
            print("Invalid input. Please enter a NUMBER between 1 and 5.")
            continue

        choice_num = int(choice)

        if 1 <= choice_num <= 5:
            return choice
        else:
            print("Invalid selection. Please choose a number BETWEEN 1 and 5.")


# -----------------------------
# Main Menu
# -----------------------------

def mainmenu():
    clear_screen()
    print("==== Aurora Library Console Application ====")
    print()
    print("1. Membership Plans")
    print("2. Optional Extras")
    print("3. Reading Challenges")
    print("4. Aurora-Picks Rental Calculator")
    print("5. Exit Application")
    return get_menu_choice()



# -----------------------------
# Membership Plans
# -----------------------------

def membershiplan():
    while True:
        clear_screen()
        print("==== Membership Plans ====")
        print()
        print("1. Standard Membership")
        print("2. Premium Membership")
        print("3. Kids Membership")
        print("4. Return to Main Menu")
        print("5. Exit Application")

        choice = get_menu_choice()

        if choice == '1':
            clear_screen()
            print("=== Membership Information ====")
            print()
            print("Standard Membership selected.")
            print("Standard Membership is $10 per month.")
            print("Standard Membership includes access to all regular book collections and basic library services.")
            print()
            input("Press Enter to continue...")

        elif choice == '2':
            clear_screen()
            print("=== Membership Information ====")
            print()
            print("Premium Membership selected.")
            print("Premium Membership is $15 per month.")
            print("Premium Membership includes access to all regular book collections and basic library services Discounts and special rates ")
            print()
            input("Press Enter to continue...")

        elif choice == '3':
            clear_screen()
            print("=== Membership Information ====")
            print()
            print("Kids Membership selected.")
            print("Kids Membership is $5 per month.")
            print("Kids Membership includes access to all regular book collections and basic library services.")
            print("but at a cheaper rate for children under 12.")
            print()
            input("Press Enter to continue...")

        elif choice == '4':
            return

        elif choice == '5':
            return "exit"
        
# -----------------------------
# Optional Extras
# -----------------------------        

def optionalextras():
    clear_screen()
    print("==== Optional Extras ====\n")

    print(" Book Rental — $5")
    print("• Borrow one book at a time from a selection of older titles.")
    print("• Return the book to borrow another, up to twice per month.")
    print("• This rental option is separate from the Aurora-Picks system.")
    print("\n------------------------------\n")

    print("  Private Area Access — $15")
    print("• Access to the quiet reading area on the second floor.")
    print("• Comfortable seating and a peaceful environment.")
    print("\n------------------------------\n")

    print("  Monthly Booklet — $2")
    print("• A monthly booklet delivered at the start of each month.")
    print("• Includes news, events, reviews, and upcoming releases.")
    print("\n------------------------------\n")

    print("  Online eBook Rental — $5")
    print("• Borrow eBooks using an e-reader device.")
    print("• One member per book at a time.")
    print("• Books auto-return after 7 days.\n")

    input("Press Enter to continue...")

    total = 0

    book_rental = ask_yes_no("Would you like the book rental for $5?")
    private_area = ask_yes_no("Would you like private area access for $15?")
    booklet = ask_yes_no("Would you like the monthly booklet for $2?")
    ebook = ask_yes_no("Would you like the online ebook rental for $5?")

    if book_rental:
        total += 5

    if private_area:
        total += 15

    if booklet:
        total += 2

    if ebook:
        total += 5

    print("\nHere are the extras you selected:\n")

    if book_rental:
        print("Book Rental — $5")

    if private_area:
        print("Private Area Access — $15")

    if booklet:
        print("Monthly Booklet — $2")

    if ebook:
        print("Online eBook Rental — $5")

    print(f"\nTotal cost for extras: ${total}")

    input("\nPress Enter to return to the main menu...")

# -----------------------------
# Reading Challenges
# -----------------------------    



def number_checker(day):
    while True:
        pages_input = input(f"How many pages did you read on {day}? ").strip()

        # Empty input check
        if pages_input == "":
            print("Error: Input cannot be empty. Please enter a number (e.g., 10 or 10.5).")
            continue

        try:
            pages = float(pages_input)

            # Check if vaild / postive number

            if math.isnan(pages) or math.isinf(pages):
                print("Error: Please enter a valid, finite number.")
                continue

            if pages < 0:
                print("Error: Pages cannot be negative. Please enter 0 or a positive number.")
                continue

            return pages  

        except ValueError:
            print("Error: Invalid input. Please enter a number (e.g., 10 or 10.5).")

def readingchallenges():
    clear_screen()
    print("==== Welcome to Aurora Archive Kids' Reading Challenges ====\n")
    print("Enter the pages you read each weekday (Monday to Friday).")
    print("Decimals are okay (e.g., 23.7). If you didn't read, enter 0.")
    input("\nPress Enter to continue...")

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    pages = []

    
    for day in days:
        pages_for_that_day = number_checker(day)
        pages.append(pages_for_that_day)

    # Calculations
    total = sum(pages)
    average = total / 5
    max_pages = max(pages)
    top_days = [d for d, p in zip(days, pages) if p == max_pages]

    # Ranks 

    if total <= 25:
        rank = "Bronze"
    elif total <= 50:
        rank = "Silver"
    elif total <= 100:
        rank = "Gold"
    else:
        rank = "Platinum"

 ## Display Results
 
    clear_screen()
    print("==== Reading Challenge Results ====\n")
    print(f"Total pages read: {total:.0f}")
    print(f"Average pages per day: {average:.1f}")

    if len(top_days) == 1:
        print(f"{top_days[0]} was your biggest reading day!")
    else:
        joined = " and ".join(top_days) if len(top_days) == 2 else ", ".join(top_days[:-1]) + f", and {top_days[-1]}"
        print(f"Your biggest reading days were: {joined}!")

    print(f"You ranked {rank}!")


    if rank == "Bronze":
        needed = max(0.0, 26 - total)   
        print(f"To reach the next rank you need to read {needed:.0f} more pages. Good luck!")
    elif rank == "Silver":
        needed = max(0.0, 51 - total)   
        print(f"To reach the next rank you need to read {needed:.0f} more pages. Good luck!")
    elif rank == "Gold":
        needed = max(0.0, 101 - total) 
        print(f"To reach the next rank you need to read {needed:.0f} more pages. Good luck!")
    else:
        print("Amazing! You’re at the highest rank—Platinum! There is no further rank.")


    if total > 150:
        print("\n🎉 New Record! You’ve beaten the current weekly record of 150 pages. Outstanding!")

    input("\nPress Enter to return to the main menu...")



### Rental Calculator 

def rentalcalculator():
    while True:
        clear_screen()
        print("==== Aurora-Picks Rental Calculator ====")
        print()
        print("1. Enter rental period")
        print("2. Return to main menu")
        
        choice = input("\nSelect an option 1–2: ")

        if choice not in ['1', '2']:
            print("Error ❌ Please Select Option 1 or 2. ")
            input("Press Enter to try again...")
            continue  


        if choice == '1':
            clear_screen()
            print("==== Enter Rental Period ====\n")

            while True:
                days = input("Enter Number of Rental Days (3–21): ")

                if not days.isdigit():
                    print("Error ⚠️  : Please enter a whole number ")
                    continue

                days = int(days)

                if days < 3:
                    print("Warning ⚠️  Minimum rental is 3 days ")
                    continue

                if days > 21:
                    print("Warning ⚠️  Maximum rental is 21 days ")
                    continue

                break

        #### Calucate the cost 

           
            if days == 21:
                total_cost = 12
            else:
                total_cost = 0

                first_block = min(days, 3)
                total_cost += first_block * 1.00

                
                if days > 3:
                    second_block = min(days - 3, 5)
                    total_cost += second_block * 0.80

                
                if days > 8:
                    third_block = min(days - 8, 12)
                    total_cost += third_block * 0.50

            print(f"\nTotal rental cost for {days} days is: ${total_cost:.2f}")
            input("\nPress Enter to return to the rental menu...")

        elif choice == '2':
            return

   
                  



#-----------------------------
# Question Menus
# -----------------------------

def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter Yes/y or No/n.")



# -----------------------------
# Exit
# -----------------------------

def exitapplication():
    clear_screen()
    print("Exiting the application. Goodbye!")


# -----------------------------
# Program Loop
# -----------------------------

if __name__ == "__main__":
    while True:
        user_choice = mainmenu()

        if user_choice == '1':
            result = membershiplan()
            if result == "exit":
                exitapplication()
                break

        elif user_choice == '2':
            result = optionalextras()
            

        elif user_choice == '3':
            result = readingchallenges()

        elif user_choice == '4':
            result = rentalcalculator()
            

        elif user_choice == '5':
            exitapplication()
            break