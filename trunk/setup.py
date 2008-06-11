import os
import sys
from distutils.core import setup, Extension

try:
    # For some reason, importing Pyrex appears to change the value of
    # the MACOSX_DEPLOYMENT_TARGET to something that may be
    # inaccurate.  So we'll make sure that it's set to whatever it was
    # before we imported Pyrex.
    oldTarget = os.environ["MACOSX_DEPLOYMENT_TARGET"]

    from Pyrex.Distutils import build_ext

    os.environ["MACOSX_DEPLOYMENT_TARGET"] = oldTarget

    sources = ["spidermonkey.pyx"]
except ImportError:
    from distutils.command.build_ext import build_ext
    sources = ["spidermonkey.c"]

if not os.environ.has_key("MOZSDKDIR"):
    print ("Please set the MOZSDKDIR environment variable "
           "to the location of your XULRunner SDK before "
           "running this script.")
    sys.exit(1)

MOZ_SDK_DIR = os.environ["MOZSDKDIR"]

ext = Extension(
    "spidermonkey",
    sources=sources,
    include_dirs=[os.path.join(MOZ_SDK_DIR, "include"),
                  os.path.join(MOZ_SDK_DIR, "include", "js")],
    library_dirs=[os.path.join(MOZ_SDK_DIR, "lib")],
    extra_compile_args=["-include", "mozilla-config.h"],
    libraries=["mozjs"]
    )

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
      ext_modules =  [ext],
      cmdclass = {'build_ext': build_ext}
      )
