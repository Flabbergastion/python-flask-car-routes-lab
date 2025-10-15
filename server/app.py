from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Car models data
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def index():
    """Default route returning welcome message"""
    return 'Welcome to Flatiron Cars'

@app.route('/<model>')
def model_route(model):
    """Route for specific car model with validation"""
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'

if __name__ == '__main__':
    app.run(debug=True)
