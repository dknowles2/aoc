package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

var (
	useExample = flag.Bool("e", false, "Use the example dataset")
	debug      = flag.Bool("d", false, "Run in debug mode")
	part2      = flag.Bool("2", false, "Run part 2 of the puzzle")
)

type Action func(int)

type Instruction struct {
	action string
	value  int
}

func (i Instruction) String() string {
	return fmt.Sprintf("%s%04d", i.action, i.value)
}

type Pos struct {
	x, y int
}

func (p *Pos) Add(o Pos) {
	p.x += o.x
	p.y += o.y
}

func (p *Pos) Rotate(d int) {
	r := float64(d) * math.Pi / 180.0
	fx, fy := float64(p.x), float64(p.y)
	p.x = int(math.Round(fx*math.Cos(r) - fy*math.Sin(r)))
	p.y = int(math.Round(fy*math.Cos(r) + fx*math.Sin(r)))
}

func (p *Pos) Manhattan() int {
	abs := func(x int) int { return int(math.Abs(float64(x))) }
	return abs(p.x) + abs(p.y)
}

type Navigator struct {
	p, w Pos
}

func (n *Navigator) Run(inst []Instruction) int {
	actions := map[string]func(int){
		"N": n.north,
		"S": n.south,
		"E": n.east,
		"W": n.west,
		"L": n.left,
		"R": n.right,
		"F": n.forward,
	}
	for _, i := range inst {
		if *debug {
			fmt.Printf("%s", i)
		}
		actions[i.action](i.value)
		if *debug {
			fmt.Printf(" --> %+v\n", *n)
		}
	}
	return n.p.Manhattan()
}

func (n *Navigator) nsew(d Pos) {
	if *part2 {
		n.w.Add(d)
	} else {
		n.p.Add(d)
	}
}

func (n *Navigator) north(v int) {
	n.nsew(Pos{0, -v})
}

func (n *Navigator) south(v int) {
	n.nsew(Pos{0, v})
}

func (n *Navigator) east(v int) {
	n.nsew(Pos{v, 0})
}

func (n *Navigator) west(v int) {
	n.nsew(Pos{-v, 0})
}

func (n *Navigator) left(deg int) {
	n.w.Rotate(-deg)
}

func (n *Navigator) right(deg int) {
	n.w.Rotate(deg)
}

func (n *Navigator) forward(v int) {
	for i := 0; i < v; i++ {
		n.p.Add(n.w)
	}
}

func getFilename(puzzleDay int) string {
	var suffix string
	if *useExample {
		suffix = "-example"
	}
	return fmt.Sprintf("input/%d%s.txt", puzzleDay, suffix)
}

func main() {
	flag.Parse()
	f, err := os.Open(getFilename(12))
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}
	var inst []Instruction
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		l := scanner.Text()
		if l == "" {
			continue
		}
		sl := strings.SplitN(l, "", 2)
		v, _ := strconv.Atoi(sl[1])
		inst = append(inst, Instruction{sl[0], v})
	}

	w := Pos{1, 0}
	if *part2 {
		w = Pos{10, -1}
	}

	n := Navigator{w: w}
	dist := n.Run(inst)
	fmt.Printf("MANHATTAN DISTANCE: %d\n", dist)
}
