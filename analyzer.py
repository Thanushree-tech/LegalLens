import re


def analyze_text(text):
    risks = []

    rules = {
        "penalty": {
            "title": "Penalty",
            "explanation": "This clause may require you to pay an additional amount if a specified condition is not met."
        },
        "termination": {
            "title": "Termination",
            "explanation": "This clause describes when the agreement can be ended and may contain conditions or notice requirements."
        },
        "liability": {
            "title": "Liability",
            "explanation": "This clause deals with responsibility for losses, damages, or other problems."
        },
        "non-refundable": {
            "title": "Non-Refundable",
            "explanation": "This means that money paid under this condition may not be returned."
        },
        "confidential": {
            "title": "Confidentiality",
            "explanation": "This clause requires certain information to be kept private or restricts how it can be shared."
        },
        "indemnify": {
            "title": "Indemnification",
            "explanation": "This may require one party to compensate the other for specified losses, claims, or damages."
        },
        "interest": {
            "title": "Interest / Additional Charge",
            "explanation": "This clause mentions interest or an additional charge. Check the rate and conditions carefully."
        }
    }

    # Split the extracted document into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    for keyword, details in rules.items():

        for sentence in sentences:

            if keyword in sentence.lower():

                clean_sentence = " ".join(sentence.split())

                # Avoid showing the same keyword twice
                already_found = any(
                    item["keyword"] == keyword
                    for item in risks
                )

                if not already_found:
                    risks.append({
                        "keyword": keyword,
                        "title": details["title"],
                        "clause": clean_sentence[:500],
                        "explanation": details["explanation"]
                    })

                break

    return risks