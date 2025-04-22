
from belief_base import BeliefBase
from belief_revision import revise
from resolution import pl_resolution



def main():
    bb = BeliefBase()
    bb.add_belief("A|B")
    bb.add_belief("~B|C")
    bb.add_belief("~C")

    print("\n--- Belief Base BEFORE revision ---")
    bb.display_beliefs()

    revised_bb = revise(bb, "~A")

    print("\n--- Belief Base AFTER revision with φ = ~A ---")
    revised_bb.display_beliefs()

    # After displaying revised beliefs
    print("Consistent after revision:", not pl_resolution(
        set(map(str, revised_bb.get_beliefs())), 'False'))

if __name__ == "__main__":
    main()
