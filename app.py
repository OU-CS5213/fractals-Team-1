# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, render_template
  
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
@app.route('/', methods = ['GET'])
def main():
    return render_template('index.html')

@app.route('/<string:fractal_name>/<string:res>', methods = ['GET'])
def fractal_image(fractal_name,res):
    
    context = {
        'name':  fractal_name,
        'resolution': res,
    }
  
    return render_template('fractal.html', **context)
  
# driver function
if __name__ == '__main__':
    app.run(debug=True)