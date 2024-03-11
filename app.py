from flask import Flask, render_template, request, jsonify
import re
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    matches = []
    error_message = None

    if request.method == "POST":
        # Check if the form is submitted for regex matching
        if "test_string" in request.form and "regex_pattern" in request.form:
            test_string = request.form.get("test_string")
            regex_pattern = request.form.get("regex_pattern")

            print("Test String:", test_string)
            print("Regex Pattern:", regex_pattern)

            if test_string and regex_pattern:
                try:
                    matches = re.findall(regex_pattern, test_string)
                    print("Matches:", matches)
                except re.error:
                    error_message = "Invalid regular expression"

        # Check if the form is submitted for email validation
        elif "email" in request.form:
            email = request.form.get("email")
            is_valid = validate_email(email)
            return jsonify({"email": email, "valid": is_valid})

    return render_template("index.html", matches=matches, error_message=error_message)



def validate_email(email):
    # Regular expression for email validation
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(regex, email))

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
