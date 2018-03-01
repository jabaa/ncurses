from conans import ConanFile, AutoToolsBuildEnvironment


class NcursesConan(ConanFile):
    name = "ncurses"
    version = "6.1"
    license = "MIT"
    url = "https://invisible-island.net/ncurses/"
    description = "ncurses (new curses) is a programming library providing an application programming interface (API) that allows the programmer to write text-based user interfaces in a terminal-independent manner. It is a toolkit for developing \"GUI-like\" application software that runs under a terminal emulator. It also optimizes screen changes, in order to reduce the latency experienced when using remote shells."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    exports_sources = "src/*"

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.configure(configure_dir="src", build=False, host=False, target=False)
        env_build.make()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["libform.a", "libform_g.a", "libmenu.a", "libmenu_g.a", "libncurses.a", "libncurses++.a", "libncurses_g.a", "libncurses++_g.a", "libpanel.a", "libpanel_g.a"]
