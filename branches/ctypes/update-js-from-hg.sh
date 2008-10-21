#! /bin/bash

# This script assumes that you have the mozilla-central HG repository
# checked out at ../mozilla-central relative to the directory this
# file is in, and copies all relevant spidermonkey files into this
# Python-SpiderMonkey checkout.
#
# The mozilla-central HG repository can be found at:
#
#   http://hg.mozilla.org/mozilla-central/

cp -R ../mozilla-central/js/src js
rm -rf js/src/xpconnect
rm -rf js/src/liveconnect
