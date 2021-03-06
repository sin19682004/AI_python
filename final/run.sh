#!/bin/bash

echo '$0 = '$0
echo '$1 = '$1

if [ $1 == "dfs" ]; then
	python pacman.py --frameTime 0.01 -l bigMaze -z .5 -p SearchAgent -a fn=dfs
	python pacman.py --frameTime 0.01 -l contoursMaze -z .5 -p SearchAgent -a fn=dfs
elif [ $1 == "ucf" ]; then
	python pacman.py --frameTime 0.1 -l mediumMaze -p SearchAgent -a fn=ucs
	python pacman.py --frameTime 0.1 -l mediumDottedMaze -p StayEastSearchAgent
	python pacman.py --frameTime 0.1 -l mediumScaryMaze -p StayWestSearchAgent
elif [ $1 == "aStar" ]; then
	#python pacman.py --frameTime 0.01 -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
	#python pacman.py --frameTime 0.01 -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
	#python pacman.py --frameTime 0.01 -l contoursMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
	
	#python pacman.py --frameTime 0.1 -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
	#python pacman.py --frameTime 0.1 -l contoursMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
	#python pacman.py --frameTime 0.1 -l mediumMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
	python pacman.py --frameTime 0.1 -l mediumDottedMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
	python pacman.py --frameTime 0.1 -l mediumScaryMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
	#python pacman.py --frameTime 0.1 -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
	#python pacman.py --frameTime 0.1 -l smallMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
	#python pacman.py --frameTime 0.1 -l testMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
	#python pacman.py --frameTime 0.1 -l myMaze -z .5 -p SearchAgent -a fn=astar,heuristic=euclideanHeuristic
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

