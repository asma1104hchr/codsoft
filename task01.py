import re
import random

def doctor_chatbot_response(user_input):
    # Convert user input to lowercase to make matching case-insensitive
    user_input = user_input.lower()

    # Greetings: Responds to various greeting phrases
    if re.search(r"\b(hello|hi|hey|good morning|good evening)\b", user_input):
        return random.choice([
            "Hello! I'm Dr. Bot. How can I assist you with your health today?",
            "Hi there! I'm here to help with any medical concerns you might have.",
            "Hey! How can I assist you with your health?"
        ])

    # Asking about Symptoms: Responds to inquiries about general symptoms
    elif re.search(r"\b(symptoms|feeling|pain|ache|sick|unwell)\b", user_input):
        return random.choice([
            "I'm sorry to hear that you're not feeling well. Can you describe your symptoms in more detail?",
            "I understand you're experiencing discomfort. Could you tell me where you're feeling pain?",
            "Let's get to the bottom of this. What symptoms are you experiencing?"
        ])

    # Specific Symptoms: Responds to specific symptoms like fever or headache
    elif re.search(r"\b(fever|temperature|headache|dizzy|cough|sore throat|nausea)\b", user_input):
        return random.choice([
            "It sounds like you might have a common illness. Make sure to rest and stay hydrated. If symptoms persist or worsen, please consult a healthcare professional.",
            "These symptoms could indicate a minor illness, but it's always best to monitor them closely. If they don't improve, seek medical advice.",
            "Common symptoms like these usually pass with time, but if you're concerned or if they persist, consider consulting a healthcare professional."
        ])

    # Asking for Health Advice: Provides general health and wellness tips
    elif re.search(r"\b(advice|tips|healthy|wellness|diet|exercise)\b", user_input):
        return random.choice([
            "Staying healthy involves a balanced diet, regular exercise, and adequate sleep. Try to eat a variety of fruits and vegetables, and drink plenty of water.",
            "For good health, incorporate physical activity into your daily routine, and avoid excessive stress. How can I assist you further with your health goals?",
            "A healthy lifestyle includes managing stress, eating nutritious foods, and staying active. Let me know if you need tips on any specific aspect of wellness."
        ])

    # Medication Inquiry: Responds to questions about medication
    elif re.search(r"\b(medicine|medication|pill|drug)\b", user_input):
        return random.choice([
            "It's crucial to take medications as prescribed by your healthcare provider. If you have specific questions about your medication, please provide more details.",
            "Always follow the dosage instructions on your medication label. If you have any concerns or experience side effects, consult your healthcare provider.",
            "Medication advice is best provided by a healthcare professional. If you have questions about a specific medication or its effects, let me know!"
        ])

    # Follow-up Questions: Provides responses to queries about what to do next
    elif re.search(r"\b(should I|can I|do I need)\b", user_input):
        return random.choice([
            "For personalized advice, it's best to consult with a healthcare professional. They can offer guidance based on your symptoms and medical history.",
            "Your healthcare provider is the best resource for personalized recommendations. If you have specific concerns, it's important to discuss them with them.",
            "For medical decisions, professional advice is crucial. I'm here to provide general guidance, but a real doctor's opinion is always best."
        ])

    # Goodbye: Responds to farewell phrases
    elif re.search(r"\b(goodbye|bye|thank you|thanks)\b", user_input):
        return random.choice([
            "You're welcome! Take care of yourself, and don't hesitate to reach out if you need anything else.",
            "Goodbye! Wishing you good health and a speedy recovery if you're feeling unwell.",
            "Take care, and remember to prioritize your health. Goodbye!"
        ])

    # Catch-all response: For any input that doesn't match the above categories
    else:
        return random.choice([
            "I'm here to help with health-related questions. Could you provide more details so I can assist you better?",
            "I'm not sure I understood that. Could you provide more information about your health concern?",
            "Health is important. Can you tell me more about what you're experiencing so I can offer better assistance?"
        ])

# Main loop to simulate conversation
def chat():
    print("Dr. Bot: Hi! I'm Dr. Bot, your virtual health assistant. How can I help you today?")
    while True:
        user_input = input("You: ")
        # Check for farewell phrases to end the conversation
        if re.search(r"\b(goodbye|bye|thank you|thanks)\b", user_input.lower()):
            print("Dr. Bot: Take care! Wishing you good health.")
            break
        # Get a response from the chatbot
        response = doctor_chatbot_response(user_input)
        print(f"Dr. Bot: {response}")

# Start the chatbot
chat()
