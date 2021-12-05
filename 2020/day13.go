package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"math"
	"strconv"
	"strings"
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

func getBuses(s string) []int {
	ss := strings.Split(strings.TrimSpace(s), ",")
	ret := make([]int, len(ss))
	for _, b := range ss {
		if b == "x" {
			continue
		}
		bi, _ := strconv.Atoi(b)
		ret = append(ret, bi)
	}
	return ret
}

func runPart1(contents []string) {
	t, _ := strconv.Atoi(contents[0])
	if *debug {
		fmt.Printf("t = %d\n", t)
	}

	var minBus int
	min := math.MaxInt32 // arbitrary large number
	for _, bs := range strings.Split(strings.TrimSpace(contents[1]), ",") {
		if bs == "x" {
			continue
		}
		b, _ := strconv.Atoi(bs)
		diff := b - (t % b)
		if diff < min {
			min = diff
			minBus = b
		}
	}
	fmt.Printf("\n\nPART ONE: %d * %d = %d", minBus, min, minBus*min)
}

type Bus struct {
	i, id, offset, v int
	prev             *Bus
}

func (b *Bus) String() string {
	return fmt.Sprintf("%+v", *b)
}

func (b *Bus) Fix() {
	if b.prev == nil {
		return
	}
	for b.v-b.prev.v != b.offset {
		if b.v < b.prev.v {
			b.v = b.id + b.id*int(math.Floor(float64(b.prev.v)/float64(b.id)))
		} else {
			b.prev.v += b.prev.id
		}
		b.prev.Fix()
	}
}

func runPart2(contents []string) {
	// var lines []int
	// buses := map[int]int{}
	var buses []int
	var numLines int
	startTs := 1
	product := 1

	for i, n := range strings.Split(strings.TrimSpace(contents[1]), ",") {
		numLines++
		if n == "x" {
			continue
		}
		b, _ := strconv.Atoi(n)
		buses = append(buses, b)
		if *debug {
			fmt.Printf("startTs = %d :: i = %d :: b = %d\n", startTs, i+1, b)
		}
		for (startTs+b)%(i+1) != 0 {
			startTs += product
			fmt.Printf("    --> %d\n", startTs)
		}
		product *= b
	}

	fmt.Printf("time\t")
	for _, b := range buses {
		fmt.Printf("bus %2d\t", b)
	}
	for i := 0; i < numLines; i++ {
		t := startTs + i
		fmt.Printf("%d\t", t)
		for _, b := range buses {
			d := "."
			if b%i == 0 {
				d = "D"
			}
			fmt.Printf("  %s  \t", d)
		}
		fmt.Printf("\n")
	}
}

func main() {
	flag.Parse()
	content, err := ioutil.ReadFile(getFilename(13))
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}
	contentS := strings.SplitN(string(content), "\n", 2)
	if *part2 {
		runPart2(contentS)
	} else {
		runPart1(contentS)
	}
}
