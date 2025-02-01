// Name: endian.c
// Compile: gcc -o endian endian.c

#include <stdio.h>
int main() {
  unsigned long long n = 0x4011dd;

  printf("Low <-----------------------> High\n");

  for (int i = 0; i < 8; i++) printf("0x%hhx ", *((unsigned char*)(&n) + i));

  return 0;
}
