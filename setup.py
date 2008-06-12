import os
import sys
import glob
from distutils.core import setup, Extension
from distutils.command.clean import clean
from distutils.command.install import install
from distutils.file_util import copy_file

try:
    # For some reason, importing Pyrex appears to change the value of
    # the MACOSX_DEPLOYMENT_TARGET to something that may be
    # inaccurate.  So we'll make sure that it's set to whatever it was
    # before we imported Pyrex.
    oldTarget = os.environ.get("MACOSX_DEPLOYMENT_TARGET", "")

    from Pyrex.Distutils import build_ext

    os.environ["MACOSX_DEPLOYMENT_TARGET"] = oldTarget

    sources = ["spidermonkey.pyx"]
except ImportError:
    from distutils.command.build_ext import build_ext
    sources = ["spidermonkey.c"]

def _find_obj_dir():
    objdirs = [dirname for dirname
               in glob.glob(os.path.join("js", "src", "*.OBJ"))
               if os.path.isdir(dirname)]
    if len(objdirs) > 1:
        raise AssertionError("Multiple objdirs found in "
                             "js dir: %s" % objdirs)
    elif not objdirs:
        raise AssertionError("No objdir found.")
    return objdirs[0]

class spidermonkey_install(install):
    def run(self):
        install.run(self)
        objdir = _find_obj_dir()
        if sys.platform == "darwin":
            copy_file(os.path.join(objdir, "libjs.dylib"),
                      "/usr/local/lib")
        elif sys.platform.startswith("win"):
            raise NotImplementedError("Windows not yet supported.")
        else:
            copy_file(os.path.join(objdir, "libjs.so"),
                      "/usr/local/lib")

class spidermonkey_clean(clean):
    def run(self):
        os.chdir(os.path.join("js", "src"))
        os.system("make -f Makefile.ref clean")
        os.chdir("../..")
        clean.run(self)

class spidermonkey_build_ext(build_ext):
    def run(self):
        os.chdir(os.path.join("js", "src"))
        rv = os.system("make -f Makefile.ref")
        os.chdir("../..")
        if rv != 0:
            print "Build failed, exiting."
            sys.exit(rv)
        objdir = _find_obj_dir()

        self.include_dirs.extend([os.path.join("js", "src"), objdir])
        self.library_dirs.append(objdir)

        if self.define is None:
            self.define = []
        if sys.platform.startswith("win"):
            raise NotImplementedError("Windows not yet supported.")
        self.define.append(("XP_UNIX", None))
        if sys.platform == "darwin":
            self.define.append(("XP_MACOSX", None))

        build_ext.run(self)

setup(name = "spidermonkey",
      version = "0.0.1a",
      license = "GPL",
      author = "John J. Lee",
      author_email = "jjl@pobox.com",
      description = "JavaScript / Python bridge.",
      url = "http://code.google.com/p/python-spidermonkey/",
      long_description = """\
Python/JavaScript bridge module, making use of Mozilla's spidermonkey
JavaScript implementation.  Allows implementation of JavaScript classes,
objects and functions in Python, and evaluation and calling of JavaScript
scripts and functions respectively.  Borrows heavily from Claes Jacobssen's
Javascript Perl module, in turn based on Mozilla's 'PerlConnect' Perl binding.
""",
      ext_modules =  [Extension("spidermonkey",
                                sources=sources,
                                libraries=["js"])],
      cmdclass = {'build_ext': spidermonkey_build_ext,
                  'clean': spidermonkey_clean,
                  'install': spidermonkey_install}
      )
