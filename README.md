MIC HAT for Raspberry Pi
========================

## Requirements
+ [spidev](https://pypi.python.org/pypi/spidev)
+ [google-assistant-library](https://github.com/googlesamples/assistant-sdk-python/tree/master/google-assistant-sdk/googlesamples/assistant/library)

## Setup
1. Setup [google-assistant-library](https://github.com/googlesamples/assistant-sdk-python/tree/master/google-assistant-sdk/googlesamples/assistant/library)
2. Use `raspi-config` to enable SPI.
3. Install `spidev` (`pip install spidev`)
4. Run `python google_assistant.py`