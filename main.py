import tkinter as tk
from tkinter import messagebox
import random

question_bank = {
    "General Knowledge": [
        {"question": "What is the smallest country in the world?", "options": ["Monaco", "Nauru", "Vatican City", "San Marino"], "answer": "Vatican City"},
        {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
        {"question": "What is the capital of Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Perth"], "answer": "Canberra"},
        {"question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
        {"question": "What is the currency of Japan?", "options": ["Yen", "Won", "Renminbi", "Dollar"], "answer": "Yen"},
        {"question": "Which country gifted the Statue of Liberty to the USA?", "options": ["UK", "France", "Germany", "Italy"], "answer": "France"},
        {"question": "What is the tallest mountain in the world?", "options": ["K2", "Everest", "Kilimanjaro", "Makalu"], "answer": "Everest"},
        {"question": "Which is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"},
        {"question": "What is the largest desert in the world?", "options": ["Sahara", "Antarctic", "Arctic", "Gobi"], "answer": "Antarctic"},
        {"question": "In what year did the Titanic sink?", "options": ["1912", "1905", "1898", "1921"], "answer": "1912"},
    ],
    "Science": [
        {"question": "What planet is known as the Red Planet?", "options": ["Mars", "Jupiter", "Saturn", "Venus"], "answer": "Mars"},
        {"question": "What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "HighText Transmission Protocol", "Hyper Tool Transfer Protocol", "HyperText Translate Program"], "answer": "HyperText Transfer Protocol"},
        {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Gd", "Go"], "answer": "Au"},
        {"question": "How many bones are in the human body?", "options": ["206", "205", "201", "200"], "answer": "206"},
        {"question": "What gas do plants absorb?", "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"], "answer": "Carbon Dioxide"},
        {"question": "What is H2O?", "options": ["Hydrogen", "Oxygen", "Water", "Salt"], "answer": "Water"},
        {"question": "What type of energy comes from the sun?", "options": ["Wind", "Solar", "Hydro", "Thermal"], "answer": "Solar"},
        {"question": "Who developed the theory of relativity?", "options": ["Newton", "Einstein", "Bohr", "Tesla"], "answer": "Einstein"},
        {"question": "Which part of the atom has a negative charge?", "options": ["Proton", "Neutron", "Electron", "Nucleus"], "answer": "Electron"},
        {"question": "How many legs does a spider have?", "options": ["6", "8", "10", "12"], "answer": "8"},
    ],
    "Python / Programming": [
        {"question": "What keyword is used to define a function in Python?", "options": ["function", "def", "fun", "define"], "answer": "def"},
        {"question": "Which of these is NOT a Python data type?", "options": ["tuple", "list", "map", "string"], "answer": "map"},
        {"question": "What does 'len()' return?", "options": ["Size", "Length", "Width", "Index"], "answer": "Length"},
        {"question": "Which symbol is used for comments in Python?", "options": ["//", "#", "/* */", "--"], "answer": "#"},
        {"question": "Which keyword is used for loops in Python?", "options": ["while", "repeat", "loop", "foreach"], "answer": "while"},
        {"question": "What does 'int' represent?", "options": ["Integer", "Interactive", "Interval", "Interpreter"], "answer": "Integer"},
        {"question": "Which Python library is used for data analysis?", "options": ["matplotlib", "pandas", "pygame", "requests"], "answer": "pandas"},
        {"question": "Which function is used to get user input?", "options": ["get()", "input()", "read()", "ask()"], "answer": "input()"},
        {"question": "What does IDE stand for?", "options": ["Integrated Design Engine", "Intelligent Debugger Editor", "Integrated Development Environment", "Interpreter Display Engine"], "answer": "Integrated Development Environment"},
        {"question": "Which Python keyword is used to handle errors?", "options": ["try", "catch", "error", "check"], "answer": "try"},
    ],
    "Movies & Pop Culture": [
        {"question": "Who directed 'Inception'?", "options": ["Steven Spielberg", "Christopher Nolan", "Quentin Tarantino", "James Cameron"], "answer": "Christopher Nolan"},
        {"question": "Which movie features a character named Jack Dawson?", "options": ["Titanic", "The Notebook", "Inception", "Avatar"], "answer": "Titanic"},
        {"question": "Which superhero is known as the 'Caped Crusader'?", "options": ["Superman", "Iron Man", "Batman", "Spider-Man"], "answer": "Batman"},
        {"question": "Who played Iron Man in the MCU?", "options": ["Chris Evans", "Chris Hemsworth", "Robert Downey Jr.", "Tom Holland"], "answer": "Robert Downey Jr."},
        {"question": "What is the name of Harry Potter's owl?", "options": ["Errol", "Hedwig", "Fawkes", "Crookshanks"], "answer": "Hedwig"},
        {"question": "Which movie starts with a young lion prince?", "options": ["Madagascar", "The Lion King", "Finding Nemo", "Shrek"], "answer": "The Lion King"},
        {"question": "In which year was the first Toy Story released?", "options": ["1995", "1999", "2001", "1992"], "answer": "1995"},
        {"question": "What is the name of the wizarding bank in Harry Potter?", "options": ["Gringotts", "Diagon", "Vaultor", "Magibank"], "answer": "Gringotts"},
        {"question": "Which actor voiced Woody in Toy Story?", "options": ["Tom Hanks", "Tim Allen", "Robin Williams", "Jim Carrey"], "answer": "Tom Hanks"},
        {"question": "Which sci-fi series features Spock?", "options": ["Star Wars", "Firefly", "Doctor Who", "Star Trek"], "answer": "Star Trek"},
    ],
    "Gaming": [
        {"question": "What game is known for 'It's dangerous to go alone! Take this.'?", "options": ["Zelda", "Mario", "Skyrim", "Minecraft"], "answer": "Zelda"},
        {"question": "Which company makes the PlayStation?", "options": ["Sony", "Microsoft", "Nintendo", "Sega"], "answer": "Sony"},
        {"question": "What is the main goal in Minecraft?", "options": ["Build", "Survive", "Craft", "Ender Dragon"], "answer": "Survive"},
        {"question": "Who is the main character of the Halo series?", "options": ["Master Chief", "Cortana", "Arbiter", "Noble Six"], "answer": "Master Chief"},
        {"question": "What game features the city of Los Santos?", "options": ["GTA V", "Watch Dogs", "Saints Row", "Cyberpunk"], "answer": "GTA V"},
        {"question": "In which game can you land at Tilted Towers and Pleasant Park?", "options": ["PUBG", "Call of Duty", "Fortnite", "Apex"], "answer": "Fortnite"},
        {"question": "What is the name of Mario's brother?", "options": ["Luigi", "Wario", "Toad", "Yoshi"], "answer": "Luigi"},
        {"question": "Which game lets you catch and train creatures called Pokémon?", "options": ["Digimon", "Yu-Gi-Oh", "Pokémon", "Monster Rancher"], "answer": "Pokémon"},
        {"question": "Which item restores health in most games?", "options": ["Shield", "Potion", "Crystal", "Ammo"], "answer": "Potion"},
        {"question": "What is the name of the blocky building game by Mojang?", "options": ["Terraria", "Minecraft", "Roblox", "Blockcraft"], "answer": "Minecraft"},
    ],
    "Memes": [
        {"question": "What Costco food item does Big Justice eat?", "options": ["Double-Chunk Chocolate Cookie", "Churro", "Chicken Bake", "Cheese Pizza"], "answer": "Chicken Bake"},
        {"question": "Which Italian brainrot character is a shark with blue shoes?", "options": ["Tralalero Tralala", "Brr Brr Patapim", "Bombardino Crocodilo", "Tung Tung Tung Sahur"], "answer": "Tralalero Tralala"},
        {"question": "Who is the GOAT?", "options": ["Michael Jordan", "LeBron James", "Shaq", "Kobe Bryant"], "answer": "LeBron James"},
        {"question": "What streamer is known for traveling to many countries and loving Ronaldo?", "options": ["Kai Cenat", "IShowSpeed", "Lacy", "Clix"], "answer": "IShowSpeed"},
        {"question": "What does 'kevin' mean?", "options": ["Something Good", "Something Bad", "Something Mid", "Something Evil"], "answer": "Something Bad"},
        {"question": "Who did Baby Gronk rizz up?", "options": ["Livvy Dunne", "Brody Joling", "Fanum", "LeBron"], "answer": "Livvy Dunne"},
        {"question": "What artist has come under fire for his actions online?", "options": ["Kendrick", "Justin Bieber", "Kanye", "Bad Bunny"], "answer": "Kanye"},
        {"question": "Which of the following categories does Brody Joling fall under?", "options": ["Unemployed", "Chopped", "Tall", "Nonchalant"], "answer": "Unemployed"},
        {"question": "What is impossible for a computer science student to do?", "options": ["Shower", "Get a j*b", "Touch Grass", "All of the above"], "answer": "All of the above"},
        {"question": "What word is based on charisma?", "options": ["Rizz", "Aura", "Gamer", "Frat Bro"], "answer": "Rizz"},
    ]
}

class QuizApp:
    """
    A class to create and manage a quiz game using Tkinter.

    Attributes:
        root (tk.Tk): The main Tkinter window.
        genre (str): The selected quiz genre.
        questions (list): List of questions for the current quiz.
        current_q (int): Index of the current question.
        player_score (int): The player's score.
        python_score (int): The computer's score.
        option_buttons (list): List of option button widgets.
        timer_label (tk.Label): Label widget for the timer.
        time_left (int): Seconds left for the current question.
        timer_id (int): ID for the timer event.
    """

    def __init__(self, root):
        """
        Initializes the QuizApp with the main window and sets up initial state.
        Builds the genre selection menu.
        """

        self.root = root
        self.genre = None
        self.questions = []
        self.current_q = 0
        self.player_score = 0
        self.python_score = 0
        self.option_buttons = []
        self.timer_label = None
        self.time_left = 15
        self.timer_id = None

        self.build_genre_menu()

    def build_genre_menu(self):
        """
        Clears the window and displays buttons for each quiz genre.
        Allows the user to select a genre to start the quiz.
        """
         
        self.clear_window()
        tk.Label(self.root, text="Choose a Quiz Genre:", font=("Helvetica", 16)).pack(pady=20)

        for genre in question_bank:
            btn = tk.Button(self.root, text=genre, width=30, font=("Helvetica", 14),
                            command=lambda g=genre: self.start_quiz(g))
            btn.pack(pady=5)

    def start_quiz(self, genre):
        """
        Starts a new quiz for the selected genre.
        Shuffles questions, resets scores, and builds the quiz UI.

        Args:
            genre (str): The selected quiz genre.
        """

        self.genre = genre
        self.questions = random.sample(question_bank[genre], len(question_bank[genre]))
        self.current_q = 0
        self.player_score = 0
        self.python_score = 0
        self.build_quiz_ui()
        self.next_question()

    def build_quiz_ui(self):
        """
        Clears the window and builds the quiz interface.
        Displays the question, timer, answer options, result, and score labels.
        """

        self.clear_window()

        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 16), wraplength=400)
        self.question_label.pack(pady=20)
        self.timer_label = tk.Label(self.root, text="Time Left: 15s", font=("Helvetica", 14), fg="blue")
        self.timer_label.pack(pady=5)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Helvetica", 14), width=40,
                            command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

    def next_question(self):
        """
        Loads the next question if available.
        Updates the question and options, resets result label, and starts the timer.
        If no more questions, ends the game.
        """

        if self.current_q < len(self.questions):
            q = self.questions[self.current_q]
            self.question_label.config(text=f"Q{self.current_q + 1}: {q['question']}")
            for i, opt in enumerate(q['options']):
                self.option_buttons[i].config(text=opt, state=tk.NORMAL)
            self.result_label.config(text="")
            self.score_label.config(text=f"You: {self.player_score}  |  Python: {self.python_score}")
            self.start_timer()
        else:
            self.end_game()

    def check_answer(self, selected):
        """
        Checks if the selected answer is correct.
        Updates scores, disables option buttons, and shows the result.
        Proceeds to the next question after a short delay.

        Args:
            selected (int): Index of the selected option button.
        """

        self.root.after_cancel(self.timer_id)
        correct = self.questions[self.current_q]['answer']
        chosen = self.option_buttons[selected]['text']

        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)

        if chosen == correct:
            self.result_label.config(text="✅ Correct!", fg="green")
            self.player_score += 1
        else:
            self.result_label.config(text=f"❌ Wrong! Answer: {correct}", fg="red")
            self.python_score += 1

        self.current_q += 1
        self.root.after(1500, self.next_question)
    
    def start_timer(self):
        """
        Initializes and starts the countdown timer for the current question.
        """

        self.time_left = 15
        self.update_timer()

    def update_timer(self):
        """
        Updates the timer label every second.
        If time runs out, marks the question as missed and moves to the next question.
        """

        self.timer_label.config(text=f"Time Left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.result_label.config(text="⏰ Time's up!", fg="orange")
            self.python_score += 1
            self.current_q += 1
            self.score_label.config(text=f"You: {self.player_score}  |  Python: {self.python_score}")
            self.root.after(1500, self.next_question)


    def end_game(self):
        """
        Displays the final score and result in a message box.
        Returns to the genre selection menu.
        """

        result = ""
        if self.player_score > self.python_score:
            result = "🎉 You beat Python! Humanity wins!"
        elif self.python_score > self.player_score:
            result = "🤖 Python wins! The robots are coming!"
        else:
            result = "😐 It's a tie. Suspicious..."

        messagebox.showinfo("Game Over", f"Final Score:\nYou: {self.player_score}\nPython: {self.python_score}\n\n{result}")
        self.build_genre_menu()

    def clear_window(self):
        """
        Removes all widgets from the main window.
        """
        
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
root.title("Are You Smarter Than A Python Program?")
root.geometry("600x500")
app = QuizApp(root)
root.mainloop()

