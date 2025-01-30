import re
import unicodedata

def standardize_data(text: str) -> str:
    # Standardize text by removing noise characters and normalizing format.

    if not isinstance(text, str):
        return ""
    
    # Convert to lowercase and normalize unicode
    text = text.lower()
    text = unicodedata.normalize('NFKC', text)
    
    # Define patterns for noise characters
    noise_patterns = {
        # Basic punctuation
        r'[.,;:!?"]': ' ',
        # Quotes and brackets
        r'["\'"\'«»\(\)\[\]\{\}]': ' ',
        # Dashes and hyphens
        r'[\-\_\—\–]': ' ',
        # Multiple spaces
        r'\s+': ' ',
        # Ellipsis
        r'\.{2,}': ' ',
        # Special characters
        r'[♫♪♩♬♭♮♯°†‡±′″‾⁄]': ' ',
        # Common Vietnamese-specific patterns
        r'\.{3,}': ' ',  # Ellipsis variations
        r'\d+[\./,]\d+': ' ',  # Numbers with separators
        # Remove extra spaces around punctuation
        r'\s*[,\.!?:;]\s*': ' ',
        # Remove multiple punctuation
        r'[,\.!?:;]+': ' ',
        # Remove standalone numbers
        r'\s+\d+\s+': ' ',
        # Remove URLs
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+': ' ',
        # Remove email addresses
        r'[\w\.-]+@[\w\.-]+': ' '
    }
    
    # Apply each pattern
    for pattern, replacement in noise_patterns.items():
        text = re.sub(pattern, replacement, text)
    
    # Additional cleaning steps
    text = text.strip()  # Remove leading/trailing whitespace
    text = re.sub(r'\s+', ' ', text)  # Normalize spaces
    
    return text
