# C++ Skeleton <a href="https://travis-ci.org/gnzlbg/cpp_skeleton" target="_blank">![Build Status][badge.Travis]</a>
> Your standard C++ project skeleton

## Disclaimer

This project is a fork from Boost.Hana's build system, so most of the credit
goes to Louis Dione for the great work he is doing. It also steals some ideas
from the build systems of Paul Futz II FIT's library and Eric Niebler's range-v3
library.

## Overview

Setting up a modern C++ project with Continuous Integration is a time-consuming
task. The amount of tools available is daunting, and one really wants to use
them all: cmake as a meta-build-system, gh-pages and doxygen for documentation,
travis-ci for running your unit-tests and performing continuous integration,
coveralls for displaying code coverage reports, clang-format for
auto-formatting, valgrind, sanitizers, swang, and many more!

The aim of this project is to give you a fully-functional starting point for
your own projects, so that you can skip setting up most of these tools
correctly.

Right now it uses:
- cmake as a meta-build system
- doxygen for embedded documentation
- travis-ci for continuous integration: running unit-testing, benchmarks, and
  updating the website

and optionally it can use:
- clang-format for auto-formatting the code

In the future it should also provide:
- coveralls for code coverage
- simple configuration of the following external packages:
  - Catch for unit-testing
  - range-v3 (which includes meta)
  - Eggs.Variant
  - Boost.Hana
  - nonious/CPM for benchmarking

The directory structure is as follows:

```shell
bench/               : Bench-mark files
cmake/               : CMake files
include/             : Header files go here
    project_name/    : Project header files
src/                 : Source files
test/                : Unit-tests 
site/                : Website
CMakeLists.txt       : Main CMake file
.clang-format        : Specifies the formatting style
.travis.yml          : Sets up travis
```

## Getting started

1. Fork this repository and check-out your fork.
2. Run `bootstrap.py` script to configure it to your needs and commit your
   changes to your repository.
3. Start working on your project.

<!-- Links -->
[badge.Gitter]: https://img.shields.io/badge/gitter-join%20chat-blue.svg
[badge.Travis]: https://travis-ci.org/ldionne/hana.svg?branch=master
