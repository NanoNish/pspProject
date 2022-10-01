import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pspdata.settings")

from mergedata.models import Data

def run():
    data = Data.objects.all()
    print(data)
    return

if __name__ == '__main__':
    run()