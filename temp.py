from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


def process_data(data):
    
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_alphabet = max(alphabets, key=lambda x: x.lower()) if alphabets else []
    return numbers, alphabets, highest_alphabet


@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        print(data)
        full_name = "padala_asish_manoj_reddy" 
        dob = "28052004" 

        numbers, alphabets, highest_alphabet = process_data(data)
        
        response = {
            "is_success": True,
            "user_id": f"{full_name}_{dob}",
            "email": "asishmanoj_padala@srmap.edu.in",
            "roll_number": "AP21110011239",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200

    except Exception as e:
        response = {
            "is_success": False,
            "error": str(e)
        }
        return jsonify(response), 400


@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

