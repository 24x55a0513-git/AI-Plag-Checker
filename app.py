import os

print("=" * 60)
print("APP:", os.path.abspath(__file__))
print("=" * 60)
from flask import Flask, render_template, request
from flask import send_from_directory
from engine.preprocessor import preprocess_code
import os

from engine.detector import detect_plagiarism
from utils.highlight import highlight_matches
from utils.report import generate_report
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download/<filename>")
def download_pdf(filename):
    return send_from_directory(
        "static",
        filename,
        as_attachment=True
    )


@app.route("/compare", methods=["POST"])
def compare():

    file1 = request.files["file1"]
    file2 = request.files["file2"]

    compare_mode = request.form.get("compare_mode", "complete")

    path1 = os.path.join(app.config["UPLOAD_FOLDER"], file1.filename)
    path2 = os.path.join(app.config["UPLOAD_FOLDER"], file2.filename)

    file1.save(path1)
    file2.save(path2)

    with open(path1, "r", encoding="utf-8", errors="ignore") as f:
        original_code1 = f.read()

    with open(path2, "r", encoding="utf-8", errors="ignore") as f:
        original_code2 = f.read()

    # Detect plagiarism
    result = detect_plagiarism(
        original_code1,
        original_code2,
        compare_mode
    )

    similarity = result["overall"]
    token_similarity = result["token"]
    ast_score = result["ast"]
    cfg_score = result["cfg"]
    complexity_score = result["complexity"]
    risk = result["risk"]
    recommendation = result["recommendation"]
    clone_type = result["clone_type"]

    # Code to display
    if compare_mode == "clean":
        display_code1 = preprocess_code(original_code1)
        display_code2 = preprocess_code(original_code2)
    else:
        display_code1 = original_code1
        display_code2 = original_code2

    # Generate PDF
    pdf = generate_report(
        file1.filename,
        file2.filename,
        similarity,
        token_similarity,
        ast_score,
        cfg_score,
        complexity_score,
        clone_type,
        risk,
        recommendation
    )

    return render_template(
        "result.html",

        similarity=similarity,
        token_similarity=token_similarity,
        ast_score=ast_score,
        cfg_score=cfg_score,
        complexity_score=complexity_score,

        risk=risk,
        recommendation=recommendation,
        clone_type=clone_type,

        file1=file1.filename,
        file2=file2.filename,

        code1=display_code1.splitlines(),
        code2=display_code2.splitlines(),

        pdf_path=pdf
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)