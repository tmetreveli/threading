import threading
import requests

class CustomThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(CustomThread, self).__init__(*args, **kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        super(CustomThread, self).join()
        return self._return

def get_data(product_id, url):
    response = requests.get(url + str(product_id))
    data = response.json()
    return data