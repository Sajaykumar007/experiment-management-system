def evaluate_output(output: str, execution_time: float):
    score = 0
    quality = "Poor"

    if not output:
        score = 0
        quality = "Failed"
    elif len(output) < 20:
        score = 4
        quality = "Average"
    else:
        score = 8
        quality = "Good"

    performance = "Slow" if execution_time > 3 else "Normal"

    return {
        "score": score,
        "quality": quality,
        "performance": performance
    }
