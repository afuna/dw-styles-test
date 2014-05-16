#!/bin/bash

# creates the baseline images we want to compare against
# with the assumption that we want the various multiple-column layouts on mobile
# to look like the one-column view

tests=$*

nosetests --with-save-baseline $tests
mkdir screenshots/baseline/mobile-multicolumn 2> /dev/null
for screenshot in $(ls screenshots/baseline/*columns-*-mobile.png)
do
    backup_file=screenshots/baseline/mobile-multicolumn/$(basename $screenshot)
    if [[ ! -f $backup_file ]]
    then
        # back it up and then replace
        cp $screenshot $backup_file
        cp $(echo $screenshot | sed 's/two.*mobile/one-column-mobile/' | sed 's/three.*mobile/one-column-mobile/') $screenshot
    fi
done