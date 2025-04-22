
import random
from belief_base import BeliefBase
from belief_revision import revise

colors = ['R', 'G', 'B']
code_length = 2
all_codes = [''.join(p) for p in [a + b for a in colors for b in colors]]

def generate_secret_code():
    return random.choice(all_codes)

def get_feedback(secret, guess):
    # Return (black, white): black = correct pos+color, white = correct color wrong pos
    black = sum(s == g for s, g in zip(secret, guess))
    secret_counts = {c: secret.count(c) for c in colors}
    guess_counts = {c: guess.count(c) for c in colors}
    white = sum(min(secret_counts.get(c, 0), guess_counts.get(c, 0)) for c in colors) - black
    return black, white

def formula_from_feedback(guess, feedback):
    black, white = feedback
    invalids = []
    for code in all_codes:
        fb = get_feedback(code, guess)
        if fb != feedback:
            invalids.append(code)
    return invalids  # these will be eliminated (¬code)

def mastermind_ai():
    print("🎯 Mastermind AI (2-color, RGB, belief-revision-based)")
    secret = generate_secret_code()
    print("🧪 Secret code generated. Let AI find it.")

    bb = BeliefBase()
    for code in all_codes:
        bb.add_belief(code)

    attempts = 0
    found = False

    while not found:
        options = sorted(map(str, bb.get_beliefs()))
        if not options:
            print("❌ No possible codes left! Something went wrong.")
            break

        guess = options[0]  # naive: always choose the first valid code
        attempts += 1
        print(f"🤖 Attempt {attempts}: Guess = {guess}")

        fb = get_feedback(secret, guess)
        print(f"🔁 Feedback: {fb[0]} black, {fb[1]} white")

        if fb == (2, 0):
            print(f"✅ AI found the code: {guess} in {attempts} attempts!")
            found = True
            break

        # Build ¬invalid_code for all codes that don't match the feedback
        for invalid in formula_from_feedback(guess, fb):
            bb.remove_belief(invalid)

if __name__ == "__main__":
    mastermind_ai()
