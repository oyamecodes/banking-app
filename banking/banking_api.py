from flask import Flask, request, jsonify
from database import Database
from transaction import Transaction

app = Flask(__name__)
db = Database()

@app.route('/create_account', methods=['POST'])
def create_account():
    data = request.json
    account_id = data['account_id']
    name = data['name']
    initial_balance = data.get('initial_balance', 0)
    try:
        account = db.create_account(account_id, name, initial_balance)
        return jsonify({"account_id": account.account_id, "name": account.name, "balance": account.get_balance()})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/balance/<account_id>', methods=['GET'])
def balance(account_id):
    try:
        account = db.get_account(account_id)
        return jsonify({"balance": account.get_balance()})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/transfer', methods=['POST'])
def transfer():
    data = request.json
    sender_id = data['sender_id']
    receiver_id = data['receiver_id']
    amount = data['amount']
    try:
        sender = db.get_account(sender_id)
        receiver = db.get_account(receiver_id)
        success = Transaction.transfer(sender, receiver, amount)
        if success:
            return jsonify({"message": "Transfer successful"})
        else:
            return jsonify({"error": "Transfer failed"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/transactions/<account_id>', methods=['GET'])
def transactions(account_id):
    try:
        account = db.get_account(account_id)
        return jsonify({"transactions": account.get_transactions()})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)