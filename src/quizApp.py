# app.py

from flask import Flask, render_template, request, session, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Set a secret key for session management

# Load the JSON data
with open('quiz_data_sorted.json', 'r') as f:
    quiz_data = json.load(f)

# # Define a function to extract the numeric part of the question number
# def extract_question_number(question):
#     return int(question["question_number"].replace("#", ""))

# # Sort the questions list based on the extracted numeric part of the question number
# sorted_questions = sorted(data["questions"], key=extract_question_number)

# # Update the JSON data with the sorted questions list
# data["questions"] = sorted_questions

# # Write the updated data back to the JSON file
# with open('quiz_data_sorted.json', 'w') as f:
#     json.dump(data, f, indent=4)


@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        num_questions = int(request.form.get("num_questions"))
        session["num_questions"] = num_questions
        session["current_question"] = 1
        session["user_answers"] = {}
        return redirect(url_for("question", question_number=1))
    return render_template("homepage.html")

@app.route("/question/<int:question_number>", methods=["GET", "POST"])
def question(question_number):
    if question_number > session["num_questions"]:
        return "Quiz completed! Thank you."
    
    question = quiz_data["questions"][question_number - 1]
    if request.method == "POST":
        user_answer = request.form.get("answer")
        session["user_answers"][question_number] = user_answer
        return redirect(url_for("question", question_number=question_number + 1))
    
    return render_template("question.html", question=question, question_number=question_number)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
