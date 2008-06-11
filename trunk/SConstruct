import sys
import os

PYTHON_INCLUDE_DIR = sys.prefix + "/include/python" + sys.version[:3]

env = Environment(
    MOZDISTDIR = os.environ["MOZDISTDIR"],
    CPPPATH = [PYTHON_INCLUDE_DIR, "${MOZDISTDIR}/include",
               "${MOZDISTDIR}/include/js"],
    LIBPATH = ["${MOZDISTDIR}/lib"],
)

try:
    __import__("Pyrex")

    # We have Pyrex, so go ahead and add a target to generate
    # spidermonkey.c.
    env.Command("spidermonkey.c", "spidermonkey.pyx",
                "pyrexc -r -o $TARGET $SOURCE")
except ImportError:
    # We don't have Pyrex, so we'll use the pre-generated
    # spidermonkey.c.
    pass

env.LoadableModule(
    source = "spidermonkey.c",
    target = "spidermonkey.so",
    CCFLAGS=["-include", "mozilla-config.h"],
    LIBS=["mozjs"],
    FRAMEWORKS=["Python"]
    )
