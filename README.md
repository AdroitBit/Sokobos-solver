# Sokobos-solver
A puzzle solver for the game Sokobos that inspired by Sokoban

[Sokobos' steam page](https://store.steampowered.com/app/1655890/Sokobos/)

Some part of this project is still unfinished. But many parts has been coded.

This project utilize A* algorithm to find the solution of the given layout.

No special UI yet, but there is a function to preview the programmed layout specifically in "State" class.

Upon testing with real layout from the game itself, The result is still not usable. Due to the reason that the program take too long to find solution. This is because Sokobos introduce a lot of possibilities with its hazards from original Sokoban, resulting in many state explosion.

So The program needs a lot of improvements to handle state explosion.

## Deadlock detection
TBC

## A* algorithm usage
TBC