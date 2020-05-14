import datetime

from tools.environment_score import mx_environment_scoring_consider_crowd
from tools.objects_post_process import extract_violating_objects



class OfflineConsumer(object):
    """
    :param config: Is a ConfigEngine instance which provides necessary parameters.
    :param engine_instance:  A ConfigEngine object which store all of the config parameters. Access to any parameter
        is possible by calling get_section_dict method.
    """
    def __init__(self, config, engine, video_params):
        self.config = config
        self.engine = engine
        self.video_params = video_params
        self._dist_threshold = float(self.config.get_section_dict("PostProcessor")["DistThreshold"])

    def start(self):
        self.engine.process_video(self.video_params.video_uri)

    def update(self, input_frame, nn_out, distances):
        violating_objects = extract_violating_objects(distances, self._dist_threshold)
        env_score = mx_environment_scoring_consider_crowd(len(nn_out), len(violating_objects))

