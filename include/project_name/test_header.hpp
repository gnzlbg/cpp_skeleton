#pragma once
/// \file test_header.hpp A header file

/// Project namespace
///
/// All the code is in this namespace
namespace project_name {

/// Version 1 of the project
///
/// Inline namespaces allow providing different versions of the code
/// without breaking the ABI.
inline namespace v1 {

/// A struct (brief documentation goes in the first paragraph)
///
/// Detailed documentation follows
struct A {
  int a;   ///< Inline documentation for member a
  float b; ///< Member b
};

} // namespace v1
} // namespace project_name
