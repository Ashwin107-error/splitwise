from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "u1": {"name": "User1", "balance": 0},
    "u2": {"name": "User2", "balance": 0},
    "u3": {"name": "User3", "balance": 0},
    "u4": {"name": "User4", "balance": 0},
}

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    paid_by = data.get('paid_by')
    amount = float(data.get('amount'))
    no_of_people = len(data.get('users'))
    owes = data.get('owes')
    split_type = data.get('split')

    response = []
    
    share_per_person = amount / no_of_people

    for user_id in data.get('users'):
        if split_type == "equally":
            if user_id != paid_by:
                users[user_id]['balance'] += share_per_person
                users[paid_by]['balance'] -= share_per_person
                response.append(f"{user_id} owes Rs {share_per_person} to {paid_by}")
        else:
            if user_id != paid_by:
                users[user_id]['balance'] += owes[user_id]
                users[paid_by]['balance'] -= owes[user_id]
                response.append(f"{user_id} owes Rs {owes[user_id]} to {paid_by}")

    return jsonify({"message": "Expense added and balances updated successfully.", "balance": response})

@app.route('/balances', methods=['GET'])
def get_balances():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
