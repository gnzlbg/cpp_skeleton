# Modern C++ project skeleton

Setting up a modern C++ project with Continuous Integration is a time-consuming
PITA. The aim of this project is to give you a fully-functional starting point
for your own projects.

It is a modified version of the structure of Boost.Hana by Louis Dione and is
released under the liberal Boost Software license. All the credit goes to Louis,
who I'm sure fighted for a very long time to get all this to work.

It uses:
- cmake as a meta-build system
- Catch for unit-testing
- doxygen for embedded documentation
- clang-format for auto-formatting the code
- travis-ci for continuous integration: running unit-testing, benchmarks, and
  updating the website
- coveralls for code coverage

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

After forking the project there are a couple of things that need to be set-up.
This is a not-yet fully comprehensive list:

- In the `CMakeLists.txt` file:
  - name of the project
- name of the `include/project_name` directory and `project_name.hpp` files
- formatting style in the `.clang-format` file


## TODOS

- support non-header-only libraries as well (PR are very welcome).
- provide a script that sets the project for you
