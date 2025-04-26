import random
import nltk  # pip install nltk
nltk.data.path.append("D:/Users/SAYANI SENGUPTA/AppData/Roaming/nltk_data")  # Adjust to your path
nltk.download('punkt', download_dir=nltk.data.path[0])
from nltk.stem import PorterStemmer

# initialize NLTK and download required resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("tokenizers/punkt/english.pickle")
stemmer = PorterStemmer()

# DATA: All possible intents and responses
data = {
    "greetings": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
    "responses": ["Hello! How can I assist you with your job search today?", "Hi there! Looking for a job?", "Hey! Need help finding career opportunities?"],

    "job_search": ["i am looking for a job", "job opportunities", "find me a job", "search jobs", "how to get a job"],
    "job_responses": ["There are many platforms like LinkedIn, Indeed, and Naukri to search for jobs.", "You can network through LinkedIn or apply through company websites directly."],

    "internships": ["i am looking for internships", "internship opportunities", "find internships", "summer internship", "internship programs"],
    "internship_responses": ["Internships can be found on Internshala, LinkedIn, and AngelList.", "Consider applying early for internships to improve your chances!"],

    "skills": ["what skills are required", "skills for getting a job", "what should i learn", "important skills"],
    "skills_responses": ["It depends on your field, but communication skills, technical skills, and problem-solving are valued everywhere.", "Learning Python, data analysis, and digital marketing are highly in-demand skills!"],

    "it_jobs": ["it jobs", "software jobs", "tech jobs", "technology careers", "software engineer jobs"],
    "it_responses": ["You can apply for IT jobs through LinkedIn, Stack Overflow Jobs, and GitHub Careers.", "Learning programming languages like Python, Java, and frameworks will help you secure IT roles."],

    "marketing_jobs": ["marketing jobs", "digital marketing", "advertising careers", "sales and marketing", "branding jobs"],
    "marketing_responses": ["Marketing roles are available on sites like Naukri, LinkedIn, and AngelList.", "Skills like SEO, content marketing, and social media management are highly valued in marketing."],

    "finance_jobs": ["finance jobs", "banking jobs", "investment banking", "accounting jobs", "finance careers"],
    "finance_responses": ["Finance jobs are available in banks, fintech companies, and consulting firms.", "Skills like financial modeling, Excel proficiency, and accounting principles are essential."],

    "farewells": ["bye", "goodbye", "see you later", "take care", "farewell"],
    "farewell_responses": ["Goodbye! Wishing you success in your job search!", "See you later! Hope you land a great job!", "Take care and good luck with your career journey!"],
}

# Mapping intent categories to their corresponding response categories
INTENT_RESPONSE_MAP = {
    "greetings": "responses",
    "job_search": "job_responses",
    "internships": "internship_responses",
    "skills": "skills_responses",
    "it_jobs": "it_responses",
    "marketing_jobs": "marketing_responses",
    "finance_jobs": "finance_responses",
    "farewells": "farewell_responses"
}


# Preprocess user input
def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return [stemmer.stem(token) for token in tokens]


# Generate a response based on user input
def get_response(user_input):
    processed_input = preprocess(user_input)

    # check for all the pattern categories
    for intent_category, response_category in INTENT_RESPONSE_MAP.items():
        for pattern in data[intent_category]:
            processed_pattern = preprocess(pattern)
            if all(word in processed_input for word in processed_pattern):
                return random.choice(data[response_category])

    # fallback for unknown inputs
    return "I'm not sure how to respond to that. Could you please specify if you're looking for jobs, internships, or skill advice?"


# Chat loop
def chat():
    print("Chatbot: Hello! I'm your Job Search Assistant. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Best of luck with your career!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "_main_":
    chat()
