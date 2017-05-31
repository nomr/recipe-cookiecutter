import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

if __name__ == '__main__':
    # move Jenkins file up one folder
    shutil.move(os.path.join(PROJECT_DIRECTORY, 'Jenkinsfile'),
                os.path.join(PROJECT_DIRECTORY, '..'))


