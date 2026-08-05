def risk_analysis(score):

    if score >= 90:
        return (
            "Very High 🔴",
            "The submitted code is almost identical to the reference code. Strong plagiarism suspected."
        )

    elif score >= 70:
        return (
            "High 🟠",
            "Significant similarity detected. Manual verification is recommended."
        )

    elif score >= 50:
        return (
            "Medium 🟡",
            "Moderate similarity found. Review the matching sections carefully."
        )

    elif score >= 30:
        return (
            "Low 🟢",
            "Only minor similarities were detected."
        )

    else:
        return (
            "Very Low ⚪",
            "No meaningful plagiarism detected."
        )