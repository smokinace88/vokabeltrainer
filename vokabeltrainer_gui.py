import tkinter as tk
from tkinter import messagebox
import json
import random

# Datei zum Speichern der Vokabeln
VOCAB_FILE = 'vocab.json'

# Vokabeln laden oder ein leeres Dictionary erstellen
def load_vocab():
    try:
        with open(VOCAB_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Vokabeln speichern
def save_vocab(vocab):
    with open(VOCAB_FILE, 'w') as file:
        json.dump(vocab, file, ensure_ascii=False, indent=4)

# Vokabeltrainer-Klasse
class VocabTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deutsch-Italienisch Vokabeltrainer")

        # Laden der Vokabeln
        self.vocab = load_vocab()

        # GUI-Elemente
        self.create_widgets()

    def create_widgets(self):
        # Hinzufügen von Vokabeln
        self.label_add = tk.Label(self.root, text="Neue Vokabel hinzufügen:")
        self.label_add.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_german = tk.Entry(self.root, width=20)
        self.entry_german.grid(row=1, column=0, padx=10, pady=5)

        self.entry_italian = tk.Entry(self.root, width=20)
        self.entry_italian.grid(row=1, column=1, padx=10, pady=5)

        self.btn_add = tk.Button(self.root, text="Hinzufügen", command=self.add_vocab)
        self.btn_add.grid(row=1, column=2, padx=10, pady=5)

        # Abfragen von Vokabeln
        self.label_quiz = tk.Label(self.root, text="Vokabel abfragen:")
        self.label_quiz.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.label_question = tk.Label(self.root, text="", font=("Arial", 12))
        self.label_question.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

        self.entry_answer = tk.Entry(self.root, width=20)
        self.entry_answer.grid(row=4, column=0, padx=10, pady=5)

        self.btn_quiz = tk.Button(self.root, text="Überprüfen", command=self.check_answer)
        self.btn_quiz.grid(row=4, column=1, padx=10, pady=5)

        self.btn_new_quiz = tk.Button(self.root, text="Neue Vokabel", command=self.new_quiz)
        self.btn_new_quiz.grid(row=4, column=2, padx=10, pady=5)

        # Erste Quizfrage generieren
        self.new_quiz()

    def add_vocab(self):
        german_word = self.entry_german.get().strip()
        italian_word = self.entry_italian.get().strip()

        if german_word and italian_word:
            self.vocab[german_word] = italian_word
            save_vocab(self.vocab)
            messagebox.showinfo("Erfolg", f"'{german_word} - {italian_word}' wurde hinzugefügt.")
            self.entry_german.delete(0, tk.END)
            self.entry_italian.delete(0, tk.END)
        else:
            messagebox.showwarning("Fehler", "Bitte beide Felder ausfüllen.")

    def new_quiz(self):
        if not self.vocab:
            self.label_question.config(text="Keine Vokabeln vorhanden.")
            return

        self.german_word, self.italian_word = random.choice(list(self.vocab.items()))
        self.label_question.config(text=f"Was ist die italienische Übersetzung für '{self.german_word}'?")
        self.entry_answer.delete(0, tk.END)

    def check_answer(self):
        answer = self.entry_answer.get().strip()

        if answer.lower() == self.italian_word.lower():
            messagebox.showinfo("Richtig!", "Das ist korrekt!")
        else:
            messagebox.showerror("Falsch", f"Die richtige Antwort ist '{self.italian_word}'.")

        self.new_quiz()

# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = VocabTrainerApp(root)
    root.mainloop()
