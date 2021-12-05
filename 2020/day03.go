package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strings"
)

type Slope struct {
	mx, my int
}

type Map struct {
	tiles [][]string
	x, y  int
}

func (m *Map) AddRow(row string) {
	m.tiles = append(m.tiles, strings.Split(row, ""))
}

func (m *Map) Traverse(mx, my int, print bool) int {
	var numTrees int
	px := mx
	py := my
	for y := range m.tiles {
		for x, t := range m.expandRow(y, mx, my) {
			if y == py && x == px {
				px += mx
				py += my
				if t == "#" {
					numTrees++
					t = "X"
				} else {
					t = "O"
				}
			}
			if print {
				fmt.Printf("%s", t)
			}
		}
		if print {
			fmt.Printf("\n")
		}
	}
	return numTrees
}

func (m *Map) expandRow(y, mx, my int) []string {
	var row []string
	width := len(m.tiles[y])
	totalWidth := len(m.tiles) * my * mx
	repeat := int(math.Ceil(float64(totalWidth) / float64(width)))
	for i := 0; i < repeat; i++ {
		row = append(row, m.tiles[y]...)
	}
	return row
}

func main() {
	f, err := os.Open("input/03.txt")
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}
	scanner := bufio.NewScanner(f)

	m := &Map{}
	for scanner.Scan() {
		m.AddRow(scanner.Text())
	}

	p := 1
	for _, slope := range []Slope{{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}} {
		numTrees := m.Traverse(slope.mx, slope.my, false)
		fmt.Printf("[%d, %d] :: %d\n", slope.mx, slope.my, numTrees)
		p *= numTrees
	}
	fmt.Printf("Product: %d\n", p)
}
