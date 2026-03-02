"""
BMI Calculator - Command Line Application
CSE 4283/6283 Assignment 2
"""


def calculate_bmi(height_feet, height_inches, weight_lbs):
    """
    Calculate BMI given height in feet/inches and weight in pounds.
    
    Formula:
      1. Convert weight: weight_kg = weight_lbs * 0.45
      2. Convert height: height_m = total_inches * 0.025
      3. BMI = weight_kg / (height_m ** 2)
    
    Returns:
        float: BMI value rounded to 1 decimal place
    """
    total_inches = (height_feet * 12) + height_inches
    weight_kg = weight_lbs * 0.45
    height_m = total_inches * 0.025
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)


def get_bmi_category(bmi):
    """
    Return the BMI category string based on the BMI value.
    
    Categories (smallest allowable change = 0.1):
        < 18.5          -> Underweight
        18.5 - 24.9     -> Normal weight
        25.0 - 29.9     -> Overweight
        >= 30.0         -> Obese
    
    Returns:
        str: BMI category label
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal weight"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def run_bmi_calculator():
    """Interactive command line interface for BMI calculation."""
    print("=" * 50)
    print("       BMI Calculator")
    print("=" * 50)

    while True:
        try:
            height_feet = int(input("\nEnter height (feet): "))
            height_inches = float(input("Enter height (inches): "))
            weight_lbs = float(input("Enter weight (pounds): "))

            if height_feet < 0 or height_inches < 0 or weight_lbs <= 0:
                print("Error: Please enter positive values.")
                continue

            bmi = calculate_bmi(height_feet, height_inches, weight_lbs)
            category = get_bmi_category(bmi)

            print("\n--- Results ---")
            print(f"  BMI Value    : {bmi}")
            print(f"  Category     : {category}")
            print("---------------")

        except ValueError:
            print("Error: Please enter valid numeric values.")
            continue

        again = input("\nCalculate again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    run_bmi_calculator()
