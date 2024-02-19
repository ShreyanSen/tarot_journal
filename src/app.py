from flask import Flask
from random import choice

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <form method="post" action="/generate">
        <button type="submit">Generate Random Text</button>
    </form>
    '''


# Sample data for demonstration
random_text_options = [
    "Lorem ipsum dolor sit amet",
    "Consectetur adipiscing elit",
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
]

@app.route('/generate', methods=['POST'])
def generate_text():
    random_text = choice(random_text_options)
    return random_text


if __name__ == '__main__':
    app.run(debug=True)
