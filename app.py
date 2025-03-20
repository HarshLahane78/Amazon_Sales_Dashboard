from flask import Flask, render_template
from Python.visualization import save_plots

app = Flask(__name__)

@app.route('/')
def home():
     # Generate visualizations
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
