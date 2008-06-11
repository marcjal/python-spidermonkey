
   [1]SourceForge.net Logo 

                                 spidermonkey

   Python/JavaScript bridge module, making use of Mozilla's
   [2]spidermonkey JavaScript implementation. Allows implementation of
   JavaScript classes, objects and functions in Python, and evaluation
   and calling of JavaScript scripts and functions respectively. Borrows
   heavily from Claes Jacobssen's Javascript Perl module, in turn based
   on Mozilla's 'PerlConnect' Perl binding.

   Example of a few of the features:
from spidermonkey import Runtime
rt = Runtime()
cx = rt.new_context()

class foo:
    def hello(self):
        print "Hello, JavaScript world!"

cx.bind_class(foo, bind_constructor=True)
f = cx.eval_script("""var f = new foo();
f.hello();
f; // script return value
""")
print f  # script return value
f.hello()

def repeat(x): return x*2
cx.bind_callable("repeat", repeat)

print cx.eval_script("""
var r = ["foo", {"bar": 2.3, "spam": [1,2,3]}];
repeat(r);
""")

   [3]Python 2.3 and [4]spidermonkey 1.5 are required (earlier versions
   may work, but are untested). Currently [5]Pyrex is required to build
   it (probably this won't stay a requirement - I will just include the C
   file that results from the Pyrex compilation).

   Thanks to Brendan Eich for help with several spidermonkey issues (and
   for all his Mozilla work), and to Erwin on the freenode #c IRC channel
   for gdb tips &c.

Download

   For installation instructions, see the INSTALL file included in the
   distribution.

   Development release. This is an alpha release: there are known bugs,
   and interfaces may change.
     * [6]spidermonkey-0.0.1a.tar.gz
     * [7]spidermonkey-0_0_1a.zip
     * [8]Change Log (included in distribution)

See also

   [9]PyXPCOM (see also [10]here).

FAQs

     * What license?
       The [11]GPL.
     * What platforms does it work on?
       It should work on any platform where spidermonkey runs. I've only
       tested on Linux, though.
     * Why?
       I wanted a way to interpret JavaScript with minimal dependencies,
       and to easily expose a Python DOM to JavaScript. This is used by
       [12]DOMForm.

   [13]John J. Lee, October 2003.

   [14]Home
   [15]ClientCookie
   [16]ClientForm
   [17]DOMForm
   spidermonkey
   [18]ClientTable
   [19]General FAQs
   [20]1.5.2 urllib2.py
   [21]1.5.2 urllib.py
   [22]Other stuff
   [23]Download
   [24]FAQs

References

   1. http://sourceforge.net/
   2. http://www.mozilla.org/js/spidermonkey/
   3. http://www.python.org/download/
   4. http://www.mozilla.org/js/spidermonkey/
   5. http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/
   6. http://wwwsearch.sourceforge.net/spidermonkey/src/spidermonkey-0.0.1a.tar.gz
   7. http://wwwsearch.sourceforge.net/spidermonkey/src/spidermonkey-0_0_1a.zip
   8. http://wwwsearch.sourceforge.net/spidermonkey/src/ChangeLog.txt
   9. http://pyxpcom.mozdev.org/
  10. http://aspn.activestate.com/ASPN/Downloads/Komodo/PyXPCOM/
  11. http://www.opensource.org/licenses/gpl-license.php
  12. http://wwwsearch.sourceforge.net/DOMForm/
  13. mailto:jjl@pobox.com
  14. http://wwwsearch.sourceforge.net/
  15. http://wwwsearch.sourceforge.net/ClientCookie/
  16. http://wwwsearch.sourceforge.net/ClientForm/
  17. http://wwwsearch.sourceforge.net/DOMForm/
  18. http://wwwsearch.sourceforge.net/ClientTable/
  19. http://wwwsearch.sourceforge.net/bits/clientx.html
  20. http://wwwsearch.sourceforge.net/bits/urllib2_152.py
  21. http://wwwsearch.sourceforge.net/bits/urllib_152.py
  22. http://wwwsearch.sourceforge.net/#other
  23. http://wwwsearch.sourceforge.net/spidermonkey/#download
  24. http://wwwsearch.sourceforge.net/spidermonkey/#faq
