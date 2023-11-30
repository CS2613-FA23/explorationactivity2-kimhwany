# ExplorationActivity2
# Talk2Text & Text2Talk

## Introduction

**Talk2Text & Text2Talk** is a Python application that serves as a Text-to-Speech and Speech-to-Text converter. The project includes a graphical user interface (GUI) and utilizes various libraries for audio processing, GUI creation, and speech recognition.

## Prerequisites

1. **Python:**
   - Ensure you have Python installed on your system. If not, download it from [Python Downloads](https://www.python.org/downloads/).

2. **Required Libraries:**
   - Install the necessary Python packages using pip:
     ```bash
     pip install gtts playsound speech_recognition
     ```

## How to Run the Program

1. **Clone the Repository:**
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/CS2613-FA23/explorationactivity2-kimhwany.git
     ```

2. **Navigate to the Project Directory:**
   - Open your terminal or command prompt and go to the project directory:
     ```bash
     cd talk2text-text2talk
     ```

3. **Run the Program:**
   - Execute the following command to run the program:
     ```bash
     python3 main.py
     ```

## Program Overview

The Talk2Text & Text2Talk program is designed to provide a simple and user-friendly interface for converting text to speech and speech to text. It utilizes the following libraries:

- **os:** File operations.
- **tkinter:** GUI creation.
- **gTTS (Google Text-to-Speech):** Converts text to speech.
- **speech_recognition:** Recognizes speech and converts it to text.
- **playsound:** Plays the generated audio.

## How to Use the Program

### Text to Speech:

1. Launch the program by following the installation instructions.

2. Enter any text into the input field.

3. Click the "Convert" button to convert the text into speech.

4. The program will generate an audio file and play the speech back to you.

#### Text Input - "Hello, world!"
*User Input: The user has entered the text "Hello, world!" in the input field for conversion to speech.*

![image](https://github.com/CS2613-FA23/explorationactivity2-kimhwany/assets/76538067/a436a14a-fca9-4455-9bd8-a8918c7f5c2c)

#### Audio File Created from Text Input
*Generated Audio: The program has generated an audio file from the provided text input.*

![image](https://github.com/CS2613-FA23/explorationactivity2-kimhwany/assets/76538067/a8e3bf2d-d552-4dea-aa53-7ed6562afa21)

### Speech to Text:

1. Launch the program by following the installation instructions.

2. Click the "List Available Microphones" button to view a list of connected microphones.

3. Enter the desired recording duration in seconds in the "Duration" field.

4. Click the "Speech to Text" button.

5. The program will prompt you to speak into the microphone for the specified duration.

6. After recording, it will attempt to recognize the speech and display the results.

**Note:** Ensure that you have a working microphone connected to your system for the Speech-to-Text functionality.

#### Speech Recognition
*The program is prompting the user to speak into the microphone for speech recognition.*

![image](https://github.com/CS2613-FA23/explorationactivity2-kimhwany/assets/76538067/204b4554-8b7a-44b1-b435-5f75fb46bad6)

#### Speech Recognition Output - Successful Recognition
*The program successfully recognized the speech input, and the displayed message confirms the recognized text.*

![image](https://github.com/CS2613-FA23/explorationactivity2-kimhwany/assets/76538067/755cb32f-1ae0-4aef-94f0-2ee2abe09e4c)

#### Speech Recognition Output - Unsuccessful Recognition
*The program encountered difficulty understanding the provided audio, leading to an error message.*

![image](https://github.com/CS2613-FA23/explorationactivity2-kimhwany/assets/76538067/5aa7fb25-fb49-4ad3-921e-cdce2851a0f4)

## File Structure

- **t2t_t2t.py:** Main Python script containing the GUI and program logic.
- **README.md:** Project documentation.
