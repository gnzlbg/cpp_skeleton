# Copyright Louis Dionne 2015
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE.md or copy at http://boost.org/LICENSE_1_0.txt)

##############################################################################
# Setup custom functions, master targets and file lists for the unit tests
##############################################################################
add_custom_target(test.headers
  COMMENT "Build all the header-inclusion unit tests.")

add_custom_target(tests
  DEPENDS test.headers
  COMMENT "Build all the unit tests.")

#   project_name_add_unit_test(<name> ...)
#
# Equivalent to `project_name_add_test`, except the test is also added as a
# dependency of the `tests` target.
function(project_name_add_unit_test name)
  project_name_add_test(${ARGV})
  add_dependencies(tests ${name})
endfunction()

#   project_name_add_header_test(<header-name>)
#
# Add a unit test for the public header file `header-name`, which must be a
# relative path from project_name's include directory, e.g. `project_name/project_name.hpp`.
#
# This function creates an executable named `header.header-name` and a test
# of the same name. The only source file of the executable contains an empty
# `main` and it includes the `header-name` file. This is used to make sure
# that including any public header works properly. Also, the
# `header.header-name` target is made a dependency of the `headers` target.
function(project_name_add_header_test header)
  string(REGEX REPLACE "/" "." _target "${header}")
  if (NOT EXISTS "${CMAKE_CURRENT_BINARY_DIR}/header/${header}.cpp")
    file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/header/${header}.cpp" "
            #include <${header}>
            int main() { return 0; }
        ")
  endif()
  add_executable(test.header.${_target} EXCLUDE_FROM_ALL
    "${CMAKE_CURRENT_BINARY_DIR}/header/${header}.cpp")
  project_name_add_test(test.header.${_target}
    ${CMAKE_CURRENT_BINARY_DIR}/test.header.${_target})
  add_dependencies(test.headers test.header.${_target})
endfunction()

# A list of all the test files
file(GLOB_RECURSE PROJECT_NAME_TEST_SOURCES "${project_name_SOURCE_DIR}/test/*.cpp")

# A list of all the public headers
file(GLOB_RECURSE PROJECT_NAME_PUBLIC_HEADERS "${project_name_SOURCE_DIR}/include/*.hpp")


##############################################################################
# Include directories
##############################################################################
include_directories(${project_name_SOURCE_DIR}/include)
include_directories(${CMAKE_CURRENT_LIST_DIR}/include)
include_directories(${CMAKE_CURRENT_LIST_DIR})

##############################################################################
# Generate tests that include each public header
##############################################################################
foreach(_header IN LISTS PROJECT_NAME_PUBLIC_HEADERS)
  file(RELATIVE_PATH _relative "${project_name_SOURCE_DIR}/include" "${_header}")
  project_name_add_header_test("${_relative}")
endforeach()

##############################################################################
# Add all the unit tests
##############################################################################
foreach(_file IN LISTS PROJECT_NAME_TEST_SOURCES)
  file(READ "${_file}" _contents)
  project_name_target_name_for(_target "${_file}")

  add_executable(${_target} EXCLUDE_FROM_ALL "${_file}")
  project_name_add_unit_test(${_target} ${CMAKE_CURRENT_BINARY_DIR}/${_target})
endforeach()