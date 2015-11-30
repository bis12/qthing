#!/bin/sh

set -ex

# Provided with the code test
[ "$(./lexicosort.py acb abc bca abc)" == 'abc acb bca' ]
[ "$(./lexicosort.py acb abc bca cba)" == 'bca acb abc' ]
[ "$(./lexicosort.py aaa aa '' a)" == ' aa aaa' ]

# Some others to check that I'm not crazy

[ "$(./lexicosort.py bc aaaaaa abc)" == 'aaaaaa bc' ]
[ "$(./lexicosort.py bccccc aaaa abc)" == 'aaaa bccccc' ]
[ "$(./lexicosort.py bc aaaaaa bca)" == 'bc aaaaaa' ]
[ "$(./lexicosort.py bc aaaaaa cba)" == 'bc aaaaaa' ]
[ "$(./lexicosort.py '' '' ' ' abcdefg)" == '   ' ]

echo "This works!"
