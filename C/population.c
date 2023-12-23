#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);
    // TODO: Prompt for end size

    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < start);

    // TODO: Calculate number of years until we reach threshold
    // Keep track of number of years (i.e. set years = 0 at the start)
    int years = 0;

    // Update population until we reach threshold (years++ means 1 additional year has passed therefore increase the value of years
    // by 1)
    while (start < end)
    {
        start = start + (start / 3) - (start / 4);
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}
