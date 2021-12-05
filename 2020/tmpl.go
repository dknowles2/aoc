package main

import (
	"flag"
	"fmt"
)

var (
	useExample = flag.Bool("e", false, "Use the example dataset")
	debug      = flag.Bool("d", false, "Run in debug mode")
	part2      = flag.Bool("2", false, "Run part 2 of the puzzle")
)

func getFilename(puzzleDay int) string {
	var suffix string
	if *useExample {
		suffix = "-example"
	}
	return fmt.Sprintf("input/%d%s.txt", puzzleDay, suffix)
}

func main() {
	flag.Parse()
}
