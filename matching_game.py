import tkinter as tk
from tkinter import messagebox
import random

# Define words and their definitions
words_definitions = {
    "Algorithm": "A set of rules or instructions given to an AI system to help it learn or solve problems. In the context of bias and equity, how these rules are defined and applied can lead to biased outcomes if not properly managed.",
    "Artificial Intelligence (AI)": "The simulation of human intelligence in machines that are programmed to think and learn. AI can inadvertently perpetuate biases present in the data used to train it.",
    "Bias (Algorithmic Bias)": "Systematic and repeatable errors in a computer system that create unfair outcomes, such as privileging one arbitrary group over another. This can be due to biased data, flawed model design, or other factors.",
    "Black Box": "A term used to describe complex AI systems where the decision-making process is not transparent or understandable to humans. This opacity can hide biased outcomes and make it difficult to correct them.",
    "Data Ethics": "A field of study that focuses on the ethical implications of data collection, usage, and analysis, ensuring that practices are fair and respect individuals' rights and privacy.",
    "Data Set": "A collection of data used to train or test an AI model. If a data set is not representative of the population, it can introduce bias into the AI system.",
    "Discrimination": "Unfair or prejudicial treatment of different categories of people, often exacerbated by biased AI systems that reinforce existing societal inequalities.",
    "Ethical AI": "AI development and deployment practices that prioritize fairness, accountability, and transparency to ensure that AI benefits all users equally and does not perpetuate bias or inequality.",
    "Equity": "Ensuring fair treatment, opportunities, and outcomes for all individuals. In AI, this means developing systems that do not favor any group over another and actively work to counteract existing biases.",
    "Fairness": "The principle that AI systems should treat all individuals and groups equally, without bias or favoritism. This often involves ensuring diverse and representative data sets and applying rigorous testing for bias.",
    "Inclusive Design": "An approach to designing AI systems that actively considers and addresses the needs of diverse users, aiming to minimize bias and ensure equitable outcomes.",
    "Intersectionality": "A framework for understanding how various forms of social stratification, such as race, gender, and class, intersect to create unique dynamics of privilege and disadvantage that AI systems must account for to be truly equitable.",
    "Machine Learning (ML)": "A subset of AI where machines learn from data to improve their performance on a task. The quality and representativeness of the data are crucial to preventing biased outcomes.",
    "Model Auditing": "The process of examining and testing AI models to identify and address biases. This involves looking at the data, the algorithm, and the outcomes to ensure fairness and equity.",
    "Representation Bias": "Occurs when certain groups are underrepresented or misrepresented in the data used to train AI models, leading to biased predictions and decisions.",
    "Transparency": "The practice of making the workings of AI systems clear and understandable to users. This is essential for identifying and correcting biases.",
    "Unintended Consequences": "Outcomes of AI systems that were not anticipated by the designers, often negative and affecting certain groups disproportionately due to inherent biases in the system.",
    "White Box": "An AI system whose internal workings are visible and understandable to humans, making it easier to detect and correct biases."
}

class MatchingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Matching Game")

        self.logo = tk.Label(root, text="Matching Game Logo", font=("Helvetica", 24))
        self.logo.pack(pady=20)

        self.welcome_text = tk.Label(root, text="Welcome to the AI Matching Game!", font=("Helvetica", 16))
        self.welcome_text.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.cards = []
        self.first_card = None
        self.matches = 0
        self.words_definitions_list = list(words_definitions.items())
        self.display_cards()

    def display_cards(self):
        random.shuffle(self.words_definitions_list)
        cards_data = self.words_definitions_list[:5] + [(v, k) for k, v in self.words_definitions_list[:5]]
        random.shuffle(cards_data)

        for i, (text, key) in enumerate(cards_data):
            card = tk.Button(self.frame, text="Click to reveal", width=40, height=5, command=lambda i=i: self.reveal_card(i))
            card.grid(row=i//2, column=i%2, padx=10, pady=10)
            self.cards.append((card, text, key))

    def reveal_card(self, index):
        card, text, key = self.cards[index]
        card.config(text=text)
        if self.first_card:
            self.check_match(index)
        else:
            self.first_card = (index, key)

    def check_match(self, second_index):
        first_index, first_key = self.first_card
        second_key = self.cards[second_index][2]
        if first_key == second_key:
            self.cards[first_index][0].config(state="disabled")
            self.cards[second_index][0].config(state="disabled")
            self.matches += 1
            if self.matches == 5:
                self.next_round()
        else:
            self.root.after(1000, self.hide_cards, first_index, second_index)
        self.first_card = None

    def hide_cards(self, first_index, second_index):
        self.cards[first_index][0].config(text="Click to reveal")
        self.cards[second_index][0].config(text="Click to reveal")

    def next_round(self):
        self.matches = 0
        self.cards = []
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.display_cards()

if __name__ == "__main__":
    root = tk.Tk()
    game = MatchingGame(root)
    root.mainloop()

