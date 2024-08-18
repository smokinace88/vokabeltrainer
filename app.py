from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

VOCAB_FILE = 'vocab.json'

def load_vocab():
    try:
        with open(VOCAB_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_vocab(vocab):
    with open(VOCAB_FILE, 'w') as file:
        json.dump(vocab, file, ensure_ascii=False, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET'])
def quiz():
    vocab = load_vocab()
    if vocab:
        german_word, italian_word = random.choice(list(vocab.items()))
        return jsonify({"german_word": german_word, "italian_word": italian_word})
    return jsonify({"error": "No vocabulary available"}), 400

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    german_word = data.get('german_word')
    user_answer = data.get('user_answer')
    vocab = load_vocab()
    
    correct_answer = vocab.get(german_word, "").lower()
    if user_answer.strip().lower() == correct_answer:
        return jsonify({"result": "correct"})
    else:
        return jsonify({"result": "incorrect", "correct_answer": correct_answer})

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    german_word = data.get('german_word')
    italian_word = data.get('italian_word')
    vocab = load_vocab()
    
    if german_word and italian_word:
        vocab[german_word] = italian_word
        save_vocab(vocab)
        return jsonify({"success": True})
    return jsonify({"success": False}), 400

@app.route('/vocablist', methods=['GET'])
def vocab_list():
    vocab = load_vocab()
    return jsonify(vocab)

if __name__ == "__main__":
    app.run(debug=True)
