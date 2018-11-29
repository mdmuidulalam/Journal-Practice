# assumed docker is installed properly
# download docker from here(for windows) -> https://docs.docker.com/docker-for-windows/install/
# for linux -> curl -sSL https://get.docker.com/ | sh
import subprocess
import os

# build docker image if needed
crawlerContainerId = subprocess.check_output(['docker', 'images', '-q', 'crawler'])
if len(crawlerContainerId) == 0: 
    os.system('docker build -t crawler .')
else:
    print('crawler image already exist')

# kick off the container
os.system('docker run -it --rm -v $(pwd)/crawler:/crawler crawler')