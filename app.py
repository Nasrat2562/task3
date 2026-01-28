from flask import Flask, request, Response
import math
import os

app = Flask(__name__)

def is_natural(num):
    """Check if a string represents a natural number"""
    try:
        n = int(num)
        return n > 0
    except (ValueError, TypeError):
        return False

@app.route('/<path:email_path>')
def calculate_lcm(email_path):
    """LCM calculation endpoint"""
    x = request.args.get('x')
    y = request.args.get('y')
    
    # Validate inputs
    if not is_natural(x) or not is_natural(y):
        return Response('NaN', mimetype='text/plain')
    
    # Calculate LCM
    x_int = int(x)
    y_int = int(y)
    lcm_result = abs(x_int * y_int) // math.gcd(x_int, y_int)
    
    return Response(str(lcm_result), mimetype='text/plain')

@app.route('/health')
def health_check():
    return 'Server is awake!'

@app.route('/')
def home():
    return 'LCM Calculator is running. Use /your_email_path?x=num&y=num'

if __name__ == '__main__':
    app.run(debug=True)