import py_vncorenlp
from pathlib import Path
from ..utils.logging import log_error

class SegmentationService:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self._initialize_model()

    def _initialize_model(self):
        if not Path(self.model_path).exists():
            print(f"Downloading VnCoreNLP model to {self.model_path}")
            py_vncorenlp.download_model(save_dir=self.model_path)
        return py_vncorenlp.VnCoreNLP(save_dir=self.model_path)

    def segment_text(self, text: str) -> str | None:
        try:
            if not isinstance(text, str) or not text.strip():
                raise ValueError("Input text must be a non-empty string.")
            
            annotated_result = self.model.annotate_text(text)
            sentences = self._extract_sentences(annotated_result)
            return self._sentences_to_text(sentences)
        
        except KeyError as e:
            log_error("segment_text", 500, f"Missing expected key: {e}")
            raise Exception("Unexpected response format from the segmentation model.")
        
        except ValueError as e:
            log_error("segment_text", 500, f"Invalid input: {e}")
            raise Exception("Invalid input text.")
        
        except Exception as e:
            log_error("segment_text", 500, f"Unexpected error: {str(e)}")
            raise Exception("An unexpected error occurred during segmentation.")

    @staticmethod
    def _extract_sentences(annotated_result):
        # Extract sentences from the annotated data with error handling. 
        # :param annotated_result: Dictionary containing annotated sentence data.
        # :return: List of sentences (each sentence is a list of words).
    
        if not isinstance(annotated_result, dict):
            raise Exception("Expected a dictionary, but got: " + str(type(annotated_result)))
    
        sentences = []
        for _, sentence in annotated_result.items():  # Iterate through numbered sentences
            words = [token['wordForm'] for token in sentence]  # Extract 'wordForm' 
            if words:
                sentences.append(words)
        return sentences

    @staticmethod
    def _sentences_to_text(sentences):
        # Convert the list of sentence words into readable text.
        return '\n'.join(' '.join(sentence) for sentence in sentences)
