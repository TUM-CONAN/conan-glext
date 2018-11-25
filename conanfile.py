#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os


class ZMQConan(ConanFile):
    name = "glext"
    version = "1.3"
    url = "https://github.com/ulricheck/conan-glext"
    description = "GLext headers from Khronos"
    license = "https://github.com/someauthor/somelib/blob/master/LICENSES"
    exports_sources = ["LICENSE"]
    no_copy_source = True

    def source(self):
        tools.download("https://www.khronos.org/registry/OpenGL/api/GL/glext.h", "GL/glext.h")
        tools.download("https://www.khronos.org/registry/OpenGL/api/GL/glcorearb.h", "GL/glcorearb.h")
        tools.download("https://www.khronos.org/registry/OpenGL/api/GL/glxext.h", "GL/glxext.h")
        tools.download("https://www.khronos.org/registry/OpenGL/api/GL/wglext.h", "GL/wglext.h")
        tools.download("https://www.khronos.org/registry/EGL/api/KHR/khrplatform.h", "KHR/khrplatform.h")

    def build(self):
        pass

    def package(self):
        self.copy(pattern='*.h', src='GL', dst='include/GL', keep_path=True)
        self.copy(pattern='*.h', src='KHR', dst='include/KHR', keep_path=True)

    def package_id(self):
        self.info.header_only()
