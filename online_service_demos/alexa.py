"""
Hands-free Voice Assistant with Snowboy and Alexa Voice Service. The wake-up keyword is "alexa"

Requirement:
    pip install avs
    pip install voice-engine
"""


import time
import logging
from voice_engine.source import Source
from voice_engine.kws import KWS
from avs.alexa import Alexa
from pixels import pixels


def main():
    logging.basicConfig(level=logging.DEBUG)

    src = Source(rate=16000, frames_size=320)
    kws = KWS(model='alexa', sensitivity=0.8)
    alexa = Alexa()


    alexa.state_listener.on_listening = pixels.listen
    alexa.state_listener.on_thinking = pixels.think
    alexa.state_listener.on_speaking = pixels.speak
    alexa.state_listener.on_finished = pixels.off


    src.link(kws)
    kws.link(alexa)

    def on_detected(keyword):
        logging.info('detected {}'.format(keyword))
        alexa.listen()

    kws.set_callback(on_detected)

    src.recursive_start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break

    src.recursive_stop()


if __name__ == '__main__':
    main()
