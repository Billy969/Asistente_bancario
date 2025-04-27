import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RAG:
    def __init__(self, faqs_path):
        self.faqs = self.load_faqs(faqs_path)
        self.vectorizer = TfidfVectorizer()
        self.vectorizer.fit([faq["question"] for faq in self.faqs])

    def load_faqs(self, faqs_path):
        with open(faqs_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_answer(self, question):
        question_vector = self.vectorizer.transform([question])
        similarity_scores = cosine_similarity(question_vector, self.vectorizer.transform([faq["question"] for faq in self.faqs]))
        
        most_similar_index = similarity_scores.argmax()
        return self.faqs[most_similar_index]["answer"]
    
if __name__ == '__main__':
    rag_agent = RAG("C:/Users/Juan/Documents/asistente_bancario/data/faqs.json")
    print(rag_agent.get_answer("¿Cuáles son los requisitos para abrir una cuenta de ahorros?"))