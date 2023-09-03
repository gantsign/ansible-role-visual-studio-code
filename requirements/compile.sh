#!/bin/bash

dir="$(cd -P -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"

cd "$dir" || exit 1

find . -name '*.in' -exec pip-compile --resolver=backtracking --generate-hashes '{}' \;

pip-compile --resolver=backtracking dev.in
