from pkg_resources import resource_filename, resource_string
from PyQt5 import QtGui, QtCore


# The following lines add the images and css directories to the search path.
QtCore.QDir.addSearchPath('images', resource_filename(__name__, 'images'))
QtCore.QDir.addSearchPath('css', resource_filename(__name__, 'css'))


def resourcePath(name, resource_dir="images/"):
    return resource_filename(__name__, resource_dir + name)

def loadImage(name):
    return QtGui.QPixmap(resourcePath(name))

def loadStyleSheet(name):
    # Opens the file and returns all the contents in string form
    return resource_string(__name__, "css/" + name).decode('utf8')
