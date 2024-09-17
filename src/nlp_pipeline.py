import spacy

class NLPPipeline:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process(self, text):
        doc = self.nlp(text)
        return [(token.text, token.lemma_, token.pos_) for token in doc]

if __name__ == "__main__":
    nlp_pipeline = NLPPipeline()
    print(nlp_pipeline.process("What is the capital of France?"))
