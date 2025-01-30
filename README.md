# Vietnamese Text Segmentation Service

A Flask-based RESTful API service for Vietnamese text segmentation using VnCoreNLP. This service provides endpoints for segmenting both raw text and document files (PDF, DOCX, TXT).

## Features

- Vietnamese text segmentation using VnCoreNLP
- Support for multiple file formats (PDF, DOCX, TXT)
- RESTful API endpoints
- Docker containerization
- Configurable environment
- Health check endpoint
- Comprehensive logging

## Prerequisites

- Docker and Docker Compose
- Python 3.9 or higher (for local development)
- Java Runtime Environment (JRE) 11 or higher
- At least 2GB of free disk space for the VnCoreNLP model

## Installation

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/text-segmentation-service.git
cd text-segmentation-service
```

2. Create and configure environment file:
```bash
cp .env.example .env
```

3. Build and run the service:
```bash
docker-compose up --build
```

### Local Development

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
```

3. Run the application:
```bash
python run.py
```

## Configuration

The service can be configured using environment variables in the `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| VNCORENLP_PATH | Path to VnCoreNLP model | /app/vncorenlp |
| DEBUG | Enable debug mode | False |
| HOST | Server host | 0.0.0.0 |
| PORT | Server port | 5000 |
| LOG_LEVEL | Logging level | INFO |
| MAX_CONTENT_LENGTH | Maximum file size (bytes) | 16777216 |
| ALLOWED_EXTENSIONS | Allowed file extensions | pdf,txt,docx |

## API Endpoints

### Health Check
```
GET /health
```
Returns the service health status.

**Response:**
```json
{
    "status": "healthy"
}
```

### Text Segmentation
```
POST /text_segmentation
Content-Type: application/json
```

**Request Body:**
```json
{
    "text": "Tôi là người Việt Nam."
}
```

**Response:**
```json
{
    "segmented_text": "Tôi là người_Việt_Nam ."
}
```

### File Segmentation
```
POST /file_segmentation
Content-Type: multipart/form-data
```

**Request Body:**
- `file`: File to be segmented (PDF, DOCX, or TXT)

**Response:**
```json
{
    "segmented_text": "Processed text with segmentation..."
}
```

## Error Handling

The service returns appropriate HTTP status codes and error messages:

- 400: Bad Request (invalid input)
- 500: Internal Server Error
- 413: Payload Too Large (file size exceeds limit)
- 415: Unsupported Media Type (invalid file type)

## Logging

Logs are stored in the `logs` directory and include:
- Request information
- Processing status
- Error details
- Performance metrics

## Development

### Project Structure
```
text_segmentation/
├── __init__.py
├── app.py
├── config.py
├── services/
│   ├── __init__.py
│   └── segmentation.py
└── utils/
    ├── __init__.py
    ├── file_handlers.py
    └── logging.py
```

### Running Tests
```bash
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP) for the Vietnamese NLP toolkit
- Flask framework
- Docker and Docker Compose

## Support

For support, please open an issue in the GitHub repository or contact [your-email@example.com]
