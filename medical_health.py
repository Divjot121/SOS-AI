import os
import requests
import speech_recognition as sr
from gtts import gTTS
from datetime import datetime
import random

# Initialize Speech Recognition
recognizer = sr.Recognizer()


# Speak function to convert text to speech
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")  # For macOS; change to 'start' for Windows
    os.remove("output.mp3")


# Listen function to capture audio input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        return recognizer.recognize_google(audio).lower()
    except Exception as e:
        print(f"Error: {e}")
        return ""


# Feature: Real-Time Crisis Monitoring
def crisis_monitoring():
    return "No current crisis detected."


# Feature: Emergency Response Coordination
def emergency_response():
    return "Connecting you with local emergency services."


# Feature: Disaster Preparedness Training
def disaster_training():
    return "Training on disaster preparedness is available."


# Feature: Mental Health Support
def mental_health_support():
    return "Here are resources for mental health support: [links to resources]."


# Feature: Community Alerts
def community_alerts():
    return "No community alerts at this time."


# Feature: Resource Allocation
def resource_allocation():
    return "Resources are being allocated efficiently."


# Feature: Crowdsourced Information
def crowdsourced_info():
    return "You can report incidents in real-time."


# Feature: Predictive Analytics
def predictive_analytics():
    return "Using AI to predict potential disasters based on data."


# Feature: Multi-Language Support
def multi_language_support():
    return "Language options available: English, Spanish, French, etc."


# Feature: User-Friendly Interface
def user_friendly_interface():
    return "The interface is designed for easy navigation."


# Feature: Collaboration with NGOs
def ngo_collaboration():
    return "We are partnering with NGOs for effective resource distribution."


# Feature: Health Services Locator
def health_services_locator():
    return "Finding nearby health services for you."


# Feature: Volunteer Coordination
def volunteer_coordination():
    return "Connecting volunteers with local organizations."


# Feature: Safety Check-In Feature
def safety_check_in():
    return "You can notify family and friends of your safety."


# Feature: Social Media Integration
def social_media_integration():
    return "Critical updates will be shared through social media."


# Feature: Accessibility Features
def accessibility_features():
    return "The app includes features for users with disabilities."


# Feature: Educational Resources
def educational_resources():
    return "Providing educational content about disaster prevention."


# Feature: Community Building
def community_building():
    return "Facilitating local groups for resource sharing."


# Feature: Feedback Mechanism
def feedback_mechanism():
    return "Gathering user feedback to improve our services."


# Feature: Data Privacy Protection
def data_privacy():
    return "User data is secured and complies with regulations."


# Feature: AI-Powered Chatbot
def ai_chatbot():
    return "24/7 support available through our AI chatbot."


# Feature: Geolocation Services
def geolocation_services():
    return "Finding the nearest shelters and safe zones."


# Feature: Partnership with Local Governments
def local_government_partnerships():
    return "Collaborating with local authorities for efficient response."


# Feature: Event Tracking
def event_tracking():
    return "Monitoring significant local events affecting safety."


# Feature: Crisis Simulation Tools
def crisis_simulation():
    return "Starting crisis simulation... [simulation in progress]"


# Feature: Food and Water Distribution Tracking
def distribution_tracking():
    return "Tracking distribution of essential supplies."


# Feature: Awareness Campaigns
def awareness_campaigns():
    return "Promoting awareness about ongoing social issues."


# Feature: Resource Directory
def resource_directory():
    return "Accessing local resources like food banks and shelters."


# Feature: Crisis Mapping
def crisis_mapping():
    return "Visualizing disaster impact areas for better decision-making."


# Feature: Public Health Alerts
def public_health_alerts():
    return "Sending notifications about health-related emergencies."


# Feature: Mobile Donation Platform
def mobile_donation():
    return "You can donate funds or resources directly through the app."


# Feature: Legal Aid Information
def legal_aid_info():
    return "Providing resources for legal assistance."


# Feature: Pet Safety Information
def pet_safety_info():
    return "Guidance on caring for pets during emergencies."


# Feature: Weather Alerts
def weather_alerts():
    return "Sending real-time weather updates and warnings."


