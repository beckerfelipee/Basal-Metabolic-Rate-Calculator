from time import sleep
from os import name as os_name, system

# Clear the sreen on terminal
def clear(sec):
    if os_name in ('nt', 'dos'):
        command = 'cls'
    else:
        command = 'clear'
    sleep(sec)
    return system(command)

def safe_input(description, convert_type="float", min_range="none", max_range="none"):

    # description: phrase that will appear in input("here")
    # convert type: must be "float" or "int"
    # min_range: can be "none" or a string format number (example: "10")
    # max_range: can be "none" or a string format number (example: "10")

    while True:
        var = input(description)
        try:

            if convert_type == "float":
                if "," in var:
                    var = var.replace(",", ".")
                var = float(var)
            elif convert_type == "int":
                var = int(var)
            else:
                print(f"Error: Conversion is only supported for Float or Int, not {convert_type}.")

            if min_range != "none" and max_range != "none":
                if not int(min_range) < var < int(max_range):
                    print("Oops! It seems like you entered an invalid number.")
                else:
                    break
            else:
                break

        except ValueError:
            print("Oops! It seems like you entered an invalid number.")
            pass

    return var

def get_person_info():
    while True:
        clear(0.3)
        print("\n================== Insert Information ==================\n")

        name = input("Name: ")

        # weight - between 20 and 400 kilograms
        weight = safe_input(description="Weight in KG: ", min_range="20", max_range="400")

        # height - between 1 and 3 meters
        height = safe_input(description="Height in Meters: ", min_range="1", max_range="3")

        # age - between 6 and 120 years old
        age = safe_input(description="Age: ", convert_type="int", min_range="6", max_range="120")

        # Biological Sex - Male or Female
        print("\nBiological Sex: \n [ 1 ] Male \n [ 2 ] Female \n [ 3 ] Why is this information important to collect?")
        while True:
            option = input("\nPlease Enter the corresponding number: ")

            if option == "1":
                sex = "male"
                break
            elif option == "2":
                sex = "female"
                break
            elif option == "3":
                sleep(0.5)
                print("\nCollecting biological sex information is crucial for applying accurate "
                      "Harris-Benedict formulas,\n"
                      "which consider distinct metabolic needs,"
                      " enabling precise customization of nutritional recommendations")
                sleep(1)
            else:
                print("Invalid Input")
                sleep(0.5)

        # Check Inputs
        clear(0.5)
        print("\n================== Confirm Information ==================\n")
        print(f"Name: {name}")
        print(f"Weight: {weight} kg")
        print(f"Height: {height} meters")
        print(f"Age: {age} years")
        print(f"Biological Sex: {sex}")
        print("\n [ 1 ] Confirm \n [ 2 ] Decline\n")
        while True:
            option = input("Please Enter the corresponding number: ")
            if option == "1":
                confirm = True
                break
            elif option == "2":
                confirm = False
                break
        if confirm:
            break

    return name, weight, height, age, sex

def calculate_bmr(weight, height, age, sex):
    # Formulas:
    # BMR Male: (10p) + (6.25A) - (5I) + 5
    # BMR Female: (10p) + (6.25A) - (5I) - 161

    # Convert Height in Meters to centimeters
    height = height * 100

    if sex == "male":
        result = (weight * 10) + (height * 6.25) - (age * 5) + 5
    else:
        result = (weight * 10) + (height * 6.25) - (age * 5) - 161

    result = round(result)  # convert to integer

    return result

def export_to_txt(name, weight, height, age, bmr, filename="default"):
    if filename == "default":
        filename = name + "_BMR.txt"

    with open(filename, 'w') as file:
        file.write("==================== Final Results ====================\n")
        file.write(f"\nName: {name}")
        file.write(f"\nWeight: {weight} kg")
        file.write(f"\nHeight: {height} meters")
        file.write(f"\nAge: {age} years")
        file.write(f"\n\nBasal Metabolic Rate (BMR): {bmr} calories/day")
        file.write("\n\n=======================================================")

    print(f"\nResults saved to '{filename}'!")
