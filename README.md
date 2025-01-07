# Jarvis AI Assistant

This project is a voice-activated AI assistant built using Python, capable of executing various commands like opening websites, reporting the current time, and leveraging OpenAI's GPT-3.5-Turbo for advanced conversational interactions.

## Features

1. **Voice Recognition**:
   - Uses `speech_recognition` to capture and process user voice commands.

2. **Voice Responses**:
   - Provides audio feedback using the `win32com.client` library for text-to-speech.

3. **Web Browsing**:
   - Opens popular websites (e.g., YouTube, Google) or performs Google searches for user-specified queries.

4. **Time Reporting**:
   - Reports the current time on request.

5. **Application Launching**:
   - Opens specific applications like VS Code or directories like Downloads.

6. **ChatGPT Integration**:
   - Utilizes OpenAI's GPT-3.5-Turbo for conversational AI interactions when queries don't match predefined commands.

## Dependencies

The following Python libraries are required:

- `speech_recognition`: For capturing and interpreting voice commands.
- `webbrowser`: For launching websites.
- `win32com.client`: For text-to-speech capabilities.
- `pyttsx3`: Alternative text-to-speech engine (optional).
- `openai`: For GPT-3.5 integration.
- `os` and `subprocess`: For interacting with the file system and launching applications.
- `pywhatkit`: For additional functionality like playing YouTube videos.
- `random`: For generating varied search requests to avoid blocking.
- `googlesearch-python`: For Google searches.

### Additional File

- `key.py`: This file should contain the variable `apiKey` with your OpenAI API key.

### Installation

1. Clone the repository or download the script.
2. Install the required libraries using pip:

   ```bash
   pip install speechrecognition pyttsx3 openai pywhatkit googlesearch-python pypiwin32
   ```
3. Place your OpenAI API key in `key.py`:

   ```python
   apiKey = "your-openai-api-key"
   ```
4. Ensure your microphone is functional and permissions are granted to access it.

## Usage

1. **Run the Script**:
   Execute the Python script:

   ```bash
   python jarvis.py
   ```

2. **Interact with Jarvis**:
   - Use commands like:
     - "Open YouTube"
     - "What's the time?"
     - "Open downloads"
     - "Open Visual Studio Code"
   - Or provide queries to interact with GPT (e.g., "Tell me a joke").

3. **Voice Commands**:
   - Jarvis listens and responds accordingly to voice inputs.

## Features in Detail

- **Predefined Commands**:
  - Sites: Opens predefined websites like YouTube, Google, Instagram, Facebook, and Wikipedia.
  - Applications: Opens Visual Studio Code and Downloads directory.

- **Dynamic Google Searches**:
  - Performs random searches to mitigate errors.

- **ChatGPT Integration**:
  - Queries not recognized as commands are sent to OpenAI's API for a conversational response.

## Error Handling

- Exception handling is implemented for microphone input errors and failed web searches.

## Limitations

- Requires internet access for OpenAI API and Google searches.
- Designed for Windows, utilizing `win32com.client` for speech synthesis and `os.startfile` for file access.

## Future Enhancements

- Add support for more operating systems.
- Expand predefined commands for additional websites and applications.
- Enable continuous listening mode to improve user experience.



