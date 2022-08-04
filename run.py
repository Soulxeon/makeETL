import settings
from startCheck import startCheck 

def run():
    settings.init()
    startCheck.check_init()

if __name__ == '__main__':
    run()