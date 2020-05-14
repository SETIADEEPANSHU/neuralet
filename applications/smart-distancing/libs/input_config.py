import datetime

class InputConfig(object):
    def __init__(self, video_uri: str, capture_timestamp: datetime.datetime=None,
                 capture_limit: datetime.timedelta=None, camera_id: str=None,
                 resolution: 'Tuple[int,int]'=None,
                 ):
        if camera_id == None:
            camera_id = 'default'
        self.video_uri = video_uri
        self.resolution = resolution
        self.camera_id = camera_id
        self.capture_timestamp = capture_timestamp
        self.capture_limit = capture_limit
