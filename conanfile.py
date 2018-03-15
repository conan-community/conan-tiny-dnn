from conans import ConanFile, tools
import os


class TinyDnnConan(ConanFile):
    name = "tiny-dnn"
    version = "0.1.1"
    license = "The BSD 3-Clause License"
    description = ("tiny-dnn is a C++14 implementation of deep learning. "
                   "It is suitable for deep learning on limited computational resource, embedded "
                   "systems and IoT devices.")
    homepage = "https://github.com/tiny-dnn/tiny-dnn"
    url = "https://github.com/conan-community/conan-tiny-dnn"
    settings = "os"
    no_copy_source = True
    exports_sources = ["LICENSE"]

    def source(self):
        source_url = ("%s/archive/v%s.zip" % (self.homepage, self.version))
        tools.get(source_url)
        os.rename("%s-%s" % (self.name, self.version), "sources")

    def package(self):
        self.copy("*LICENSE*", dst="licenses", src="sources")
        self.copy("*tiny_*.h", dst="include", src="sources")
        self.copy("*tiny_*.hpp", dst="include", src="sources")

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
