#!/bin/sh

set -ex

# Provided with the code test
[ "$(./lexicosort.py acb abc bca abc)" == 'abc acb bca' ]
[ "$(./lexicosort.py acb abc bca cba)" == 'bca acb abc' ]
[ "$(./lexicosort.py aaa aa '' a)" == ' aa aaa' ]

echo "This works!"
