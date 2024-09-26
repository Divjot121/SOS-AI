import re
import random
import time
from textblob import TextBlob
from collections import defaultdict
import google.generativeai as genai
from googletrans import Translator

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyADImpvFindPFR2tfmrksjEvVSuZ99ruF0")


class MentalHealthAssistant:
    def __init__(self):
        # Emergency contacts for different mental health resources
        self.emergency_contacts = {
            "AASRA": "91-9820466726",
            "Vandrevala Foundation": "1860-2662-345 or 1800-2333-330",
            "iCall": "+91 22-25521111",
            "NIMHANS": "080-4611 0007",
            "Sneha Foundation": "044-24640050"
        }

        # List of coping strategies to provide support
        self.coping_strategies = [
            "Try deep breathing exercises: Inhale for 4 seconds, hold for 4 seconds, exhale for 4 seconds.",
            "Practice mindfulness meditation for 5-10 minutes.",
            "Go for a short walk or do some light exercise.",
            "Write down your thoughts and feelings in a journal.",
            "Listen to calming music or nature sounds.",
            "Reach out to a friend or family member for support.",
            "Try progressive muscle relaxation: Tense and then relax each muscle group in your body.",
            "Engage in a creative activity like drawing, coloring, or crafting.",
            "Practice positive self-talk and affirmations.",
            "Take a warm bath or shower to relax your body and mind.",
            "Spend time in nature.",
            "Practice gratitude journaling.",
            "Engage in a hobby or activity you enjoy.",
            "Get enough sleep and maintain a healthy diet.",
            "Seek professional help if needed."
        ]

        # Memory for tracking conversation context
        self.memory = {}

        # User preferences for personalized responses
        self.user_preferences = {}

    def analyze_sentiment(self, user_input):
        """Analyze the sentiment of the user's message to determine emotional tone."""
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity  # Sentiment value between -1.0 (negative) and 1.0 (positive)
        return sentiment

    def analyze_input(self, user_input, user_id):
        """Analyze user input and determine the response."""
        # Initialize memory for user_id if not present
        if user_id not in self.memory:
            self.memory[user_id] = []

        # Append user input with interaction type as 'general'
        self.memory[user_id].append({"text": user_input, "timestamp": time.time(), "interaction": "general"})

        user_input_lower = user_input.lower()

        # Sentiment analysis for understanding user emotions
        sentiment = self.analyze_sentiment(user_input)
        self.log_interaction(user_id, "general", user_input)

        translator = Translator()
        detected_lang = translator.detect(user_input).lang

        if detected_lang != 'en':
            user_input = translator.translate(user_input, dest='en').text
            print(f"Translated input: {user_input}")

        sentiment = self.analyze_sentiment(user_input)

        # Checking for suicidal or dangerous keywords
        if re.search(r'\b(suicid|kill myself|end my life)\b', user_input_lower):
            return self.handle_emergency(user_id)
        elif re.search(r'\b(depress|anxious|overwhelm|stress)\b', user_input_lower):
            return self.offer_support_and_strategies(user_id, sentiment)
        elif re.search(r'\b(lonely|alone|isolat)\b', user_input_lower):
            return self.address_loneliness(user_id, sentiment)
        else:
            return self.general_response(user_input)

    def save_interaction(self, user_id, interaction_type):
        """Update memory with the type of interaction."""
        if self.memory[user_id]:
            # Update the latest memory with the type of interaction
            self.memory[user_id][-1]['interaction'] = interaction_type

    # Ensure that each response method calls `save_interaction`
    def handle_emergency(self, user_id):
        """Handle emergency cases like suicidal ideation."""
        prompt = (
            "Someone has expressed suicidal thoughts. Provide a compassionate, urgent response and direct them to "
            "appropriate emergency contacts."
        )
        ai_response = self.generate_gemini_response(prompt)
        response = f"{ai_response}\n\nPlease contact one of these emergency resources immediately:\n\n"
        for name, number in self.emergency_contacts.items():
            response += f"{name}: {number}\n"

        # Save the emergency interaction type
        self.save_interaction(user_id, "emergency")
        return response

    def offer_support_and_strategies(self, user_id, sentiment):
        """Offer emotional support and suggest coping strategies based on the sentiment."""
        if sentiment < -0.5:
            response = "It sounds like you're really going through something difficult. "
        elif sentiment > 0.5:
            response = "I'm glad to hear some positivity in your words! But remember, it's okay to reach out when things aren't perfect. "
        else:
            response = "I'm sorry to hear that you're feeling this way. "

        response += "Here are a couple of coping strategies that might help:\n\n"
        strategies = random.sample(self.coping_strategies, 2)
        for strategy in strategies:
            response += f"- {strategy}\n"
        response += "\nIf these feelings persist, please consider talking to a mental health professional."

        self.save_interaction(user_id, "support")
        return response

    def analyze_sentiment(self, user_input):
        """Analyze the sentiment of the user's message to determine emotional tone."""
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity  # Sentiment value between -1.0 (negative) and 1.0 (positive)
        return sentiment

    def log_interaction(self, user_id, interaction_type, user_input):
        with open("interaction_log.txt", "a") as f:
            f.write(
                f"{time.strftime('%Y-%m-%d %H:%M:%S')} - User ID: {user_id}, Type: {interaction_type}, Text: {user_input}\n")

    def save_user_data(self, name, user_id, phone_number):
        """Save user's name, user_id, and phone number in a file."""
        with open("user_data.txt", "a") as f:
            f.write(f"Name: {name}, User ID: {user_id}, Phone: {phone_number}\n")

    def generate_gemini_response(self, user_input):
        try:
            generation_config = {
                "temperature": 0.9,
                "top_p": 1,
                "top_k": 1,
                "max_output_tokens": 2048,
            }

            safety_settings = [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
            ]

            model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config,
                                          safety_settings=safety_settings)

            response = model.generate_content(
                f"Someone shared this message: {user_input}. Provide a calm response and solution, and hear them out. take indian scenarios considered")

            if response.candidates:
                return response.candidates[0].content.parts[0].text
            else:
                return "I'm sorry, I couldn't generate a response. Please try again."

        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm sorry, but I couldn't generate a response right now. Please try again later."

    def handle_emergency(self, user_id):
        """Handle emergency cases like suicidal ideation."""
        prompt = (
            "Someone has expressed suicidal thoughts. Provide a compassionate, urgent response and direct them to "
            "appropriate emergency contacts."
        )
        ai_response = self.generate_gemini_response(prompt)
        response = f"{ai_response}\n\nPlease contact one of these emergency resources immediately:\n\n"
        for name, number in self.emergency_contacts.items():
            response += f"{name}: {number}\n"

        self.save_interaction(user_id, "emergency")
        return response

    def offer_support_and_strategies(self, user_id, sentiment):
        """Offer emotional support and suggest coping strategies based on the sentiment."""
        if sentiment < -0.5:
            response = "It sounds like you're really going through something difficult. "
        else:
            response = "I'm sorry to hear that you're feeling this way. "

        response += "Here are a couple of coping strategies that might help:\n\n"
        strategies = random.sample(self.coping_strategies, 2)
        for strategy in strategies:
            response += f"- {strategy}\n"
        response += "\nIf these feelings persist, please consider talking to a mental health professional."

        self.save_interaction(user_id, "support")
        return response

    def address_loneliness(self, user_id, sentiment):
        """Address loneliness and offer suggestions to cope with isolation."""
        if sentiment < -0.5:
            response = "I understand that feeling lonely can be really tough, especially when you're feeling down. "
        else:
            response = "Feeling lonely can happen to anyone, but it's important to know that you are not alone in this."

        response += "Here are some suggestions that might help:\n\n"
        response += "1. Reach out to a friend or family member, even if it's just for a short chat.\n"
        response += "2. Join a local club or online community based on your interests.\n"
        response += "3. Volunteer for a cause you care about – it's a great way to meet like-minded people.\n"
        response += "4. Practice self-care and try to be kind to yourself during this time.\n"

        self.save_interaction(user_id, "loneliness")
        return response

    def general_response(self, user_input):
        """Generate a general compassionate response for non-specific queries."""
        prompt = (
            f"Someone just shared this: '{user_input}'. Provide a compassionate, thoughtful response that offers support "
            "and a willingness to listen."
        )
        ai_response = self.generate_gemini_response(prompt)
        return ai_response

    def save_interaction(self, user_id, interaction_type):
        """Save interaction for emotional trend tracking."""
        self.memory[user_id].append({
            "interaction": interaction_type,
            "timestamp": time.time()
        })

    def detect_trends(self, user_id):
        """Analyze emotional trends over time."""
        trends = defaultdict(int)
        for interaction in self.memory[user_id]:
            trends[interaction['interaction']] += 1

        if trends['emergency'] >= 2:
            return "Seek immediate professional help."
        if trends['support'] >= 3:
            return "Consider a professional therapist."
        return "Monitor your emotional health."

    def get_user_prompt(self, name=None):
        if name:
            return f"Hi {name}, Any problem are you facing? Feel free to discuss! "
        else:
            return "You: "


