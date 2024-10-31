"""PII Scan"""
import spacy
import logging
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, RecognizerResult
from presidio_analyzer.predefined_recognizers import (ItDriverLicenseRecognizer,
                                                      ItVatCodeRecognizer,
                                                      ItFiscalCodeRecognizer,
                                                      ItIdentityCardRecognizer,
                                                      ItPassportRecognizer,
                                                      EsNieRecognizer,
                                                      EsNifRecognizer,
                                                      PlPeselRecognizer,
                                                      FiPersonalIdentityCodeRecognizer,
                                                      AuAbnRecognizer)
from presidio_anonymizer import AnonymizerEngine

# make sure en_core_web_lg is loaded correctly
# this can also be achieved with
# python -m spacy download en_core_web_lg
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    from spacy.cli import download
    download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")

# Configure logging to DEBUG level when needed
# logging.basicConfig(level=logging.DEBUG)
# Configure logging to INFO level when needed
# logging.basicConfig(level=logging.INFO)
# By default only critical logs will be printed
logging.basicConfig(level=logging.CRITICAL)

# Create an analyzer object
registry = RecognizerRegistry()
registry.load_predefined_recognizers()
# Add some language specific recognizers as english instead of default language
registry.add_recognizer(ItDriverLicenseRecognizer(supported_language='en'))
registry.add_recognizer(ItVatCodeRecognizer(supported_language='en'))
registry.add_recognizer(ItFiscalCodeRecognizer(supported_language='en'))
registry.add_recognizer(ItIdentityCardRecognizer(supported_language='en'))
registry.add_recognizer(ItPassportRecognizer(supported_language='en'))
registry.add_recognizer(EsNieRecognizer(supported_language='en'))
registry.add_recognizer(EsNifRecognizer(supported_language='en'))
registry.add_recognizer(PlPeselRecognizer(supported_language='en'))
registry.add_recognizer(FiPersonalIdentityCodeRecognizer(supported_language='en'))
registry.add_recognizer(AuAbnRecognizer(supported_language='en'))

# Create an analyzer object
# log_decision_process=True will log the decision process for debugging
analyzer = AnalyzerEngine(registry=registry, log_decision_process=False)
anonymizer = AnonymizerEngine()


def show_aggie_pride():
    """Show Aggie Pride"""
    return "Aggie Pride - Worldwide"


def anonymize_text(text: str, entity_list: list) -> str:
    """
    Anonymize the text using the entity list
    :param text: the text to be anonymized
    :param entity_list: the list of entities to be anonymized
           https://microsoft.github.io/presidio/supported_entities/
    """
    # Call analyzer to get results
    results = analyzer.analyze(text=text,
                               entities=entity_list,
                               language='en')

    # Analyzer results are passed to the AnonymizerEngine for anonymization
    anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)

    return anonymized_text.text


def anonymize_file(file_path: str) -> None:
    """
    Anonymize the text using the entity list
    :param file_path: the path to the file to be anonymized
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            print(anonymize_text(line, []))


def analyze_text(text: str, entity_list: list, ) -> list[RecognizerResult]:
    """
    Analyze the text using the entity list
    :param text: the text to be analyzed
    :param entity_list: the list of entities to be analyzed
           https://microsoft.github.io/presidio/supported_entities/
    """
    # Call analyzer to get results
    results = analyzer.analyze(text=text,
                               entities=entity_list,
                               language='en',
                               return_decision_process=True)  # return decision process details

    return results


if __name__ == '__main__':
    show_aggie_pride()
