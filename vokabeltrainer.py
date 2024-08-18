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

# Neue Vokabel hinzufügen
def add_vocab(vocab):
    german_word = input("Gib das deutsche Wort ein: ").strip()
    italian_word = input("Gib die italienische Übersetzung ein: ").strip()
    vocab[german_word] = italian_word
    save_vocab(vocab)
    print(f"'{german_word} - {italian_word}' wurde hinzugefügt.")

# Vokabel abfragen
def quiz(vocab):
    if not vocab:
        print("Keine Vokabeln vorhanden. Bitte füge Vokabeln hinzu.")
        return
    
    german_word, italian_word = random.choice(list(vocab.items()))
    answer = input(f"Was ist die italienische Übersetzung für '{german_word}'? ").strip()

    if answer.lower() == italian_word.lower():
        print("Richtig!")
    else:
        print(f"Falsch! Die richtige Antwort ist '{italian_word}'.")

# Hauptmenü
def main():
    vocab = load_vocab()

    while True:
        print("\nVokabeltrainer Menü")
        print("1. Neue Vokabel hinzufügen")
        print("2. Vokabel abfragen")
        print("3. Beenden")
        choice = input("Wähle eine Option (1/2/3): ").strip()

        if choice == '1':
            add_vocab(vocab)
        elif choice == '2':
            quiz(vocab)
        elif choice == '3':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte versuche es erneut.")

if __name__ == '__main__':
    main()
