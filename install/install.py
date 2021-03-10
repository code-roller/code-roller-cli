import os
import urllib.request
from zipfile import ZipFile
from error.error import ThrowError

class InstallPackage(object):
    def __init__(self, package_name, install_directory):
        self.package_name = package_name

        self.install_directory = install_directory

        self.install_package()

    def install_package(self):
        if not (os.path.exists(f".\{self.install_directory}") and os.path.isdir(f".\{self.install_directory}")):
            os.system("@echo off")
            os.system(f"mkdir .\{self.install_directory}")
        if self.package_name == "jsobj":
            urllib.request.urlretrieve("https://github.com/code-roller/python-javascript-objects/archive/v1.0.0.zip", f".\\{self.install_directory}\\jsobj.zip")
            with ZipFile('.\code-roller\jsobj.zip', 'r') as zipObj:
                zipObj.extractall(f".\{self.install_directory}\jsobj")
            os.system("del .\code-roller\jsobj.zip")
        else:
            error = ThrowError("Package not found", "Please try a package name that actually exists")