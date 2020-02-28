import totalsum
from fabric.api import cd, local, run
from fabric.state import output


def publish(message):
    v = totalsum.__version__

    output["everything"] = True
    local("git pull")
    try:
        local("git add -A")
        local("git commit -m '%s'" % message)
        local("git push")
    except:
        print("Add, commit e push non riuscito")
    try:
        local("git tag {}".format(v))
        local("git push --tags")
    except:
        print("Tag non riuscito")
    try:
        local("python setup.py sdist register")
        local("python setup.py sdist upload")
    except:
        print("Upload non riuscito")
