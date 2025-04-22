
from belief_base import BeliefBase

def main():
    bb = BeliefBase()

    # Add some beliefs
    bb.add_belief("A >> B")  # A implies B
    bb.add_belief("B >> C")  # B implies C
    bb.add_belief("A")       # A is true

    print("\n--- Current Belief Base ---")
    bb.display_beliefs()

    print("\nConsistency check:", bb.is_consistent())  # Should be consistent

    # Add a conflicting belief
    bb.add_belief("~C")  # Not C, which contradicts the implications from A

    print("\n--- After adding ~C ---")
    bb.display_beliefs()

    print("\nConsistency check:", bb.is_consistent())  # Should be inconsistent

    # Remove the conflicting belief
    bb.remove_belief("~C")

    print("\n--- After removing ~C ---")
    bb.display_beliefs()
    print("\nConsistency check:", bb.is_consistent())  # Should be consistent again

if __name__ == "__main__":
    main()
