# Copyright Louis Dionne 2015
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE.md or copy at http://boost.org/LICENSE_1_0.txt)

##############################################################################
# Setup project
##############################################################################
project(project_name CXX)
cmake_minimum_required(VERSION 3.0)
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
enable_testing()


##############################################################################
# Setup CMake options
##############################################################################
include(CMakeDependentOption)
option(PROJECT_NAME_ENABLE_VALGRID "Run the unit tests and examples under Valgrind if it is found." OFF)
option(PROJECT_NAME_ENABLE_ASAN   "Run the unit tests and examples using AddressSanitizer." OFF)
option(PROJECT_NAME_ENABLE_COVERAGE "Run the unit tests and examples with code coverage instrumentation." OFF)
option(PROJECT_NAME_ENABLE_WERROR   "Fail and stop if a warning is triggered." OFF)

##############################################################################
# Setup compiler flags (more can be set on a per-target basis or in subdirectories)
##############################################################################
# Compiler flags:
include(CheckCXXCompilerFlag)
macro(project_name_append_flag testname flag)
    check_cxx_compiler_flag(${flag} ${testname})
    if (${testname})
        add_compile_options(${flag})
    endif()
endmacro()

# Language flag: version of the C++ standard to use
project_name_append_flag(PROJECT_NAME_HAS_STDCXX14 -std=c++14)

# PITA warning flags:
project_name_append_flag(PROJECT_NAME_HAS_WSHADOW -Wshadow)
project_name_append_flag(PROJECT_NAME_HAS_WUNUSED -Wunused)
project_name_append_flag(PROJECT_NAME_HAS_WUNUSED_FUNCTION -Wunused-function)
project_name_append_flag(PROJECT_NAME_HAS_WUNUSED_LABEL -Wunused-label)
project_name_append_flag(PROJECT_NAME_HAS_WUNUSED_PARAMETER -Wunused-parameter)
project_name_append_flag(PROJECT_NAME_HAS_WUNUSED_VALUE -Wunused-value)
project_name_append_flag(PROJECT_NAME_HAS_WUNUSED_VARIABLE -Wunused-variable)

