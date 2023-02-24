import os
import allure
from xx_api.MoocLearn.learn import Learns


class Learn:
    @allure.step("视频标记")
    def video_learn(self, res):
        learn = Learns().mark_video(res)
        return learn

#
# if __name__ == '__main__':
#     Learn().video_learn()
