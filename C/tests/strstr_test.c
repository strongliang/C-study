#include <stdio.h>
#include <string.h>

int main ()
{
  char str[] ="This is a line";
  char *p;
  
  p = strstr (str, "is");
  strncpy (p, "sample",5 );
  puts (str);
  
  return 0;
}
