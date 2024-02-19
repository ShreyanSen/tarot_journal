from flask import Flask
from src.tarot_deck import TarotDeck

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

# Is this the right place to put this?

deck = TarotDeck()



@app.route('/generate', methods=['POST'])
def generate_text():
    deck.draw()
    return deck.prompt


if __name__ == '__main__':
    app.run(debug=True)
