
"""
BioBuddy - Plant Health Detective
An interactive plant-care project built with Python.
"""

BANNER = """
========================================
       🌱 BIOBUDDY 🌱
     PLANT HEALTH DETECTIVE
========================================
"""

def ask_choice(question, options):
    print("\n" + question)

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(options):
                return choice

        print("Invalid choice. Please try again.")


def investigate_plant():
    print("\nLet's investigate your plant!")

    leaf = ask_choice(
        "What do the leaves look like?",
        [
            "Yellow leaves",
            "Brown or crispy edges",
            "Drooping leaves",
            "Healthy green leaves"
        ]
    )

    soil = ask_choice(
        "How does the soil feel?",
        [
            "Very dry",
            "Slightly moist",
            "Wet or soggy",
            "I am not sure"
        ]
    )

    sunlight = ask_choice(
        "How much sunlight does the plant receive?",
        [
            "Very little light",
            "Bright indirect light",
            "Strong direct sunlight"
        ]
    )

    watering = ask_choice(
        "How often do you water your plant?",
        [
            "Every day",
            "When the top soil feels dry",
            "Only occasionally"
        ]
    )

    findings = []
    advice = []

    # Check for possible overwatering
    if soil == 3 and (leaf == 1 or leaf == 3 or watering == 1):
        findings.append("Possible overwatering")
        advice.append(
            "Check drainage and allow the soil to dry "
            "appropriately before watering again."
        )

    # Check for possible underwatering
    if soil == 1 and (leaf == 3 or leaf == 2 or watering == 3):
        findings.append("Possible underwatering")
        advice.append(
            "Check the plant's water requirements and "
            "water thoroughly if needed."
        )

    # Check for possible sunlight stress
    if sunlight == 3 and leaf == 2:
        findings.append("Possible sunlight stress")
        advice.append(
            "Consider moving the plant to suitable "
            "indirect light."
        )

    if sunlight == 1 and leaf == 1:
        findings.append("Possible low-light stress")
        advice.append(
            "Consider a brighter location suitable "
            "for your plant species."
        )

    if soil == 4:
        findings.append("Soil moisture needs checking")
        advice.append(
            "Check moisture below the soil surface "
            "before deciding whether to water."
        )

    if not findings:
        findings.append("No clear cause identified")
        advice.append(
            "Observe new growth and check for pests, "
            "drainage problems, and species-specific needs."
        )

    print("\n" + "=" * 40)
    print("       YOUR BIOBUDDY REPORT")
    print("=" * 40)

    for finding in findings:
        print("\nPossible clue:", finding)

    print("\nSuggested next steps:")

    for item in dict.fromkeys(advice):
        print("-", item)

    print(
        "\nNote: These are possible explanations, "
        "not a confirmed plant diagnosis."
    )


def main():
    print(BANNER)
    print("Your little assistant for plant-care clues.")

    while True:
        investigate_plant()

        again = input(
            "\nCheck another plant? (y/n): "
        ).strip().lower()

        if again not in ("y", "yes"):
            print("\nThanks for using BioBuddy!")
            print("Keep observing. Keep growing! 🌿")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBioBuddy session ended. Goodbye!")
