from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def Home():
    return render_template('Index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)