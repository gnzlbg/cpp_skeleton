# C++ Skeleton <a href="https://travis-ci.org/gnzlbg/cpp_skeleton" target="_blank">![Build Status][badge.Travis]</a> <a href="https://coveralls.io/r/gnzlbg/cpp_skeleton" target="_blank">![Coverage Status][badge.Coveralls]</a>
> Your standard C++ project skeleton

## Disclaimer

This project is a fork from [Boost.Hana][]'s build system, so all of the credit
goes to [Louis Dione][] for the great work he is doing. It also steals some
ideas from the build systems of [Paul Fultz II][] [FIT][]'s library and
[Eric Niebler][]'s [range-v3][] library.

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

## Getting started

1. Fork this repository and check-out your fork.
2. Add your repository to [travis-ci][] and [coveralls][].
3. Run `bootstrap.py` script to configure it to your needs and commit your
changes to your repository.
4. Start working on your project.

## Details

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

<!-- Links -->
[badge.Travis]: https://travis-ci.org/gnzlbg/cpp_skeleton.svg?branch=master
[badge.Coveralls]: https://coveralls.io/repos/gnzlbg/cpp_skeleton/badge.svg
[Boost.Hana]: https://github.com/ldionne/hana
[Louis Dione]: http://ldionne.com/
[FIT]: https://github.com/pfultz2/Fit
[Paul Fultz II]: http://pfultz2.com/blog/
[Eric Niebler]: http://ericniebler.com/
[range-v3]: https://github.com/ericniebler/range-v3
[travis-ci]: https://travis-ci.org/
[coveralls]: https://coveralls.io/
