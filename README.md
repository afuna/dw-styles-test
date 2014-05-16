Dreamwidth Styles Automated Testing

The basic idea is that you:
* apply etc/enable-s2-hacking.diff
* start with a base known-good state
* create baseline screenshots: `nosetests --with-save-baseline` for everything, or `nosetests --with-save-baseline test_[layout].py` for individual layouts
* make your changes and recompile: `$LJHOME/bin/update-db.pl -r -p`
* test that your changes didn't have any unexpected effects: `nosetests` for everything or `nosetests test_[layout].py` for individual layouts

Obviously once you make changes to the CSS you'll expect something to change! This is to make it easier to confirm you're not doing unexpected changes (especially if you're touching core2base, or working on multiple styles at once).

Requires [needle](http://needle.readthedocs.org/en/latest/). That will also install nosetests and selenium.

Make sure to check out the bottom for instructions on using `perceptualdiff`. The visual diff of screenshots is nice.

