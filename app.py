from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def website():  # put application's code here
    #return 'Hello World!'
    # htps://www.geeksforgeeks.org/how-to-serve-static-files-in-flask/
    message = "Hello, World"
    return render_template('index.html',
                           message=message)

# https://studygyaan.com/flask/best-folder-and-directory-structure-for-a-flask-project
# gunicorn


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
