def detect_intent(text):

    text = text.lower()

    if "mass" in text:
        return "mass"

    elif "decay" in text:
        return "decay"

    elif "spin" in text:
        return "spin"

    elif "charge" in text:
        return "charge"

    elif "draw" in text or "visualize" in text:
        return "draw"

    elif "compare" in text:
        return "compare"
    elif "interaction" in text:
        return "interaction"
    elif "draw" in text or "visualize" in text:
        return "draw"

    else:
        return "full_info"