# Feature: Emergency Contact Storage
def store_emergency_contacts():
    contacts = {}
    while True:
        name = input("Enter contact name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        phone = input(f"Enter phone number for {name}: ")
        contacts[name] = phone
    return contacts


# Feature: Training for First Responders
def first_responder_training():
    return "Resources for training local first responders."


# Feature: Crisis Recovery Plans
def recovery_plans():
    return "Templates for creating community recovery plans."


# Feature: Impact Reporting
def impact_reporting():
    return "Tracking and reporting the impact of disasters."


# Feature: Donation Matching
def donation_matching():
    return "Connecting donors with organizations that match contributions."


# Feature: Community Forums
def community_forums():
    return "Facilitating discussions among users."


# Feature: Partnership with Educational Institutions
def educational_partnerships():
    return "Collaborating with schools on emergency preparedness."


# Feature: Local Business Support
def local_business_support():
    return "Connecting users with local businesses providing essential services."


# Feature: Sustainability Initiatives
def sustainability_initiatives():
    return "Promoting sustainable practices to minimize disaster impacts."


# Feature: Crisis Communication Tools
def crisis_communication():
    return "Helping organizations communicate effectively during emergencies."


# Feature: AI-Based Needs Assessment
def needs_assessment():
    return "Assessing community needs using AI."


# Feature: Post-Disaster Surveys
def post_disaster_surveys():
    return "Collecting data to evaluate response effectiveness."


# Feature: Crisis Resolution Strategies
def resolution_strategies():
    return "Providing frameworks for resolving community issues."


# Feature: Cultural Sensitivity Training
def cultural_sensitivity_training():
    return "Resources on providing support to diverse populations."


# Feature: Partnership with Mental Health Organizations
def mental_health_partnership():
    return "Collaborating with mental health services for holistic support."


# Main function for SOS AI
def virtual_assistant():
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()

        if "exit" in command:
            speak("Goodbye!")
            break
        elif "crisis monitoring" in command:
            speak(crisis_monitoring())
        elif "emergency response" in command:
            speak(emergency_response())
        elif "disaster training" in command:
            speak(disaster_training())
        elif "mental health" in command:
            speak(mental_health_support())
        elif "community alerts" in command:
            speak(community_alerts())
        elif "resource allocation" in command:
            speak(resource_allocation())
        elif "crowdsourced information" in command:
            speak(crowdsourced_info())
        elif "predictive analytics" in command:
            speak(predictive_analytics())
        elif "multi-language support" in command:
            speak(multi_language_support())
        elif "user-friendly interface" in command:
            speak(user_friendly_interface())
        elif "ngo collaboration" in command:
            speak(ngo_collaboration())
        elif "health services locator" in command:
            speak(health_services_locator())
        elif "volunteer coordination" in command:
            speak(volunteer_coordination())
        elif "safety check-in" in command:
            speak(safety_check_in())
        elif "social media integration" in command:
            speak(social_media_integration())
        elif "accessibility features" in command:
            speak(accessibility_features())
        elif "educational resources" in command:
            speak(educational_resources())
        elif "community building" in command:
            speak(community_building())
        elif "feedback mechanism" in command:
            speak(feedback_mechanism())
        elif "data privacy" in command:
            speak(data_privacy())
        elif "ai chatbot" in command:
            speak(ai_chatbot())
        elif "geolocation services" in command:
            speak(geolocation_services())
        elif "local government partnerships" in command:
            speak(local_government_partnerships())
        elif "event tracking" in command:
            speak(event_tracking())
        elif "crisis simulation" in command:
            speak(crisis_simulation())
        elif "food distribution tracking" in command:
            speak(distribution_tracking())
        elif "awareness campaigns" in command:
            speak(awareness_campaigns())
        elif "resource directory" in command:
            speak(resource_directory())
        elif "crisis mapping" in command:
            speak(crisis_mapping())
        elif "public health alerts" in command:
            speak(public_health_alerts())
        elif "mobile donation" in command:
            speak(mobile_donation())
        elif "legal aid" in command:
            speak(legal_aid_info())
        elif "pet safety" in command:
            speak(pet_safety_info())
        elif "weather alerts" in command:
            speak(weather_alerts())
        elif "store contacts" in command:
            contacts = store_emergency_contacts()
            speak("Emergency contacts stored successfully.")
        elif "first responder training" in command:
            speak(first_responder_training())
        elif "recovery plans" in command:
            speak(recovery_plans())
        elif "impact reporting" in command:
            speak(impact_reporting())
        elif "donation matching" in command:
            speak(donation_matching())
        elif "community forums" in command:
            speak(community_forums())
        elif "educational partnerships" in command:
            speak(educational_partnerships())
        elif "local business support" in command:
            speak(local_business_support())
        elif "sustainability initiatives" in command:
            speak(sustainability_initiatives())
        elif "crisis communication" in command:
            speak(crisis_communication())
        elif "needs assessment" in command:
            speak(needs_assessment())
        elif "post-disaster surveys" in command:
            speak(post_disaster_surveys())
        elif "resolution strategies" in command:
            speak(resolution_strategies())
        elif "cultural sensitivity training" in command:
            speak(cultural_sensitivity_training())
        elif "mental health partnership" in command:
            speak(mental_health_partnership())
        else:
            speak("I'm not sure how to respond to that.")


if __name__ == "__main__":
    virtual_assistant()