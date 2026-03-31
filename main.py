import json
from datetime import datetime

DATA_FILE = "data.json"

# Load existing data
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add new health log
def add_log():
    date = datetime.now().strftime("%Y-%m-%d")
    food = input("Enter food taken: ")
    water = int(input("Water intake (glasses): "))
    poop = int(input("Number of bowel movements: "))

    entry = {
        "date": date,
        "food": food,
        "water": water,
        "poop": poop
    }

    data = load_data()
    data.append(entry)
    save_data(data)

    print("✅ Log added successfully!")

# View logs
def view_logs():
    data = load_data()
    if not data:
        print("No data found!")
        return

    for entry in data:
        print("\nDate:", entry["date"])
        print("Food:", entry["food"])
        print("Water:", entry["water"], "glasses")
        print("Bowel movements:", entry["poop"])

# Health analysis
def analyze_health():
    data = load_data()
    if not data:
        print("No data to analyze!")
        return

    last = data[-1]

    print("\n🔍 Health Analysis for", last["date"])

    if last["water"] < 5:
        print("⚠️ Low water intake! Drink more water.")

    if last["poop"] == 0:
        print("⚠️ Possible constipation detected!")

    if last["poop"] > 3:
        print("⚠️ Too frequent bowel movements!")

    print("✅ Analysis complete.")

# Menu
def main():
    while True:
        print("\n--- Student Health Tracker ---")
        print("1. Add Log")
        print("2. View Logs")
        print("3. Analyze Health")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_log()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            analyze_health()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
