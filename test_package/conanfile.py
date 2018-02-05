from conans import ConanFile, CMake
import os
import shutil


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        bin_path = os.path.join("bin", "test_package")
        self.run("%s %s" % (bin_path, os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))))