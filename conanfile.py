import os

from conans import ConanFile, tools


class GlibcVersionHeaderConan(ConanFile):
    name = "glibc_version_header"
    version = "master"
    license = "MIT"
    description = "Build portable Linux binaries without using an ancient distro"
    no_copy_source = True
    # No settings/options are necessary, this is header only

    def source(self):
        self.run("git clone --depth=1 --branch master git@github.com:wheybags/glibc_version_header.git .")

    def package(self):
        self.copy("*.h", dst="include", src="version_headers")

    def package_id(self):
        self.info.header_only()
