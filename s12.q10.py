import math
import random
from datetime import datetime

# Global logbook to store all calculations
calc_logbook = {}

def current_datetime():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %I:%M %p") # DD/MM/YYYY 12hr format

def menu_display():
    print("\n" + "*" * 35)
    print(" SAYALI'S PYTHON CALCULATOR PRO")
    print("*" * 35)
    print("1. Simple Math + - * /")
    print("2. Science Mode √ ^ sin cos log")
    print("3. Lucky Numbers Random Gen")
    print("4. My Calculations View Log")
    print("5. Clear My Log")
    print("6. Exit App")
    print("*" * 35)

def do_simple_math():
    try:
        a = float(input("First value: "))
        operator = input("Pick operation [ + - * / ]: ")
        b = float(input("Second value: "))

        operations = {
            '+': a + b,
            '-': a - b,
            '*': a * b,
            '/': a / b if b!= 0 else None
        }

        if operator not in operations:
            print("Wrong operator! Use only + - * /")
            return None
        if operator == '/' and b == 0:
            print("Math Error: Can't divide by zero")
            return None

        answer = operations[operator]
        print(f"Answer = {answer}")
        return f"{a} {operator} {b} = {answer}"

    except ValueError:
        print("Input Error: Please enter numbers only")
    except Exception as err:
        print(f"Something broke: {err}")
    return None

def science_mode():
    try:
        print("\n--- Science Mode ---")
        print("a. Square Root √")
        print("b. Power x^y")
        print("c. Sine sin()")
        print("d. Cosine cos()")
        print("e. Log base 10")

        opt = input("Choose a/b/c/d/e: ").lower()

        if opt == 'a':
            val = float(input("Enter number for √: "))
            if val < 0:
                print("Error: Square root of negative not allowed")
                return None
            res = math.sqrt(val)
            print(f"√{val} = {res}")
            return f"√{val} = {res}"

        elif opt == 'b':
            x = float(input("Base number: "))
            y = float(input("Power: "))
            res = math.pow(x, y)
            print(f"{x} ^ {y} = {res}")
            return f"{x}^{y} = {res}"

        elif opt == 'c':
            deg = float(input("Angle in degrees: "))
            res = math.sin(math.radians(deg))
            print(f"sin({deg}°) = {res:.4f}")
            return f"sin({deg}°) = {res:.4f}"

        elif opt == 'd':
            deg = float(input("Angle in degrees: "))
            res = math.cos(math.radians(deg))
            print(f"cos({deg}°) = {res:.4f}")
            return f"cos({deg}°) = {res:.4f}"

        elif opt == 'e':
            val = float(input("Number for log10: "))
            if val <= 0:
                print("Error: Log only defined for positive numbers")
                return None
            res = math.log10(val)
            print(f"log10({val}) = {res}")
            return f"log10({val}) = {res}"
        else:
            print("Invalid option selected")

    except ValueError:
        print("Input Error: Please enter a number")
    except Exception as err:
        print(f"Error: {err}")
    return None

def lucky_number_gen():  #i.e.random number generatot
    
    try:
        print("\n--- Lucky Number Generator ---")
        print("x. Random Integer")
        print("y. Random Decimal 0-1")
        print("z. Pick From List")

        pick = input("Choose x/y/z: ").lower()

        if pick == 'x':
            low = int(input("Start range: "))
            high = int(input("End range: "))
            lucky = random.randint(low, high)
            print(f"Your lucky number: {lucky}")
            return f"Random int({low},{high}) = {lucky}"

        elif pick == 'y':
            lucky = random.random()
            print(f"Lucky decimal: {lucky:.4f}")
            return f"Random decimal = {lucky:.4f}"

        elif pick == 'z':
            data = input("Enter items with space: ").strip()
            if not data:
                print("List is empty")
                return None
            item_list = data.split()
            lucky = random.choice(item_list)
            print(f"Picked for you: {lucky}")
            return f"Random choice from {item_list} = {lucky}"
        else:
            print("Invalid option")

    except ValueError:
        print("Please enter valid numbers for range")
    except Exception as err:
        print(f"Error: {err}")
    return None

def show_logbook():
    if not calc_logbook:
        print("\nLogbook is empty. Do some calculations first!")
        return

    print("\n" + "="*50)
    print(" MY CALCULATION LOGBOOK")
    print("="*50)
    count = 1
    for time, calc in calc_logbook.items():
        print(f"{count}. [{time}] → {calc}")
        count += 1
    print("="*50)
    print(f"Total Entries: {len(calc_logbook)}")

def run_calculator():
    print("Welcome to Sayali's Calculator!")

    while True:
        menu_display()
        try:
            user_choice = input("Enter option 1-6: ")

            if not user_choice.isdigit():
                print("Enter a number between 1-6")
                continue

            choice = int(user_choice)
            calc_entry = None

            if choice == 1:
                calc_entry = do_simple_math()
            elif choice == 2:
                calc_entry = science_mode()
            elif choice == 3:
                calc_entry = lucky_number_gen()
            elif choice == 4:
                show_logbook()
            elif choice == 5:
                calc_logbook.clear()
                print("Logbook cleared! Fresh start.")
            elif choice == 6:
                print("Thanks for using my calculator! Bye ")
                break
            else:
                print("Choose a number between 1-6")

            # Save to logbook if calculation happened
            if calc_entry:
                time_stamp = current_datetime()
                calc_logbook[time_stamp] = calc_entry
                print(f"Saved @ {time_stamp}")

        except KeyboardInterrupt:
            print("\nExiting... Bye!")
            break
        except Exception as err:
            print(f"App crashed: {err}")


if __name__ == "__main__":
    run_calculator()