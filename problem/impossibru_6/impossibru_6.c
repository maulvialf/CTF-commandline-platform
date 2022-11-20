#include <stdio.h>
#include <stdlib.h>

#define FLAG_SIZE 69

int glob_x = 0;
int glob_y = 0;

void setup()
{
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
}

int main(int argc, char const *argv[])
{
  char username[255];

  setup();

  scanf("%s", username);
  printf("Welcome, %s!\n", username);

  puts("Nothing todo here. :\\");

  return 0;
}