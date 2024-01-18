/* code: q6_63.cpp   (v1.24.00) */
#include <iostream>
#include <list>
#include <cstdlib>
using namespace std;

int main () {
  list < int >dl;
  list < int >::iterator ptr;
  int i, r;

  for (i = 0; i < 10; i++) {
    r = rand () % 100;
    cout << "push_front: " << r << "\n";
    dl.push_front (r);
  }
  cout << "list    (" << dl.size () << ") : ";
  ptr = dl.begin ();
  while (ptr != dl.end ()) {
    cout << *ptr++ << " ";
  }
  cout << "\n";

  dl.sort (greater < int >());

  cout << "sort    (" << dl.size () << ") : ";
  ptr = dl.begin ();
  while (ptr != dl.end ()) {
    cout << *ptr++ << " ";
  }
  cout << "\n";

  dl.reverse ();
  cout << "reverse (" << dl.size () << ") : ";
  ptr = dl.begin ();
  while (ptr != dl.end ()) {
    cout << *ptr++ << " ";
  }
  cout << "\n";

  return 0;
}