# Warning flags:
project_name_append_flag(PROJECT_NAME_HAS_WALL -Wall)
project_name_append_flag(PROJECT_NAME_HAS_WEXTRA -Wextra)
project_name_append_flag(PROJECT_NAME_HAS_WDEPRECATED -Wdeprecated)
project_name_append_flag(PROJECT_NAME_HAS_WDOCUMENTATION -Wdocumentation)
project_name_append_flag(PROJECT_NAME_HAS_WCOMMENT -Wcomment)
project_name_append_flag(PROJECT_NAME_HAS_PEDANTIC -Wpedantic)
project_name_append_flag(PROJECT_NAME_HAS_WSTACK_PROTECTOR -Wstack-protector)
project_name_append_flag(PROJECT_NAME_HAS_WSTRICT_ALIASING "-Wstrict-aliasing=2")
project_name_append_flag(PROJECT_NAME_HAS_WSTRICT_OVERFLOW "-Wstrict-overflow=5")
project_name_append_flag(PROJECT_NAME_HAS_WDISABLED_OPTIMIZATION -Wdisabled-optimization)
project_name_append_flag(PROJECT_NAME_HAS_WINLINE -Winline)
project_name_append_flag(PROJECT_NAME_HAS_WRETURN_TYPE -Wreturn-type)
project_name_append_flag(PROJECT_NAME_HAS_WCAST_ALIGN -Wcast-align)
project_name_append_flag(PROJECT_NAME_HAS_WCAST_QUAL -Wcast-qual)
project_name_append_flag(PROJECT_NAME_HAS_WSIGN_COMPARE -Wsign-compare)
project_name_append_flag(PROJECT_NAME_HAS_WSIGN_PROMO -Wsign-promo)
project_name_append_flag(PROJECT_NAME_HAS_WFORMAT "-Wformat=2")
project_name_append_flag(PROJECT_NAME_HAS_WFORMAT_NONLITERAL -Wformat-nonliteral)
project_name_append_flag(PROJECT_NAME_HAS_WFORMAT_SECURITY -Wformat-security)
project_name_append_flag(PROJECT_NAME_HAS_WFORMAT_Y2K -Wformat-y2k)
project_name_append_flag(PROJECT_NAME_HAS_WMISSING_BRACES -Wmissing-braces)
project_name_append_flag(PROJECT_NAME_HAS_WMISSING_FIELD_INITIALIZERS -Wmissing-field-initializers)
project_name_append_flag(PROJECT_NAME_HAS_WMISSING_INCLUDE_DIRS -Wmissing-include-dirs)
project_name_append_flag(PROJECT_NAME_HAS_WOVERLOADED_VIRTUAL -Woverloaded-virtual)
project_name_append_flag(PROJECT_NAME_HAS_WCHAR_SUBSCRIPTS -Wchar-subscripts)
project_name_append_flag(PROJECT_NAME_HAS_WFLOAT_EQUAL -Wfloat-equal)
project_name_append_flag(PROJECT_NAME_HAS_WPOINTER_ARITH -Wpointer-arith)
project_name_append_flag(PROJECT_NAME_HAS_WINVALID_PCH -Winvalid-pch)
project_name_append_flag(PROJECT_NAME_HAS_WIMPORT -Wimport)
project_name_append_flag(PROJECT_NAME_HAS_WINIT_SELF -Winit-self)
project_name_append_flag(PROJECT_NAME_HAS_WREDUNDANT_DECLS -Wredundant-decls)
project_name_append_flag(PROJECT_NAME_HAS_WPACKED -Wpacked)
project_name_append_flag(PROJECT_NAME_HAS_WPARENTHESES -Wparentheses)
project_name_append_flag(PROJECT_NAME_HAS_WSEQUENCE_POINT -Wsequence-point)
project_name_append_flag(PROJECT_NAME_HAS_WSWITCH -Wswitch)
project_name_append_flag(PROJECT_NAME_HAS_WSWITCH_DEFAULT -Wswitch-default)
project_name_append_flag(PROJECT_NAME_HAS_WTRIGRAPHS -Wtrigraphs)
project_name_append_flag(PROJECT_NAME_HAS_WUNINITIALIZED -Wuninitialized)
project_name_append_flag(PROJECT_NAME_HAS_WUNKNOWN_PRAGMAS -Wunknown-pragmas)
project_name_append_flag(PROJECT_NAME_HAS_WUNREACHABLE_CODE -Wunreachable-code)
project_name_append_flag(PROJECT_NAME_HAS_WVARIADIC_MACROS -Wvariadic-macros)
project_name_append_flag(PROJECT_NAME_HAS_WVOLATILE_REGISTER_VAR -Wvolatile-register-var)
project_name_append_flag(PROJECT_NAME_HAS_WWRITE_STRINGS -Wwrite-strings)
project_name_append_flag(PROJECT_NAME_HAS_WNO_ATTRIBUTES -Wno-attributes)
project_name_append_flag(PROJECT_NAME_HAS_WUNNEEDED_INTERNAL_DECLARATION -Wunneeded-internal-declaration)

# Template diagnostic flags
project_name_append_flag(PROJECT_NAME_HAS_FDIAGNOSTIC_SHOW_TEMPLATE_TREE -fdiagnostics-show-template-tree)
project_name_append_flag(PROJECT_NAME_HAS_FTEMPLATE_BACKTRACE_LIMIT "-ftemplate-backtrace-limit=0")
project_name_append_flag(PROJECT_NAME_HAS___EXTERN_ALWAYS_INLINE -D__extern_always_inline=inline)

# Compiler flags controlled by CMake options above
if (PROJECT_NAME_ENABLE_WERROR)
    project_name_append_flag(PROJECT_NAME_HAS_WERROR -Werror)
    project_name_append_flag(PROJECT_NAME_HAS_WX -WX)
endif()

