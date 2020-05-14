#!/usr/bin/python3
import sys

import argparse

from libs.core import Distancing as CvEngine
from libs.config_engine import ConfigEngine
from libs.input_config import InputConfig
from ui.web_gui import WebGUI as UI
from ui.offline_consumer import OfflineConsumer

class DistanceApp():
    def __init__(self, config, offline_video=None):
        self.config = config
        if offline_video:
            input_config = offline_video
        else:
            input_config = InputConfig(self.config.get_section_dict("App")["VideoPath"])

        self.engine = CvEngine(self.config, input_config)
        # TODO: rename ui to consumer
        if offline_video:
            self.ui = OfflineConsumer(self.config, self.engine, offline_video)
        else:
            self.ui = UI(self.config, self.engine)
        self.engine.set_ui(self.ui)
        self.ui.start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    args = parser.parse_args()
    config = ConfigEngine(args.config)
    DistanceApp(config)
