from flask import Flask, render_template_string, request

app = Flask(__name__)

variables = {
    "$MY_INT": False,
    "int4": True,
    "4int": False,
    "global": False,
    "my_int": True,
    "for_01": True,
    "MY_INT": True,
    "Another int": False,
    "another_int": True,
    "my-int": False
}

explanations = {
    "$MY_INT": "Invalid: Variable names can't start with '$'.",
    "int4": "Valid: Starts with a letter and contains only alphanumeric characters.",
    "4int": "Invalid: Variable names can't start with a number.",
    "global": "Invalid: 'global' is a reserved keyword in Python.",
    "my_int": "Valid: Uses only letters, digits, and underscores.",
    "for_01": "Valid: Uses valid characters and not a reserved word.",
    "MY_INT": "Valid: Uses valid characters.",
    "Another int": "Invalid: Contains a space.",
    "another_int": "Valid: Uses valid characters.",
    "my-int": "Invalid: Hyphens are not allowed in variable names."
}

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Python Variable Naming Quiz</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        .correct { color: green; }
        .wrong { color: red; }
        table, th, td { border: 1px solid black; border-collapse: collapse; padding: 8px; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h2>Python Variable Naming Quiz</h2>
    <form method="POST">
        <p>Select whether each variable name is Valid or Invalid:</p>
        <table>
            <tr>
                <th>Variable Name</th>
                <th>Your Answer</th>
                {% if submitted %}<th>Result</th><th>Explanation</th>{% endif %}
            </tr>
            {% for var, correct in variables.items() %}
            <tr>
                <td>{{ var }}</td>
                <td>
                    <select name="{{ var }}">
                        <option value="Valid" {% if answers[var] == "Valid" %}selected{% endif %}>Valid</option>
                        <option value="Invalid" {% if answers[var] == "Invalid" %}selected{% endif %}>Invalid</option>
                    </select>
                </td>
                {% if submitted %}
                <td class="{{ 'correct' if (correct and answers[var]=='Valid') or (not correct and answers[var]=='Invalid') else 'wrong' }}">
                    {{ "✅ Correct" if (correct and answers[var]=='Valid') or (not correct and answers[var]=='Invalid') else "❌ Wrong" }}
                </td>
                <td>{{ explanations[var] }}</td>
                {% endif %}
            </tr>
            {% endfor %}
        </table>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def quiz():
    submitted = False
    answers = {var: "" for var in variables}
    if request.method == "POST":
        submitted = True
        for var in variables:
            answers[var] = request.form.get(var, "")
    return render_template_string(html_template,
                                  variables=variables,
                                  explanations=explanations,
                                  answers=answers,
                                  submitted=submitted)

if __name__ == "__main__":
    app.run(debug=True)
