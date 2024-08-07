import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import random
from googlesearch import search
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pywhatkit


recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()


def speak(text):
    """Convert text to speech."""
    print(f"Speaking: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()


def listen():
    """Listen for a voice command and convert it to text."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None


def google_search(query):
    """Perform a Google search and return the top results."""
    try:
        print(f"Searching for: {query}")
        results = list(search(query, num_results=3))
        print(f"Search results: {results}")
        return results
    except Exception as e:
        print(f"Error during Google search: {e}")
        return [f"An error occurred: {e}"]


def open_website(url):
    """Open a website in the default web browser."""
    webbrowser.open(url)
    speak(f"Opening {url}")


def tell_joke():
    """Tell a random joke."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts."
    ]
    joke = random.choice(jokes)
    speak(joke)


def tell_date():
    """Tell the current date."""
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")


def play_music():
    """Play music by opening a music streaming website."""
    open_website("https://www.spotify.com")


def calculate(expression):
    """Perform a basic arithmetic calculation."""
    try:
        result = eval(expression)
        speak(f"The result is {result}")
    except Exception as e:
        speak(f"Sorry, I couldn't calculate that. {str(e)}")


def send_email(to_email, subject, body):
    """Send an email using a predefined email account."""
    from_email = "kumarswarup7272@gmail.com"  # Use your gmail.
    from_password = "my_password_1234"  # use your password
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        speak(f"Sorry, I couldn't send the email. {str(e)}")


def play_youtube_video(query):
    """Play a specific YouTube video or search for a video and play it."""
    try:
        speak(f"Playing {query} on YouTube.")
        pywhatkit.playonyt(query)
    except Exception as e:
        speak(f"Sorry, I couldn't play the video. {str(e)}")


def main():
    """Main function to run the Jarvis-like AI."""
    speak("Hello, I am Jarvis. How can I assist you today?")
    while True:
        command = listen()
        if command:
            command = command.lower()
            if "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            elif "how are you" in command:
                speak("I am fine, how can i help you!")
            elif "how r u" in command:
                speak("I am fine, how can i help you!")
            elif "open youtube" in command:
                speak("Opening Youtube...")
                open_website("https://www.youtube.com")
            elif "open instagram" in command:
                speak("Opening instagram...")
                open_website("https://www.instagram.com")
            elif "open facebook" in command:
                speak("Opening facebook...")
                open_website("https://www.facebook.com")
            elif "open twitter" in command:
                speak("Opening twitter...")
                open_website("https://www.twitter.com")
            elif "open linkedin" in command:
                speak("Opening linkedin...")
                open_website("https://www.linkedin.com")
            elif "open reddit" in command:
                speak("Opening reddit...")
                open_website("https://www.reddit.com")
            elif "tell me a joke" in command:
                tell_joke()
            elif "what is the date" in command:
                tell_date()
            elif "play music" in command:
                play_music()
            elif "calculate" in command:
                expression = command.split("calculate")[-1].strip()
                calculate(expression)
            elif "send email" in command:
                speak("To whom should I send the email?")
                to_email = listen()
                speak("What is the subject of the email?")
                subject = listen()
                speak("What should I say in the email?")
                body = listen()
                send_email(to_email, subject, body)
            elif "play" in command and "youtube" in command:
                query = command.replace("play", "").replace("on youtube", "").strip()
                play_youtube_video(query)
            else:
                results = google_search(command)
                if results:
                    speak("Here are the results.")
                    for i, result in enumerate(results):
                        print(f"Result {i + 1}: {result}")
                    open_website(results[0])
                else:
                    speak("Sorry, I couldn't find any results.")


if __name__ == "__main__":
    main()
