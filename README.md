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
### Similarity Analysis
The application analyzes two source-code files using multiple techniques:

1. **Token Similarity (35%)** – Compares the tokens and code elements used in both programs.

2. **AST Similarity (25%)** – Compares the structural representation of both programs using Abstract Syntax Trees.

3. **Control-Flow Similarity (20%)** – Compares the program’s execution flow, such as loops, conditions, and branches.

4. **Code Complexity Similarity (10%)** – Compares the complexity and structural characteristics of both programs.

5. **AI Semantic Similarity (10%)** – Uses AI-based code embeddings to identify similarities in the meaning and functionality of the code.

The final plagiarism score combines **Token (35%), AST (25%), Control-Flow (20%), Complexity (10%), and AI semantic similarity (10%)**.
Additional rules adjust the score for very low/high similarity cases, and the final value is limited to **0–100%**.

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
