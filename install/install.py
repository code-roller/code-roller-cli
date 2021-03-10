import requests as RequestHandler
import os as os

class InstallPackage(object):
    def __init__(self, package_name, install_directory):
        self.package_name = package_name

        self.install_directory = install_directory

        print(self.package_name)