from flask import Flask, render_template, request
from time import time

app = Flask(__name__)

difficulty_levels = {
    'Easy': [
        "the solar system consists of the sun, moon, and planets.",
        "hard work is worthless for those who don't believe in themselves."
    ],
    'Medium': [
        "if you don't like the hand that fate has dealt you, fight for a new one.",
        "the moment people come to know love, they run the risk of carrying hate."
    ],
    'Hard': [
        "life is really simple, but we insist on making it complicated.",
        "in the middle of difficulty lies opportunity."
    ]
}

def compare(test, user_input):
    error = 0
    right = 0
    for i in range(len(test)):
        try:
            if test[i] != user_input[i]:
                error += 1
            elif test[i] == user_input[i]:
                right += 1
        except IndexError:
            error += 1

    total_chars = len(test)
    accuracy = (right / total_chars) * 100

    return error, accuracy, right


def calculate_speed(test, user_input, start_time):
    end_time = time()
    time_taken = end_time - start_time
    minutes = time_taken / 60

    try:
        words_typed = len(user_input.split())
        speed = words_typed / minutes
        speed = round(speed)
    except ZeroDivisionError:
        speed = 0

    error_count, accuracy, correct_count = compare(test, user_input)

    return {
        'test': test,
        'speed': speed,
        'accuracy': round(accuracy),
        'errors': error_count
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        difficulty = request.form['difficulty']
        test = difficulty_levels.get(difficulty)
        if test:
            test = test[0]
            start_time = time()
            return render_template('index.html', test=test, start_time=start_time, difficulty_levels=difficulty_levels)

    return render_template('index.html', difficulty_levels=difficulty_levels)


@app.route('/play', methods=['POST'])
def play():
    test = request.form['test']
    start_time = float(request.form['start_time'])
    user_input = request.form['user_input']

    result = calculate_speed(test, user_input, start_time)

    return render_template('result.html', **result, difficulty_levels=difficulty_levels)


if __name__ == '__main__':
    app.run(debug=True)
