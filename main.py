from flask import Flask, render_template, request, jsonify
from sentence_transformers import util

from model import Model

myModel = Model()

app = Flask(__name__)


def get_bot_response(userText):
    # Get user input
    user_input = (userText)

    # Find top 5 similar questions
    question_scores = util.semantic_search(myModel.bi_encoder.encode(user_input, convert_to_tensor=True),
                                           myModel.question_embeddings,
                                           top_k=5)
    top_questions_indices = [hits['corpus_id'] for hits in question_scores[0]]

    # Re-rank top questions with CrossEncoder
    cross_inp = [[user_input, myModel.questions[idx]] for idx in top_questions_indices]
    cross_scores = myModel.cross_encoder.predict(cross_inp)

    # Find the best match
    best_idx = top_questions_indices[cross_scores.argmax()]

    return "Fry: " + myModel.questions[best_idx]


@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message']

    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
