from flask import Flask, request, jsonify
from .config import Config
from .services.segmentation import SegmentationService
from .utils.logging import log_info, log_error, setup_logging
from .utils.file_handlers import (
    extract_text_from_pdf,
    extract_text_from_txt,
    extract_text_from_docx
)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    setup_logging()
    segmentation_service = SegmentationService(app.config['VNCORENLP_PATH'])

    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({"status": "healthy"}), 200

    @app.route('/text_segmentation', methods=['POST'])
    def text_segmentation():
        try:
            data = request.json
            if data is None or 'text' not in data:
                return jsonify({"error": "No text provided"}), 400
            
            text = data['text']
            if not text:
                return jsonify({"error": "Empty text provided"}), 400
            
            segmented_text = segmentation_service.segment_text(text)
            log_info("segment_text", 200, "Text segmentation successful")
            return jsonify({"segmented_text": segmented_text}), 200
            
        except Exception as e:
            log_error("text_segmentation", 500, f"Error during text segmentation: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500

    @app.route('/file_segmentation', methods=['POST'])
    def file_segmentation():
        try:
            file = request.files.get('file')
            if not file or not hasattr(file, 'filename') or not file.filename:
                return jsonify({"error": "No file provided or empty filename"}), 400

            file_name = file.filename.lower()
            
            if file_name.endswith('.pdf'):
                text = extract_text_from_pdf(file)
            elif file_name.endswith('.txt'):
                text = extract_text_from_txt(file)
            elif file_name.endswith('.docx'):
                text = extract_text_from_docx(file)
            else:
                return jsonify({"error": "Unsupported file type"}), 400
            
            segmented_text = segmentation_service.segment_text(text)
            log_info("file_segmentation", 200, f"File segmentation successful, file name: {file_name}")
            return jsonify({"segmented_text": segmented_text}), 200
            
        except Exception as e:
            log_error("file_segmentation", 500, f"Error processing file: {str(e)}")
            return jsonify({"error": "Internal Server Error"}), 500

    return app
