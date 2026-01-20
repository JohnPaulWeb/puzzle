import random
import time

class puzzle:
    def __init__(self):
        self.player_inventory = []
        self.current_room = 0
        self.rooms_completed = 0
        self.game_over = False
        self.player_name = ""

        def display_title(self):
            print("\n" + "="*60)
            print("    Chambers of Mystical Enchantment".center(60))
            print("        A Fantasy Puzzle Adventure".center(60))
            print("="*60 + "\n")

            def get_player_name(self):
                self.player_name = input("Enter your adventurer's name: ").strip() or "Brave Soul"
                print(f"\nWelcome, {self.player_name}! Your quest begins now...\n")

                def puzzle_riddler(self):
                    """Room 1: Answer riddles to proceed."""
                    print("\n[Room 1: The Riddler's Challenge]")
                    print("-" * 40)
                    print("An ancient sphinx blocks your path and poses a riddle.")
                    print("Answer its riddles correctly to pass.\n")

                    riddles = [
                        {
                            "question": "I have cities, but no houses; forests, but no trees; and rivers, but no water. What am I?",
                            "answer": "map",
                            "hint": "It's something you use to navigate."
                        },
                        {
                            "question": "What has keys but can't open locks?",
                            "answer": "piano",
                            "hint": "It's a musical instrument."
                        },
                        {
                            "question": "What can travel around the world while staying in the same spot?",
                            "answer": "stamp",
                            "hint": "It's something you put on an envelope."
                        }
                    ]

                    correct = 0
                    for i, riddle in enumerate(riddles, 1):
                        print(f"Riddle {i}: {riddle['question']}")
                        hint_used = False

                        for attempt in range(2):
                            if attempt == 1 and not hint_used:
                                use_hint = input("Would you like a hint? (yes/no): ").lower().strip()
                                if use_hint == "yes":
                                    print(f"Hint: {riddle['hint']}\n")
                                    hint_used = True

                                    answer = input("Your answer: ").strip().lower()
                                    if answer == riddle['answer']:
                                        print("Correct!\n")
                                        correct += 1
                                        break
                                    else:
                                        if attempt == 0:
                                            print("Incorrect. Try again.\n")
                                        else:
                                            print(f"Incorrect. The correct answer was: {riddle['answer']}\n")

                                            if correct >= 2:
                                                print("The sphinx bows and grants you a Crystal Key!")
                                                self.player_inventory.append("Crystal Key")
                                                return True
                                            else:
                                                print("The sphinx refuses to let your pass.")
                                                return False

                                                def puzzle_logic_sequence(self):
                                                    """Room 2: Solve a logic sequence to proceed."""
                                                    print("\n[Room 2: The Logic Chamber]")
                                                    print("-" * 40)
                                                    print("Glowing stones on the floor form a pattern.")
                                                    print("Complete the sequence to unlock the door.\n")

                                                    sequences = [
                                                        {
                                                            "sequence": [12, 4, 6, 8],
                                                            "options": ["9", "10", "11", "12"],
                                                            "correct": 1,
                                                            "explanation": "Each number increases by 2."
                                                        },
                                                        {
                                                            "sequence": [3, 9, 27, 81],
                                                            "options": ["162", "243", "324", "405"],
                                                            "correct": 1,
                                                            "explanation": "Each number is multiplied by 3."
                                                        }
                                                    ]



                                                    selected = random.choice(sequences)
                                                    print(f"Sequence: {selected['sequence']} ...")
                                                    print("What comes next?\n")

                                                    for i, option in enumerate(selected['options'], 1):
                                                        print(f"{i}. {option}")

                                                        choice = input("\nYour Choice (1-4): ").strip()

                                                        try:
                                                            choice_num = int(choice) - 1
                                                            if 0 <= choice_num < 4:
                                                                if choice_num == selected['correct']:
                                                                    print(f"\nCorrect! {selected['explanation']}")
                                                                    self.player_inventory.append("Enchanted Compass")
                                                                    return True
                                                                else:
                                                                    print(f"\nIncorrect. {selected['explanation']}")
                                                                    return False
                                                                except ValueError:
                                                                    pass

                                                                print("Invalid input")
                                                                return False
                                                            
                                                            def puzzle_memory_game(self):
                                                                """Room 3: Memory matching Puzzle"""
                                                                print("\n[Room 3: The Memory Maze]")
                                                                print("-" * 40)
                                                                print("Magical runes appear, then disappear")
                                                                print("Remember the pattern!\n")

                                                                runes = ['⊕', '⊙', '⊗', '⊘']
                                                                pattern = random.sample(runes, 3)

                                                                print("Memorize this pattern:")
                                                                print(" ".join(pattern))
                                                                time.sleep(3)

                                                                print("\n" * 50)

                                                                print("Room 3: The Memory Sanctum")
                                                                print("The runes have vanished! Recreate the pattern.\n")

                                                                for attempt in range(2):
                                                                    print("Enter the runes in order, (space-separated):")
                                                                    user_input = input("Your pattern: ").strip().split()

                                                                     if len(user_input) == 3 and user_input == pattern:
                                                                        print("\nYou mastered the pattern! A hidden chest appears")
                                                                        self.player.inventory.append("Mystic Amulet")
                                                                        return True
                                                                else:
                                                                    if attempt == 0:
                                                                        print("That's not quite right. Try again.\n")
                                                                    else:
                                                                        print(f"\nThe correct pattern was: {' '.join(pattern)}")
                                                                        return False
                                                                    
                                                                    return False
                                                                def puzzle_word_ladder(self):
                                                                    """Room 4: Word Transformation Puzzle"""
                                                                    print("\n[Room 4: The Word Tower")
                                                                    print("-" * 40)
                                                                    print("Transform one word into another by changing.")
                                                                    print("one letter at a time. Each step must be a valid word.\n")

                                                                    puzzle = [
                                                                        {"start": "FIRE", "end": "WATER", "hint": "Start with Fire, try changing letters to reach Water"},
                                                                        {"start": "GOOD", "end": "EVIL", "hint": "Start with Good, try changing letters to reach Evil"}
                                                                    ]

                                                                    puzzle = random.choice(puzzles)
                                                                    print(f"Transform {puzzle['start']} → {puzzle['end']}")
                                                                    print(f"Hint: {puzzle['hint']}\n")
                                                                    

                                                                    solution_attempt = input("Enter your solution (steps separated by spaces): ").upper().strip()
                                                                    steps = solution_attempt.split()

                                                                    if len(steps) >= 2 and steps[0] == puzzle['start'] and steps[-1] == puzzle['end']:
                                                                        print("\nYou found a path! the Tower rumbles and settles")
                                                                        self.player_inventory.append("Ancient Scroll")
                                                                        return True
                                                                    else:
                                                                        print(f"\nExample solution might be: {puzzle['start']} → FIER → TIER → TIAR → TEAR → SEAR → WEAR → WARE → WARD → WART → WART → WART → WART... (Note: this is a hard puzzle)")
                                                                        return False
                                                                    

                                                                    def display_status(self):
                                                                        print(f"\n[Status] Rooms Completed: {self.rooms_completed}/4")
                                                                        print(f"[Inventory] {', '.join(self.player_inventory) if self.player_inventory else 'Empty'}")
                                                                        priint("-" * 40)

                                                                        def play_game(self):
                                                                            self.display_title()
                                                                            self.get_player_name()

                                                                            rooms = [
                                                                                self.puzzle_riddler,
                                                                                self.puzzle_logic_sequence,
                                                                                self.puzzle_memory_game,
                                                                                self.puzzle_word_ladder
                                                                            ]

                                                                            for room_func in room:
                                                                                self.display_status()

                                                                                if room_func():
                                                                                    self.rooms_completed += 1
                                                                                    print("\nYou proceed to the next chamber...")
                                                                                else:
                                                                                    print("\nYou must try again")
                                                                                    retry = input("Try this puzzle again? (yes/no): ").lower().strip()
                                                                                    if retry == "yes":
                                                                                        if room_func():
                                                                                            self.rooms_completed += 1
                                                                                            print("\nYou proceed to the next chamber...")
                                                                                        else:
                                                                                            print("You're force to retreat")
                                                                                            break
                                                                                    else:
                                                                                         print("You're force to retreat")
                                                                                            break
                                                                                    
                                                                                    self.display_ending()

                                                                                    def display_ending(self):
                                                                                        print("\n" + "="*60)