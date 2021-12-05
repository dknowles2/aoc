package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"sort"
	"strings"
)

type Seat struct {
	row, col, id int
}

func parse(p string) Seat {
	var s Seat
	min := 0
	max := 127
	for i := 0; i < 6; i++ {
		c := p[i]
		if c == 'F' {
			max = min + ((max - min) / 2)
		} else {
			min = min + ((max - min) / 2) + 1
		}
		// fmt.Printf("%d (%s) min=%d max=%d\n", i, string(c), min, max)
	}
	// fmt.Printf("%d (%s) min=%d max=%d\n", 6, string(p[6]), min, max)
	if p[6] == 'F' {
		s.row = min
	} else {
		s.row = max
	}

	min = 0
	max = 7
	for i := 7; i < 9; i++ {
		c := p[i]
		if c == 'L' {
			max = min + ((max - min) / 2)
		} else {
			min = min + ((max - min) / 2) + 1
		}
		// fmt.Printf("%d (%s) min=%d max=%d\n", i, string(c), min, max)
	}
	if p[9] == 'L' {
		s.col = min
	} else {
		s.col = max
	}

	s.id = s.row*8 + s.col
	return s
}

func main() {
	// Sanity checks:
	fmt.Println(parse("FBFBBFFRLR"))
	fmt.Println(parse("BFFFBBFRRR"))
	fmt.Println(parse("FFFBBBFRRR"))
	fmt.Println(parse("BBFFBBFRLL"))

	contents, err := ioutil.ReadFile("input/05.txt")
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}
	var max int
	var allIds []int
	for _, line := range strings.Split(string(contents), "\n") {
		if line == "" {
			continue
		}
		seat := parse(line)
		allIds = append(allIds, seat.id)
		if seat.id > max {
			max = seat.id
		}
	}
	fmt.Printf("Largest id: %d\n", max)
	sort.Ints(allIds)
	fmt.Printf("All seats: %v\n", allIds)

	for i, id := range allIds {
		if i == 0 {
			continue
		}

		if id-1 != allIds[i-1] {
			fmt.Printf("My seat: %d\n", id-1)
			break
		}
	}
}
