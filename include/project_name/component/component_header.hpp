#pragma once
/// \file component_header.hpp Another header file
///
/// Detailed documentation of the file goes here

namespace project_name {

inline namespace v1 {
namespace component {

/// B struct
struct B {
  float a;  ///< A float
  int b;    ///< An int
};

/// Returns the value of B::b incremented by 1
int bar(B b) { return b.b + 1; }

}  // namespace component

}  // namespace v1
  
}  // namespace project_name
