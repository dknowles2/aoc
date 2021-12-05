package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

var (
	useExample = flag.Bool("e", false, "Use the example dataset")
	debug      = flag.Bool("d", false, "Run in debug mode")
)

func getFilename(puzzleDay int) string {
	var suffix string
	if *useExample {
		suffix = "-example"
	}
	return fmt.Sprintf("input/%d%s.txt", puzzleDay, suffix)
}

type Pos struct {
	x, y int
}

func (p *Pos) Add(o Pos) Pos {
	return Pos{
		x: p.x + o.x,
		y: p.y + o.y,
	}
}

var dirs = []Pos{{-1, -1}, {0, -1}, {1, -1}, {-1, 0}, {1, 0}, {-1, 1}, {0, 1}, {1, 1}}

type WaitingArea struct {
	seats         map[Pos]bool
	width, height int
}

func (wa *WaitingArea) Run() int {
	var lastChanged int
	for {
		numChanged := 0
		newSeats := map[Pos]bool{}

		for p := range wa.seats {
			occ := wa.numVisiblyOccupied(p)
			if occ == 0 {
				numChanged++
				newSeats[p] = true
			} else if occ >= 5 {
				numChanged++
				newSeats[p] = false
			} else {
				newSeats[p] = wa.seats[p]
			}
		}

		wa.seats = newSeats
		if *debug {
			wa.Print()
		}
		if numChanged == lastChanged {
			return wa.countOccupied()
		}
		lastChanged = numChanged
	}
	return -1
}

func (wa *WaitingArea) numVisiblyOccupied(p Pos) int {
	var ret int
	for _, dir := range dirs {
		vp := p
		for wa.posIsValid(vp) {
			vp = vp.Add(dir)
			occ, isSeat := wa.seats[vp]
			if !isSeat {
				continue
			}
			if occ {
				ret++
			}
			break
		}
	}
	return ret
}

func (wa *WaitingArea) posIsValid(p Pos) bool {
	return p.x >= 0 && p.y >= 0 && p.x < wa.width && p.y < wa.height
}

func (wa *WaitingArea) Print() {
	for y := 0; y < wa.height; y++ {
		for x := 0; x < wa.width; x++ {
			seat, ok := wa.seats[Pos{x, y}]
			if !ok {
				fmt.Printf(".")
			} else if seat {
				fmt.Printf("#")
			} else {
				fmt.Printf("L")
			}
		}
		fmt.Printf("\n")
	}
	fmt.Printf("Num occupied: %d\n", wa.countOccupied())
}

func (wa *WaitingArea) countOccupied() int {
	var ret int
	for _, s := range wa.seats {
		if s {
			ret++
		}
	}
	return ret
}

func main() {
	flag.Parse()
	f, err := os.Open(getFilename(11))
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}

	seats := map[Pos]bool{}
	var y, width, height int

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		l := scanner.Text()
		if l == "" {
			continue
		}
		row := strings.Split(l, "")
		for x, v := range row {
			if v == "L" {
				seats[Pos{x, y}] = false
			}
		}
		width = len(row)
		y++
	}
	height = y

	wa := WaitingArea{
		seats:  seats,
		width:  width,
		height: height,
	}
	occ := wa.Run()
	fmt.Printf("Num occupied: %d\n", occ)
}
