# AI Plagiarism Checker

An AI-powered Python web application for detecting plagiarism between two source-code files.

## Features

- Compare two source-code files
- Token-based similarity analysis
- AST-based similarity analysis
- Control Flow Graph (CFG) comparison
- Code complexity comparison
- AI-based semantic similarity using CodeBERT
- Clone type detection
- Plagiarism risk analysis
- Similarity score generation
- PDF plagiarism report
- Clean-code comparison mode
- Web interface built with Flask

## Technologies Used

- Python
- Flask
- Scikit-learn
- PyTorch
- Transformers
- CodeBERT
- NumPy
- ReportLab

## How It Works

The application analyzes two source-code files using multiple techniques:

1. Token similarity
2. AST similarity
3. Control-flow similarity
4. Code complexity similarity
5. AI semantic similarity

These scores are combined to generate an overall plagiarism score and risk level.

## Project Structure

```text
AI-Plag-Checker/
│
├── engine/
│   ├── ast_compare.py
│   ├── complexity.py
│   ├── control_flow.py
│   ├── embeddings.py
│   ├── clone_detector.py
│   ├── preprocessor.py
│   ├── risk.py
│   ├── scorer.py
│   └── token_similarity.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── script.js
│   └── style.css
│
├── utils/
│   ├── highlight.py
│   └── report.py
│
├── app.py
├── requirements.txt
└── README.md
