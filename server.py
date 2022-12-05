from flask import Flask, render_template,  request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'not really secret'


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")  # Return the string 'Hello World!' as a response


@app.route('/process', methods=['POST'])
def process_form():
    print("Got Post Info")
    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']

    return redirect('/result')

@app.route('/result')
def display_info():
    if not 'name' in session:
        session['name'] = 'Not Provided'
    if not 'comments' in session:
        session['comments'] = 'No Comments'

    return render_template("result.html", name=session['name'], locations=session['locations'], language=session['language'], comments=session['comments'])


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host='0.0.0.0')    # Run the app in debug mode.
