import os as os
import sys as sys
import requests as request
import zipfile as zipfile
from error.error import ThrowError

# def install_package(self):
#         if not (os.path.exists(f".\{self.install_directory}") and os.path.isdir(f".\{self.install_directory}")):
#             os.system("@echo off")
#             os.system(f"mkdir .\{self.install_directory}")
#         if self.package_name == "jsobj":
#             urllib.request.urlretrieve("https://github.com/code-roller/python-javascript-objects/archive/v1.0.0.zip", f".\\{self.install_directory}\\jsobj.zip")
#             with ZipFile('.\code-roller\jsobj.zip', 'r') as zipObj:
#                 zipObj.extractall(f".\{self.install_directory}\jsobj")
#             os.system("del .\code-roller\jsobj.zip")
#         else:
#             error = ThrowError("Package not found", "Please try a package name that actually exists")

class InstallPackage(object):
    def __init__(self, package_name, install_directory):
        self.package_name = package_name

        self.install_directory = install_directory
        self.find_repositories = "https://api.github.com/orgs/code-roller/repos"

        self.install_package()

    def install_package(self):
        self.repos = self.find_all_existsing_repos()

        if not self.check_for_package(self.package_name):
            ThrowError(f"Cannot find package {self.package_name}")
            sys.exit()



    def check_for_package(self, package_name):
        package_names = []
        for index in range(len(self.repos)):
            if "name" in self.repos[index]:
                package_names.append(
                    self.repos[
                        index
                    ]["name"]
                )
        return len(
            list(filter(lambda el : el == package_name, package_names))
        ) == 0

    def find_all_existsing_repos(self):
        try:
            repos = request.get(self.find_repositories)
            return repos.json()
        except Exception as exception:
            ThrowError("It seem like you are offline", "Try reconnecting")
            sys.exit()



    