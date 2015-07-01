# C++ Skeleton <a href="https://travis-ci.org/gnzlbg/cpp_skeleton" target="_blank">![Build Status][badge.Travis]</a> <a href="https://coveralls.io/r/gnzlbg/cpp_skeleton" target="_blank">![Coverage Status][badge.Coveralls]</a>
> Your standard C++ project skeleton

## Disclaimer

This project is a fork from [Hana][]'s build system, so all of the credit
goes to [Louis Dione][] for the great work he is doing. It also steals some
ideas from the build systems of [Paul Fultz II][] [FIT][]'s library and
[Eric Niebler][]'s [range-v3][] library.

## Overview

Setting up a modern C++ project with Continuous Integration is a time-consuming
task. The amount of tools available is daunting, and one really wants to use
them all: [CMake][], [gh-pages][] and [Doxygen][] for documentation,
[Travis-CI][] for continuous integration, [Coveralls][] for displaying code
coverage reports, [clang-format][] for auto-formatting, [valgrind][],
[sanitizers][], [swang][], [static-analyzer][], and many more!

The aim of this project is to give you a fully-functional starting point for
your own projects, so that you can skip setting up most of these tools
correctly.

## What you get

- [CMake][] as a meta-build system:
  - debug/release builds,
  - high-optimization for release builds,
  - extensive warnings enabled out-of-the-box,
  - support for running tests and examples with [valgrind][] and [AddressSanitizer][],
  - support for generating code coverage from tests and examples.
- [Travis-CI][] is used for unit-testing:
  - compilers: [clang][]-3.7, [gcc][]-5.0,
  - test your code in debug/release, w/o [valgrind][], w/o [AddressSanitizer][],
  - uploads code coverage automatically to [Coveralls][].
- [Coveralls][] shows per-line code coverage.
- Automatic [Doxygen][] documentation generation and deployment to [gh-pages][].

## Getting started

1. Fork this repository and check-out your fork.
2. Add your repository to [Travis-CI][] and [Coveralls][].
3. Run `bootstrap.py` script to configure it to your needs.
   - Replace the secure token with your own and create a gh-pages branch that is empty.
4. Commit your changes to your repository (including the gh-pages branch).
5. Start working on your project.

### CMake configuration options

- `PROJECT_NAME_ENABLE_VALGRIND`: Run the unit tests and examples under [valgrind][] if it is found.
- `PROJECT_NAME_ENABLE_ASAN`: Run the unit tests and examples using [AddressSanitizer][].
- `PROJECT_NAME_ENABLE_COVERAGE`: Run the unit tests and examples with code coverage instrumentation.
- `PROJECT_NAME_ENABLE_WERROR`: Fail and stop if a warning is triggered.
- `PROJECT_NAME_ENABLE_DEBUG_INFORMATION`: Includes debug information in the binaries.
- `PROJECT_NAME_ENABLE_ASSERTIONS`: Enables assertions.

### CMake targets

- `make`: Compiles top-level targets.
- `make tests`: Compiles the tests.
- `make examples`: Compiles the examples.
- `make check`: Runs the test and the examples.
- `make doc`: Generates the documentation.

## Directory structure

The directory structure is as follows:

```text
benchmark/            : Benchmarks (reserved for future usage)
cmake/                : CMake files
include/project_name/ : Project header files
site/                 : website (reserved for future usage)
src/                  : Source files (reserved for future usage)
test/                 : Unit-tests 
.clang-format         : clang-format configuration
.travis.yml           : Travis-CI configuration
.gitignore            : With C++ defaults
CMakeLists.txt        : CMake configuration
```

## What remains to be done

- Targets to check the format and reformat your code automatically.
- Semantic versioning.
- Provide FindLib.cmake files for common libraries that automatically.
get the last version from their repository:
    - [ASIO][],
    - [Catch][],
    - [cppformat][],
    - [docopt][],
    - [Eigen3][],
    - [Eggs.Variant][].
    - [FIT][],
    - [Hana][],
    - [json][],
    - [meta][],
    - [range-v3][],
    - [spdlog][],
    - [Thread Building Blocks][].
- Benchmarking targets.
- Performance tracking over git revisions (and automatic upload to gh-pages).
- [static-analyzer][].
- [swang][].
- [ThreadSanitizer][].

<!-- Links -->
[badge.Travis]: https://travis-ci.org/gnzlbg/cpp_skeleton.svg?branch=master
[badge.Coveralls]: https://coveralls.io/repos/gnzlbg/cpp_skeleton/badge.svg
[Hana]: https://github.com/ldionne/hana
[Louis Dione]: http://ldionne.com/
[FIT]: https://github.com/pfultz2/Fit
[Paul Fultz II]: http://pfultz2.com/blog/
[Eric Niebler]: http://ericniebler.com/
[range-v3]: https://github.com/ericniebler/range-v3
[meta]: https://github.com/ericniebler/meta
[Travis-CI]: https://travis-ci.org/
[Coveralls]: https://coveralls.io/
[CMake]: http://www.cmake.org/
[gh-pages]: https://pages.github.com/
[Doxygen]: http://www.stack.nl/~dimitri/doxygen/
[valgrind]: http://valgrind.org/
[AddressSanitizer]: http://clang.llvm.org/docs/AddressSanitizer.html
[ThreadSanitizer]: http://clang.llvm.org/docs/ThreadSanitizer.html
[sanitizers]: http://clang.llvm.org/docs/index.html
[swang]: https://github.com/berenm/swang
[static-analyzer]: http://clang-analyzer.llvm.org/
[clang]: http://clang.llvm.org/
[gcc]: https://gcc.gnu.org/
[Eggs.Variant]: https://github.com/eggs-cpp/variant
[Eigen3]: http://eigen.tuxfamily.org/
[cppformat]: https://github.com/cppformat/cppformat
[spdlog]: https://github.com/gabime/spdlog
[FIT]: https://github.com/pfultz2/Fit
[Thread Building Blocks]: https://www.threadingbuildingblocks.org/
[clang-format]: http://clang.llvm.org/docs/ClangFormat.html
[Catch]: https://github.com/philsquared/Catch
[ASIO]: https://think-async.com/
[docopt]: https://github.com/docopt/docopt.cpp
[json]: https://github.com/nlohmann/json
