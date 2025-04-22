
from belief_base import BeliefBase
from belief_revision import revise

def main():
    belief_base = BeliefBase()

    while True:
        print("\n===== Belief Revision Interactive Console =====")
        print("1. Show current belief base")
        print("2. Add belief")
        print("3. Remove belief")
        print("4. Revise belief base with a new formula")
        print("5. Exit")
        print("==============================================")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            belief_base.display_beliefs()

        elif choice == '2':
            formula = input("Enter a formula to add: ")
            belief_base.add_belief(formula)
            print(f"Added: {formula}")

        elif choice == '3':
            formula = input("Enter a formula to remove: ")
            belief_base.remove_belief(formula)
            print(f"Removed: {formula}")

        elif choice == '4':
            phi = input("Enter the new formula φ for revision: ")
            revise(belief_base, phi)
            print("Belief base revised.")

        elif choice == '5':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid option. Please enter 1-5.")

if __name__ == "__main__":
    main()
