from video import Video


class Popcoder:

    def process_json(self, data, background_color='#000000'):
        video = Video(data, background_color)
        video.process()
