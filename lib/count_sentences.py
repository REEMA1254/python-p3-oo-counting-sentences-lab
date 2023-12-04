#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace all sentence-ending punctuation with a period for uniformity
        temp_value = self.value.replace('?', '.').replace('!', '.')
        # Split the string into potential sentences
        potential_sentences = temp_value.split('.')
        # Filter out empty strings
        sentences = [sentence for sentence in potential_sentences if sentence.strip()]
        return len(sentences)
