"""Contains functionality related to Lines"""
import json
import logging
import time


from models import Line


logger = logging.getLogger(__name__)


class Lines:
    """Contains all train lines"""

    def __init__(self):
        """Creates the Lines object"""
        self.red_line = Line("red")
        self.green_line = Line("green")
        self.blue_line = Line("blue")
        logger.info("Lines Created")

    def process_message(self, message):
        """Processes a station message"""

        
        if "TURNSTILE_SUMMARY" != message.topic():
            value = message.value()
            if message.topic() == "com.udacity.transfomed.stations":
                value = json.loads(value)
            
            #logger.info("processing from " + message.topic())
            #if message.value():
            #    logger.info("type " + str(type(value)))
            #    logger.info("processing " + str(value))
            #else:
            #    logger.info("empty message")
            #logger.info("behind_if")
            

            if value["line"] == "green":
                self.green_line.process_message(message)
            elif value["line"] == "red":
                self.red_line.process_message(message)
            elif value["line"] == "blue":
                self.blue_line.process_message(message)
            else:
                logger.debug("discarding unknown line msg %s", value["line"])
        elif "TURNSTILE_SUMMARY" == message.topic():
            self.green_line.process_message(message)
            self.red_line.process_message(message)
            self.blue_line.process_message(message)
        else:
            logger.info("ignoring non-lines message %s", message.topic())
