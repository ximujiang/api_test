import os

from xx_api.MoocLearn.learn import Learns


class Learn:

    def video_learn(self, res):
        learn = Learns().mark_video(res)
        return learn

#
# if __name__ == '__main__':
#     Learn().video_learn()
