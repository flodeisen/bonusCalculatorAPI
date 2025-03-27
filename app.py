import yaml
from flask import Flask, request, jsonify
from bonus_calculator import BonusCalculator
from datetime import datetime
from dateutil.parser import parse

app = Flask(__name__)

def load_bonus_rules():
    with open('bonus_rules.yaml', 'r') as file:
        return yaml.safe_load(file)
    
@app.route('/calculate_bonus', methods = ['POST'])
def calculate_bonus():
    data = request.json
    transaction_amount = data.get('transaction_amount')
    timestamp = parse(data.get('timestamp'))
    customer_status = data.get('customer_status')

    rules = load_bonus_rules()
    calculator = BonusCalculator(rules)

    result = calculator.calculate(
        amount=transaction_amount,
        timestamp=timestamp,
        customer_status=customer_status
    )

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
