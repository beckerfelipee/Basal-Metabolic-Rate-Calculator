import functions as fc
from time import sleep

# Start Screen
sleep(0.5)
print("\n=============== Basal Metabolic Rate Test ===============\n")

sleep(1)
print("\nThis program uses the Harris-Benedict formula to estimate your Basal Metabolic Rate (BMR),\n"
      "which represents the minimum daily energy your body needs at rest. \n")

sleep(2)
start = input("Press [Enter] to start")

# get personal information
name, weight, height, age, sex = fc.get_person_info()

# calculate basal metabolic rate
bmr = fc.calculate_bmr(weight, height, age, sex)

# Display the information
fc.clear(0)  # Create a blank screen
fc.clear(1)
print("\n==================== Final Results ====================\n")
print(f"Name: {name}")
print(f"Weight: {weight} kg")
print(f"Height: {height} meters")
print(f"Age: {age} years")
print(f"\nBasal Metabolic Rate (BMR): {bmr} calories/day")
print("\n=======================================================")

# Ask to save the results to a text file
sleep(2)
print("\nDo you want to save the results to a text file?")
print("\n[ 1 ] Yes \n[ 2 ] No\n")

while True:
    save_option = input("Please enter the corresponding number: ")
    if save_option == "1":
        save = True
        break
    elif save_option == "2":
        save = False
        break

if save:
    fc.export_to_txt(name, weight, height, age, bmr)

sleep(0.3)
print("\nThank you for using the program!")
finish = input("Press [Enter] to finish")
