from flask import Flask, render_template, request
from extractor import extract_text
from analyzer import analyze_text
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        uploaded_file = request.files.get("document")

        if uploaded_file and uploaded_file.filename:

            filename = uploaded_file.filename
            uploaded_file.save(filename)

            text = extract_text(filename)

            if text.startswith("Error"):
                result = text

            else:
                risks = analyze_text(text)

                if not risks:
                    result = (
                        "NO COMMON RISKY CLAUSES FOUND\n\n"
                        "This basic scan did not detect any of the "
                        "currently supported risk terms."
                    )

                else:
                    result = "POTENTIAL RISKY CLAUSES FOUND\n\n"

                    for risk in risks:
                        result += f"⚠ {risk['title'].upper()}\n"
                        result += f"CLAUSE FOUND:\n{risk['clause']}\n\n"
                        result += f"EXPLANATION:\n{risk['explanation']}\n\n"

            if os.path.exists(filename):
                os.remove(filename)

        else:
            result = "Please select a PDF or TXT file first."

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)