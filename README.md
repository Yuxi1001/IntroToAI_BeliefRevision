
Belief Revision System - Interactive Console
===========================================

📄 Description:
---------------
This is an interactive belief revision system implemented in Python. 
It allows you to build a belief base, revise it with new logical formulas, and inspect its contents interactively.

📁 Required Files:
------------------
- belief_base.py          # Handles storage and management of beliefs
- belief_revision.py      # Implements belief revision using resolution-based consistency
- resolution.py           # Your own resolution-based logical entailment checker
- main.py                 # Entry point for the interactive console

▶️ How to Run:
--------------
1. Make sure all the above files are in the same folder.
2. Open a terminal and navigate to that folder.
3. Run the following command:

   python main.py

📋 Menu Options:
----------------
1. Show current belief base
   - Displays all currently stored formulas.

2. Add belief
   - Allows you to enter a formula like: A|B, ~C, A>>B, etc.

3. Remove belief
   - Removes a formula by string match.

4. Revise belief base with a new formula
   - Applies belief revision using Partial Meet strategy and resolution-based consistency checking.

5. Exit
   - Exits the interactive system.

🧪 Example Formulas:
---------------------
- A
- B
- A|B           (A or B)
- ~C            (Not C)
- A>>B          (A implies B)   ← will be interpreted as A → B

📌 Notes:
---------
- Formulas are internally treated as strings and parsed using custom logic.
- Logical entailment and consistency are checked using your own resolution engine.

Enjoy debugging logic like a philosopher-logician-programmer!
