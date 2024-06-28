# Ash_AI

# Voice Assistant for Controlling Hardware Devices

This repository contains the implementation of a voice assistant programmed in Python. The voice assistant can control various hardware devices through voice commands. It utilizes speech recognition and text-to-speech conversion for interaction.

## Features

- **Voice Control**: Interact with the assistant using voice commands.
- **Hardware Control**: Control hardware devices such as light bulbs, appliances, etc.
- **Speech Recognition**: Recognize user commands through speech.
- **Text-to-Speech Conversion**: Output responses and information through speech.
- **Extensible**: Easily extend functionality by adding new voice commands and hardware interfaces.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/voice-assistant.git
   ```

2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```bash
   python voice_assistant.py
   ```

2. Speak to the assistant using voice commands.

## Supported Commands

- **Open Applications**: Open various applications like YouTube, Google, Gmail, etc.
- **Control Hardware**: Turn on/off hardware devices, adjust settings, etc.
- **Retrieve Information**: Search Wikipedia, get the current time, etc.
- **Send Emails**: Send emails to specified recipients.
- **Take Notes**: Create notes based on voice input.
- **Media Playback**: Control media playback (play, pause, mute, etc.).
- **Interact with the User**: Greet the user, respond to questions, tell jokes, etc.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for bug fixes, improvements, or new features.


## Acknowledgements

- [pyttsx3](https://pypi.org/project/pyttsx3/): Text-to-speech conversion library.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): Library for performing speech recognition.
- [pyautogui](https://pypi.org/project/PyAutoGUI/): Library for GUI automation.
- [wikipedia](https://pypi.org/project/wikipedia/): Library for interacting with Wikipedia.

---


## ERROR
Traceback (most recent call last):
  File "C:\Users\Seyram\Desktop\voice\Virtual-Assistant\controller.py", line 4, in <module>
    board=pyfirmata.Arduino(comport)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Seyram\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyfirmata\__init__.py", line 19, in __init__
    super(Arduino, self).__init__(*args, **kwargs)
  File "C:\Users\Seyram\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyfirmata\pyfirmata.py", line 101, in __init__
    self.setup_layout(layout)
  File "C:\Users\Seyram\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyfirmata\pyfirmata.py", line 157, in setup_layout
    self._set_default_handlers()
  File "C:\Users\Seyram\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyfirmata\pyfirmata.py", line 161, in _set_default_handlers
    self.add_cmd_handler(ANALOG_MESSAGE, self._handle_analog_message)
  File "C:\Users\Seyram\AppData\Local\Programs\Python\Python312\Lib\site-packages\pyfirmata\pyfirmata.py", line 185, in add_cmd_handler
    len_args = len(inspect.getargspec(func)[0])
                   ^^^^^^^^^^^^^^^^^^
AttributeError: module 'inspect' has no attribute 'getargspec'. Did you mean: 'getargs'?


```
Replace
len_args = len(inspect.getargspec(func)[0])
with

len_args = len(inspect.getfullargspec(func)[0])
```