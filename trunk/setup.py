import os
macros = []
# I've only tested on Linux, so this is guesswork
if os.name == "posix":
    symbol = "XP_UNIX"
elif os.name == "nt":
    symbol = "XP_PC"
elif os.name == "mac":
    symbol = "XP_MAC"
    # what's XP_MAC_MPW?
elif os.name == "os2":
    symbol = "XP_OS2"
macros.append((symbol, None))

from distutils.core import setup, Extension
from Pyrex.Distutils import build_ext

setup(name = "spidermonkey",
      version = "0.0.1a",
      license = "GPL",
      author = "John J. Lee",
      author_email = "jjl@pobox.com",
      description = "JavaScript / Python bridge.",
      url = "http://wwwsearch.sourceforge.net/spidermonkey/",
      long_description = """\
Python/JavaScript bridge module, making use of Mozilla's spidermonkey
JavaScript implementation.  Allows implementation of JavaScript classes,
objects and functions in Python, and evaluation and calling of JavaScript
scripts and functions respectively.  Borrows heavily from Claes Jacobssen's
Javascript Perl module, in turn based on Mozilla's 'PerlConnect' Perl binding.
""",

      ext_modules =  [Extension("spidermonkey",
                                sources=["spidermonkey.pyx"],
                                libraries=["js"],
                                define_macros=macros)
                      ],

      cmdclass = {'build_ext': build_ext}
      )
