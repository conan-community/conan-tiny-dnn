from conans import ConanFile, CMake, tools
import os


class TinyDnnConan(ConanFile):
    name = "tiny-dnn"
    version = "0.1.1"
    license = "The BSD 3-Clause License"
    homepage = "http://tiny-dnn.readthedocs.io/en/latest/"
    url = "https://github.com/tiny-dnn/tiny-dnn"
    description = ("tiny-dnn is a C++14 implementation of deep learning. "
                   "It is suitable for deep learning on limited computational resource, embedded "
                   "systems and IoT devices.")
    no_copy_source = True
    exports_sources = ["LICENSE"]

    def source(self):
        source_url = ("%s/archive/v%s.zip" % (self.url, self.version))
        tools.get(source_url)
        os.rename("%s-%s" % (self.name, self.version), "sources")

    def package(self):
        self.copy("*LICENSE*", dst="licenses", src="sources")
        self.copy("*tiny_*.h", dst="include", src="sources")
        self.copy("*tiny_*.hpp", dst="include", src="sources")

    def package_info(self):
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
