def predict_category(text):

    text = text.lower()

    if "payment" in text or "refund" in text:
        return "Payment Issue"

    elif "delivery" in text or "late" in text:
        return "Delivery Issue"

    elif "product" in text or "quality" in text:
        return "Product Issue"

    else:
        return "Other"