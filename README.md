# Modern C++ header-only project skeletton

Setting up Continuous Integration tools for modern header-only C++ libraries can be a time-consuming PITA.
The aim of this project is to give you a fully-functional starting point for your own libraries. 

It is a modified version of the structure of Boost.Hana by Louis Dione and is released under the liberal Boost Software license.
All the credit goes to Louis, who I'm sure fighted for a very long time to get all this to work. 

TODO: support non-header-only libraries as well (PR are very welcome).

It uses:
- cmake as a meta-build system
- doxygen for embedded documentation
- travis-ci for unit-testing, benchmarking, and updating the website
- coveralls for code coverage

The directory structure is as follows:

```shell
bench/               : Bench-mark files
cmake/               : FindLib.cmake used to get external libraries
include/             : Header files go here
    project_name/    : Project header files
src/                 : Source files
test/                : Unit-tests 
site/                : Website
```
