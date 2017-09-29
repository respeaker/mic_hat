MIC HAT for Raspberry Pi
========================

To build voice enabled projects with Google Assistant, Amazon Alexa Voice service and etc. 

[![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/mic_hatv1.0.png?raw=true)](https://www.seeedstudio.com/ReSpeaker-2-Mics-Pi-HAT-p-2874.html)


## Requirements
+ [seeed-voicecard](https://github.com/respeaker/seeed-voicecard), the kernel driver for on-board WM8960 codec
+ [spidev](https://pypi.python.org/pypi/spidev) for on-board SPI interface APA102 LEDs
+ [google-assistant-library](https://github.com/googlesamples/assistant-sdk-python/tree/master/google-assistant-sdk/googlesamples/assistant/library)
+ [avs](https://github.com/respeaker/avs), Alexa Voice Service client python library
+ [voice-engine](https://github.com/voice-engine/voice-engine)

## Setup
1. Go to [seeed-voicecard](https://github.com/respeaker/seeed-voicecard) and install it
2. Use `raspi-config` to enable SPI.
3. Install `spidev` (`pip install spidev`).
4. Run `python pixels.py` to test the pixels.

## Build a Google Home like device with Google Assistant SDK
1. Setup [google-assistant-library](https://github.com/googlesamples/assistant-sdk-python/tree/master/google-assistant-sdk/googlesamples/assistant/library)
2. Run `python google_assistant.py`

## Build an Echo like device with Alexa Voice Service
1. `pip install avs voice-engine`
2. Go to [snowboy](https://github.com/Kitt-AI/snowboy) and install its python binding.
3. `python alexa.py`
