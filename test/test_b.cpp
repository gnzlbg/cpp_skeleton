#include <project_name/test_header.hpp>

using namespace project_name;

int main() {
  A a{0, 1};

  if (foo(a) == 1) {
    return 0;
  } else {
    return 1;
  }
}
