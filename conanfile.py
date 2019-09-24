from conans import ConanFile, CMake, tools


class XtlConan(ConanFile):
    name = "xtl"
    version = "0.6.6"
    license = "BSD 3-Clause"
    #author = "<Put your name here> <And your email here>"
    url = "https://github.com/omaralvarez/conan-xtl"
    repo_url = "https://github.com/QuantStack/xtl"
    description = "The x template library"
    topics = ("templates")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*.hpp"
    no_copy_source = True

    def source(self):
        self.run("git clone -b '%s' --single-branch --depth 1 %s" % (self.version, self.repo_url))
    
    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="xtl")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
    
    def package_id(self):
        self.info.header_only()
