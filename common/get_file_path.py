import os


class FilePath:
    def get_path(self, file):
        f = os.path.splitext(os.path.basename(file))[0] + '.yaml'
        fp = os.path.join(os.getcwd(), f)
        return fp
