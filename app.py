from flask import Flask, request, jsonify

# initialize app
app = Flask(__name__)


#a route that handles all calculator operations
@app.route('/calculator/<operation>', methods=['POST'])
def calculator(operation):
    if operation == "Addition":
        num1 = (int)(request.headers['num1'])
        num2 = (int)(request.headers['num2'])
        result = num1 + num2
    if operation == "Subtraction":
        num1 = (int)(request.headers['num1'])
        num2 = (int)(request.headers['num2'])
        result = num1 - num2
    if operation == "Multiplication":
        num1 = (int)(request.headers['num1'])
        num2 = (int)(request.headers['num2'])
        result = num1 * num2
    if operation == "Division":
        num1 = (int)(request.headers['num1'])
        num2 = (int)(request.headers['num2'])
        result = num1 / num2
    return jsonify(result)


# Running the server..eh
if __name__ == '__main__':
    app.run(debug=True)