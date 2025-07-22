from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Example poll data
poll = {
    "question": "In 2019, approximately what percentage of violent crimes were solved (i.e., cleared) by police?",
    "options": ["A: 22%", "B: 46%", "C: 61%", "D: 83%"],
    "votes": [0, 0, 0, 0]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected = request.form.get("option")
        if selected is not None:
            try:
                choice = int(selected)
                if 0 <= choice < len(poll["votes"]):
                    poll["votes"][choice] += 1
                    return redirect(url_for("results"))
            except ValueError:
                pass  # Option wasn't an integer; ignore gracefully
        # If we reach here, something went wrong with submission
        return render_template("index.htm", poll=poll, error="Please select a valid option.")
    return render_template("index.htm", poll=poll)

@app.route("/results")
def results():
    total_votes = sum(poll["votes"])
    return render_template("results.htm", poll=poll, total=total_votes)

if __name__ == "__main__":
    app.run()

print(request.form)