def main():
    assistant = MentalHealthAssistant()
    print("Welcome to the AI Mental Health Assistant. How can I help you today?")
    print(" AASRA: +91-9820466726\n",
          "Vandrevala Foundation: 1860-2662-345 or 1800-2333-330\n",
          "iCall: +91 22-25521111\n",
          "NIMHANS: 080-4611 0007\n",
          "Sneha Foundation: 044-24640050\n")
    print("(Type 'exit' to end the conversation)")

    # Ask for user's name to personalize conversation
    # Ask for user's name to personalize conversation
    user_name = input("Before we start, what's your name? ")
    assistant.user_preferences['name'] = user_name.strip()

    # Ask for phone number
    phone_number = input(
        f"Thanks, {user_name}. Could you also provide your phone number for us to reach out if needed? ").strip()

    # Generate a random user ID
    user_id = random.randint(1, 100000)

    # Save user's name, user ID, and phone number to a file
    assistant.save_user_data(user_name, user_id, phone_number)

    while True:
        user_input = input(assistant.get_user_prompt(assistant.user_preferences.get('name'))).strip()
        if user_input.lower() == 'exit':
            print(f"Take care, {user_name}. Remember that help is always available if you need it.")
            break
        response = assistant.analyze_input(user_input, user_id)
        print(f"\nAssistant: {response}")

        # Check for emotional trends after each interaction
        trends = assistant.detect_trends(user_id)
        if trends:
            print(f"\nSOS AI's advice: {trends}")


if __name__ == "__main__":
    main()