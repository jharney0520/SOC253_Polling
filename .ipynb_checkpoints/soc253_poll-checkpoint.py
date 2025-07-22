from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Example poll data
poll = {
    "question": "In 2019, approximately what percentage of violent crimes were solved (i.e., cleared) by police?",
    "options": ["A: 22%", "46%", "61%", "83%"],
    "votes": [0, 0, 0, 0]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        choice = int(request.form.get("option"))
        poll["votes"][choice] += 1
        return redirect(url_for("results"))
    return render_template("index.htm", poll=poll)

@app.route("/results")
def results():
    total_votes = sum(poll["votes"])
    return render_template("results.htm", poll=poll, total=total_votes)

if __name__ == "__main__":
    app.run()
