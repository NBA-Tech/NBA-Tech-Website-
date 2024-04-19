from flask import Flask, render_template,jsonify,request
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
    service_type=request.args.get('type')
    with open('Data/services.json', 'r') as f:
        data = json.load(f)
    return render_template('services_prod.html',service_data={"services":data,"type":service_type})
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404  

@app.route('/gallery')
def gallery():
    with open('Data/project_details.json', 'r') as f:
        data = json.load(f)
    return render_template('gallery.html',project_data={"project":data,"length":len(data)})

@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=False)
