from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from preprocessing import preprocess_image, enhance_image
from model import analyze_image
from utils import allowed_file

app = Flask(__name__)
UPLOAD_FOLDER = './static/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'dicom'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Helper function to check allowed files
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to upload a medical image
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Preprocess the image (resize, normalize, etc.)
        processed_image = preprocess_image(filepath)
        
        return jsonify({"message": "File uploaded successfully", "filename": filename, "filepath": filepath}), 200
    
    return jsonify({"error": "File format not allowed"}), 400

# Route to process the uploaded image
@app.route('/process/<filename>', methods=['GET'])
def process_image(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404
    
    # Placeholder: You can add more sophisticated processing here
    processed_image = preprocess_image(filepath)
    
    return jsonify({"message": "Image processed", "filename": filename}), 200

# Route to analyze the image using AI/ML model
@app.route('/inference', methods=['POST'])
def run_inference():
    data = request.json
    filename = data.get('filename')
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404
    
    # Run the image through a model (placeholder for now)
    result = analyze_image(filepath)
    
    return jsonify({"message": "Inference completed", "result": result}), 200


# Route to enhance the image                                                                                                                                            
@app.route('/process/enhance/<filename>', methods=['POST'])                                                                                                             
def enhances_image(filename):                                                                                                                                
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)                                                                                                      
    if not os.path.exists(filepath):                                                                                                                                    
        return jsonify({"error": "File not found"}), 404
               
if __name__ == '__main__':
    app.run(debug=True)
