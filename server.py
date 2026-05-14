"""
Flask server for Emotion Detection web application.
"""

# Import required Flask components
from flask import Flask, render_template, request

# Import your custom emotion detection function
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask application
app = Flask("Emotion Detector")

# Route for emotion analysis API endpoint
@app.route("/emotionDetector")
def sent_detector():
    """
    Handles emotion detection requests and returns analysis result.
    """

    # Get text input from URL query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    # Call emotion detection function
    response = emotion_detector(text_to_analyze)

    # Safety check
    if response['dominant_emotion'] is None:
        return "Invalid Text! Please try again!"

    # Extract emotion scores from response dictionary
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']

    # Extract dominant emotion
    dominant_emotion = response['dominant_emotion']

    # Return formatted string response
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

# Route for homepage (loads HTML page)
@app.route("/")
def render_index_page():
    """
    Renders homepage of the application.
    """

    return render_template('index.html')

# Run Flask app on local network (port 5000)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
