from flask import Flask, render_template
from src.tarot_deck import TarotDeck

app = Flask(__name__)

"""
@app.route('/')
def home():
    return '''
    <form method="post" action="/generate">
        <button type="submit">Generate Random Text</button>
    </form>
    '''
"""
@app.route('/')
def home():
    return render_template('index.html')


# Is this the right place to put this?
deck = TarotDeck()



@app.route('/draw', methods=['GET'])
def generate_text():
    deck.draw()
    card = deck.card
    prompt = deck.prompt
    return render_template('draw.html', card=card, prompt=prompt)
    #return deck.prompt


if __name__ == '__main__':
    app.run(debug=True)
