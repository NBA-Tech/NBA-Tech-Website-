from flask import Flask, render_template,jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('Data/project.json', 'r') as f:
        data = json.load(f)
    return render_template('index.html', project_data={"project":data,"length":len(data)})

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
