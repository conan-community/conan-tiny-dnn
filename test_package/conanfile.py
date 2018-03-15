from conans import ConanFile, CMake, tools
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch", "cppstd"
    generators = "cmake"

    def configure(self):
        if not self.settings.cppstd:
            if self.settings.os == "Windows":
                self.settings.cppstd = 14
            else:
                self.settings.cppstd = "gnu14"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy(pattern="*.dll", src="bin", dst="bin")
        self.copy(pattern="*.dylib", src="lib", dst="bin")

    def test(self):
        with tools.chdir("bin"):
            arg = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
            self.run(".%stest_package %s" % (os.sep, arg))
