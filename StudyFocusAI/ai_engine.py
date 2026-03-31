import random
from textblob import TextBlob
import nltk

# Ensure necessary NLTK data is downloaded (run once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

class StudyAIEngine:
    def __init__(self):
        # Mock Database of questions with pre-assigned difficulty for the ML simulation
        self.question_bank = {
            "Physics": [
                ("What is Newton's Second Law?", "Easy"),
                ("Explain the concept of Quantum Superposition.", "Hard"),
                ("Define velocity.", "Easy"),
                ("Calculate the escape velocity of a black hole.", "Hard"),
                ("What is friction?", "Medium")
            ],
            "History": [
                ("Who was the first President of the USA?", "Easy"),
                ("Analyze the socio-economic impacts of the Industrial Revolution.", "Hard"),
                ("When did WWII end?", "Medium")
            ],
            "Computer Science": [
                ("What is a variable?", "Easy"),
                ("Explain the Big O notation of Merge Sort.", "Hard"),
                ("What is a binary tree?", "Medium")
            ]
        }

    def generate_study_plan(self, subject, hours):
        """
        Rule-based logic to divide time effectively.
        """
        hours = float(hours)
        if hours < 1:
            return ["Time is too short! Try a 15-minute rapid fire quiz."]
        
        # Architecture: Allocation logic
        plan = []
        minutes = hours * 60
        
        plan.append(f"00:00 - 00:10 : Review Syllabus for {subject}")
        
        deep_work_time = (minutes - 20) * 0.6 # 60% for core study
        practice_time = (minutes - 20) * 0.4  # 40% for practice
        
        plan.append(f"00:10 - {int(10 + deep_work_time)}m : Deep Reading & Summarization (Focus Phase)")
        plan.append(f"{int(10 + deep_work_time)}m - {int(10 + deep_work_time + practice_time)}m : Quiz & Active Recall")
        plan.append(f"Last 10 mins : Review Errors & Motivational Check")
        
        return plan

    def summarize_text(self, text):
        """
        NLP based summarization.
        In a production env, use 'transformers' (BERT/GPT).
        Here we use TextBlob/NLTK for a lightweight extraction summary.
        """
        if not text:
            return "No text provided to summarize."
            
        blob = TextBlob(text)
        sentences = blob.sentences
        
        # Simple extraction: Take the first 3 sentences or 30% of text
        # This mimics extracting 'Key Takeaways'
        summary_length = max(1, int(len(sentences) * 0.3))
        summary = " ".join([str(s) for s in sentences[:summary_length]])
        
        return summary

    def get_quiz(self, subject):
        """
        Simulates ML Classification retrieval.
        """
        questions = self.question_bank.get(subject, [("Generic Question?", "Easy")])
        # Randomize for variety
        selected = random.sample(questions, min(len(questions), 3))
        return selected

    def extract_keywords(self, text):
        """
        NLP Pipeline for Keyword Extraction.
        """
        blob = TextBlob(text)
        return list(blob.noun_phrases[:5])  # Return top 5 noun phrases
