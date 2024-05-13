import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout, CMakeDeps
from conan.tools.build import check_min_cppstd
from conan.tools.files import rmdir


class LeafRecipe(ConanFile):
    name = "leaf"
    version = "1.0.1"
    description = "Coreutils library for C++ (poor man's Google::Abseil)"
    author = "whs31 <whs31@github.io>"
    topics = ("logging", "coreutils", "utility")

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "test": [True, False],
    }
    default_options = {
        "shared": True,
        "test": False
    }

    exports_sources = "*"

    @property
    def _min_cppstd(self):
        return "20" 

    def requirements(self):
        self.requires("fmt/[^10.1.0]", transitive_headers=True, transitive_libs=True)
        self.requires("spdlog/1.13.0", transitive_headers=True, transitive_libs=True)
        self.requires("tl-expected/20190710", transitive_headers=True, transitive_libs=True)
        self.requires("magic_enum/[^0.9.0]", transitive_libs=True)
        if self.options.test:
            self.requires("gtest/1.14.0")

    def layout(self):
        cmake_layout(self)

    def validate(self):
        if self.settings.get_safe("compiler.cppstd"):
            check_min_cppstd(self, self._min_cppstd)

    def configure(self):
        self.options["spdlog/*"].shared = True
        self.options["fmt/*"].shared = True

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.cache_variables["BUILD_SHARED_LIBS"] = self.options.shared
        tc.cache_variables["INTEGRATION_TESTS"] = self.options.test
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))
        rmdir(self, os.path.join(self.package_folder, "lib", "pkgconfig"))
        rmdir(self, os.path.join(self.package_folder, "res"))
        rmdir(self, os.path.join(self.package_folder, "share"))

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "leaf")
        self.cpp_info.set_property("cmake_target_name", "leaf::leaf")
        self.cpp_info.libs = ["leaf"]
        self.cpp_info.requires = ["fmt::fmt", "magic_enum::magic_enum", "spdlog::spdlog", "tl-expected::tl-expected"]
