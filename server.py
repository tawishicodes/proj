from flask import Flask, jsonify, request, send_from_directory
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_url_path='', static_folder='.')

# Supabase configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Supabase headers
headers = {
    'apikey': SUPABASE_KEY,
    'Authorization': f'Bearer {SUPABASE_KEY}',
    'Content-Type': 'application/json',
    'Prefer': 'return=minimal'
}

@app.route('/')
def serve_static():
    return app.send_static_file('index.html')

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory('images', filename)

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('css', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('js', filename)

@app.route('/api/data', methods=['GET'])
def get_all_data():
    try:
        response = requests.get(
            f'{SUPABASE_URL}/rest/v1/SIX_data?select=*',
            headers=headers
        )
        return jsonify(response.json()), 200
    except Exception as e:
        print(f"Error in GET: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/data', methods=['POST'])
def add_data():
    try:
        data = request.json
        response = requests.post(
            f'{SUPABASE_URL}/rest/v1/SIX_data',
            headers=headers,
            json={
                'p_number': data['p_number'],
                'insta_1': data['insta_1'],
                'insta_2': data['insta_2'],
                'insta_3': data['insta_3']
            }
        )
        return jsonify({'message': 'Data added successfully'}), 201
    except Exception as e:
        print(f"Error in POST: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/data/<p_number>', methods=['GET'])
def get_data_by_phone(p_number):
    try:
        # Fetch record by phone number
        response = requests.get(
            f'{SUPABASE_URL}/rest/v1/SIX_data?select=*&p_number=eq.{p_number}',
            headers=headers
        )
        if response.json():
            return jsonify(response.json()[0]), 200
        return jsonify({'message': 'No data found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    # In production, don't use debug mode
    app.run(host='0.0.0.0', port=port, debug=False) 