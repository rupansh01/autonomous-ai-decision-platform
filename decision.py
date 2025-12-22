# decision logic
def final_decision(severity, customer_type, past_complaints):
    if severity >= 8 and customer_type == "premium":
        return "AUTO_REFUND"

    if severity >= 6 and past_complaints > 3:
        return "ESCALATE"

    if severity < 4:
        return "REJECT"

    return "ESCALATE"
