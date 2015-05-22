#!/bin/bash

echo '$0 = '$0
echo '$1 = '$1
#echo '$2 = '$2

if [ $1 == "intro" ]; then
	#python pacman.py
	#python pacman.py --frameTime 0.03 -g DirectionalGhost -p ReflexAgent -k 2
	python pacman.py --frameTime 0.03 -p ReflexAgent -k 2
	#python pacman.py --frameTime 0.1 -p ReflexAgent -l testClassic
elif [ $1 == "mM" ]; then
	python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4 -k 3
	#python pacman.py -p MinimaxAgent -a depth=3
	#python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
elif [ $1 == "ab" ]; then
	#python pacman.py -p MinimaxAgent -a depth=3 -l smallClassic
	python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
fi


: <<'END'
bigCorners.lay        mediumMaze.lay        smallSafeSearch.lay
bigMaze.lay           mediumSafeSearch.lay  smallSearch.lay
bigSafeSearch.lay     mediumScaryMaze.lay   testClassic.lay
bigSearch.lay         mediumSearch.lay      testMaze.lay
boxSearch.lay         minimaxClassic.lay    testSearch.lay
capsuleClassic.lay    oddSearch.lay         tinyCorners.lay
contestClassic.lay    openClassic.lay       tinyMaze.lay
contoursMaze.lay      openMaze.lay          tinySafeSearch.lay
greedySearch.lay      openSearch.lay        tinySearch.lay
mediumClassic.lay     originalClassic.lay   trappedClassic.lay
mediumCorners.lay     smallClassic.lay      trickyClassic.lay
mediumDottedMaze.lay  smallMaze.lay         trickySearch.lay
END

