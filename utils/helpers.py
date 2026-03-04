import random

def get_risk_color(score):
    if score < 30:
        return "green"
    elif score < 70:
        return "orange"
    else:
        return "red"

def generate_financial_impact():
    return random.randint(10000, 100000)
