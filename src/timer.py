# This code courtesy of:
# www.hyung.com/posts/python-performance-analysis
# Updated for Python 3 by Parker Michaelson.



import time

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.process_time()
        return self

    def get_secs(self):
        return time.process_time() - self.start

    def __exit__(self, *args):
        self.secs = self.get_secs()
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print('elapsed time: %f ms' % self.msecs)
