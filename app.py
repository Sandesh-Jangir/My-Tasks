from pydoc import text
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Tasks.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.text}"

@app.route("/", methods=['GET', 'POST'])
def Home():
    if request.method=="POST":
        in_task = Task(text=request.form['task'])
        db.session.add(in_task)
        db.session.commit()
    all_tasks = Task.query.all()
    return render_template('Index.html', tasks=all_tasks)

@app.route("/delete/<int:sno>")
def Delete(sno):
    to_rem = Task.query.filter_by(sno=sno).first()
    db.session.delete(to_rem)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=8000)