#include <stdarg.h>
#include <stdio.h>

int sum(int*, ...);

int main () {
    int a = 2, b = 3;
    sum(&b, NULL);
    return 0;
}

int sum(int* num_args, ...) {
   int val = 0;
   va_list ap;
   int i;

   va_start(ap, num_args);
   i = *(va_arg(ap, int *));
   printf("i = %d\n", i);
   i = *(va_arg(ap, int *));
   printf("i = %d\n", i);
   va_end(ap);
}