##############################################################################
# Search for packages.
#
# Behavior when the package is found or not is customized at the
# point where the package is required.
##############################################################################
#find_package(Boost)
# find_package(Doxygen)
# find_package(Git)
# find_package(Meta)
# find_package(MPL11)
# find_package(PythonInterp 2.7)
# find_package(Ruby 2.1)

# if (PROJECT_NAME_ENABLE_VALGRIND)
#     find_package(Valgrind REQUIRED)
# endif()

# if (NOT ${Boost_FOUND})
#     message(WARNING
#         "The Boost library headers were not found; targets depending "
#         "on Boost won't be available.")
# endif()

# if (GIT_FOUND)
#     execute_process(
#         COMMAND ${GIT_EXECUTABLE} rev-parse --short HEAD
#         OUTPUT_VARIABLE BOOST_HANA_CURRENT_COMMIT
#         OUTPUT_STRIP_TRAILING_WHITESPACE
#         WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
# endif()


##############################################################################
# Setup the URL to the official repository on GitHub.
#
# If there is a GITHUB_TOKEN environment variable, we assume this token allows
# us to push to the GitHub repository and we use that in the URL. This token
# will give us push access for updating the 'gh-pages' branch and doing other
# useful things e.g. from Travis. Otherwise, if there's no such environment
# variable, the URL just refers to the GitHub repository without authentication.
# In this case, we'll be asked for our username and password when/if we try to
# push to the repository.
##############################################################################
if (DEFINED ENV{GITHUB_TOKEN})
    set(BOOST_HANA_ORIGIN_URL "https://github_user:$ENV{GITHUB_TOKEN}@github.com/github_user/project_name")
else()
    set(BOOST_HANA_ORIGIN_URL "https://github.com/github_user/project_name")
endif()


##############################################################################
# Setup custom functions to ease the creation of targets
##############################################################################
#   boost_hana_target_name_for(<output variable> <source file> [ext])
#
# Return the target name associated to a source file. If the path of the
# source file relative from the root of project_name is `path/to/source/file.ext`,
# the target name associated to it will be `path.to.source.file`.
#
# The extension of the file should be specified as a last argument. If no
# extension is specified, the `.cpp` extension is assumed.
function(project_name_target_name_for out file)
    if (NOT ARGV2)
        set(_extension ".cpp")
    else()
        set(_extension "${ARGV2}")
    endif()

    file(RELATIVE_PATH _relative ${project_name_SOURCE_DIR} ${file})
    string(REPLACE "${_extension}" "" _name ${_relative})
    string(REGEX REPLACE "/" "." _name ${_name})
    set(${out} "${_name}" PARENT_SCOPE)
endfunction()

#   project_name_add_test(<name> <command> [<arg>...])
#
# Creates a test called `name`, which runs the given `command` with the given
# `arg`uments. However, if `project_name_ENABLE_VALGRIND` is set to `ON`, the
# test will run the provided command under the memory checker.
function(project_name_add_test name)
    if (PROJECT_NAME_ENABLE_VALGRIND)
        add_test(${name}
            ${Valgrind_EXECUTABLE} --leak-check=full --error-exitcode=1 ${ARGN})
    else()
        add_test(${name} ${ARGN})
    endif()
endfunction()

#   project_name_list_remove_glob(<list> <GLOB|GLOB_RECURSE> [globbing expressions]...)
#
# Generates a list of files matching the given glob expressions, and remove
# the matched elements from the given <list>.
macro(project_name_list_remove_glob list glob)
    file(${glob} _bhlrg10321023_avoid_macro_clash_matches ${ARGN})
    list(REMOVE_ITEM ${list} ${_bhlrg10321023_avoid_macro_clash_matches})
endmacro()


##############################################################################
# Setup subdirectories
##############################################################################
#add_subdirectory(benchmark)
#add_subdirectory(doc)
add_subdirectory(example)
add_subdirectory(test)


##############################################################################
# Setup the `check` target to build and then run all the tests and examples.
##############################################################################
add_custom_target(check ALL
    COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS tests examples
    COMMENT "Build and then run all the tests and examples.")

