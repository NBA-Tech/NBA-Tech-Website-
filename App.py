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

@app.route('/services')
def services():
    with open('Data/services.json', 'r') as f:
        data = json.load(f)
    print(data)
    return render_template('services_prod.html',service_data={"services":data,"type":"product_dev"})
@app.route('/gallery')
def gallery():
    with open('Data/project_details.json', 'r') as f:
        data = json.load(f)
    
    
    return render_template('gallery.html',project_data={"project":data,"length":len(data)})
if __name__ == '__main__':
    app.run(debug=True)
