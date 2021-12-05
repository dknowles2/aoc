package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
)

var (
	colorRe = regexp.MustCompile("^(.+) bags contain (.+).$")
	ruleRe  = regexp.MustCompile("^([0-9]+) (.+) bag[s]?$")
)

type Bag struct {
	Color string
	Rules map[string]int
}

func parse(line string) Bag {
	bag := Bag{
		Rules: make(map[string]int),
	}
	colorMatch := colorRe.FindStringSubmatch(line)
	bag.Color = colorMatch[1]
	if colorMatch[2] == "no other bags" {
		return bag
	}
	for _, c := range strings.Split(colorMatch[2], ", ") {
		bagMatch := ruleRe.FindStringSubmatch(c)
		num, _ := strconv.Atoi(bagMatch[1])
		bag.Rules[bagMatch[2]] = num
	}
	return bag
}

func find(bags map[string]Bag, color string) []string {
	match := map[string]bool{}
	var queue []string

	for _, b := range bags {
		if b.Rules[color] > 0 {
			match[b.Color] = true
			queue = append(queue, b.Color)
		}
	}

	for len(queue) > 0 {
		c := queue[0]
		queue = queue[1:]
		for _, b := range bags {
			if match[b.Color] {
				continue
			}
			if b.Rules[c] > 0 {
				match[b.Color] = true
				queue = append(queue, b.Color)
			}
		}
	}

	var ret []string
	for c := range match {
		ret = append(ret, c)
	}
	return ret
}

func sum(bags map[string]Bag, b Bag) int {
	visited := map[string]int{}
	var dfs func(Bag) int
	pfx := ""
	dfs = func(b Bag) int {
		pfx += "  "
		defer func() { pfx = pfx[:len(pfx)-2] }()
		var sum int
		for c, n := range b.Rules {
			if v, ok := visited[c]; ok {
				sum += n + (n * v)
				continue
			}
			x := dfs(bags[c])
			visited[c] = x
			sum += n + (n * x)
		}
		return sum
	}
	return dfs(b)
}

func main() {
	contents, err := ioutil.ReadFile("input/07.txt")
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}

	bags := map[string]Bag{}

	for _, line := range strings.Split(string(contents), "\n") {
		line := strings.TrimSpace(line)
		if line == "" {
			continue
		}
		bag := parse(line)
		bags[bag.Color] = bag
	}

	match := find(bags, "shiny gold")
	fmt.Println(len(match))
	fmt.Println(sum(bags, bags["shiny gold"]))
}
