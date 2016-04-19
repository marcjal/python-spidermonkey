# Python-Spidermonkey #

This Python module allows for the implementation of Javascript? classes, objects and functions in Python, as well as the evaluation and calling of Javascript scripts and functions. It borrows heavily from Claes Jacobssen's `Javascript` Perl module, which in turn is based on Mozilla's `PerlConnect` Perl binding.

This code was originally written by John J. Lee in 2003.  After being unmaintained for a number of years, it was subsequently picked up by Atul Varma in 2008.

# Tutorial #

The first thing you'll want to do is create a `Runtime` instance, which encapsulates a `JSRuntime` object from Spidermonkey.  From the [JSAPI User Guide](http://developer.mozilla.org/en/docs/JSAPI_User_Guide):

A `JSRuntime`, or **runtime**, is the space in which the Javascript variables, objects, scripts, and contexts used by your application are allocated. Every `JSContext` and every object in an application lives within a `JSRuntime`. They cannot travel to other runtimes or be shared across runtimes. Most applications only need one runtime.

Creating the `Runtime` instance is straightforward:

```
>>> from spidermonkey import Runtime
>>> rt = Runtime()
```

You'll then want to use the `Runtime` to create a `Context`instance, which encapsulates a `JSContext` object from Spidermonkey. From the JSAPI User Guide:

A `JSContext`, or **context**, is like a little machine that can do many things involving Javascript code and objects. It can compile and execute scripts, get and set object properties, call Javascript functions, convert Javascript data from one type to another, create objects, and so on.

In Firefox, for instance, a different context is used for each webpage you view.  A separate context is even created for each physical browser window, because much of Firefox's functionality is actually written in Javascript.  Contexts can have their own security policies associated with them, and objects can be shared between multiple contexts.

Creating a context in Python-Spidermonkey is done like so:

```
>>> cx = rt.new_context()
```

Now that you've got a context, you can do lots of things, like evaluating arbitrary Javascript expressions and using their results in Python code:

```
>>> cx.eval_script("1 + 2") + 3
6
```

We can create classes in Python and access them in Javascript, too:

```
>>> class Foo:
...   def hello(self):
...     print "Hello, Javascript world!"
>>> cx.bind_class(Foo, bind_constructor=True)
>>> cx.eval_script("var f = new Foo(); f.hello();")
Hello, Javascript world!
```

We can also get back objects from Javascript and use them:

```
>>> f = cx.eval_script("f;")
>>> f.hello()
Hello, Javascript world!
```

# Limitations #

The module currently has a number of features that still need to be implemented.  For instance, it's not yet possible to call a function defined in Javascript:

```
>>> cx.eval_script("function foo(x) { return x + 1; }; foo;")
{'prototype': {}}
```

Errors in Javascript code also don't produce particularly helpful tracebacks:

```
>>> cx.eval_script("3 + undefinedVariable")
Traceback (most recent call last):
...
JSError: can't evaluate Javascript script
```

# Installation #

Note that at present, installation has only been tested on OS X and 64-bit Ubuntu Linux; support for Windows is forthcoming.

At present, you'll need a C compiler on your system to install this extension, as well as the [Pyrex](http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/) package.

  * Check out the Python-Spidermonkey module from the [SVN repository](http://code.google.com/p/python-spidermonkey/source/checkout).
  * From the root of your checkout, run:
```
python setup.py build
```

> Don't worry about the compiler warnings.  Then, with appropriate permissions, run:
```
python setup.py install
```



# Testing #

The module has a test suite.  Just run:

```
python test.py
```

Note that one of the tests currently prints out a Javascript error message.  This isn't a test failure (though it is a [bug](http://code.google.com/p/python-spidermonkey/issues/detail?id=1)).

# Acknowledgements #

Thanks to Brendan Eich for help with several Spidermonkey issues (and for all his Mozilla work), and to Erwin on the freenode `#c` IRC channel for gdb tips.
