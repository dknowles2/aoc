package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var re = regexp.MustCompile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")

type Entry struct {
	a, b int
	ltr  string
	pwd  string
}

func (e *Entry) check1() bool {
	cnt := strings.Count(e.pwd, e.ltr)
	return cnt >= e.a && cnt <= e.b
}

func (e *Entry) check2() bool {
	pwds := strings.Split(e.pwd, "")
	return (pwds[e.a-1] == e.ltr) != (pwds[e.b-1] == e.ltr)
}

func main() {
	f, err := os.Open("input/02.txt")
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}
	scanner := bufio.NewScanner(f)

	numValid := []int{0, 0}
	for scanner.Scan() {
		l := scanner.Text()
		match := re.FindStringSubmatch(l)
		if len(match) < 5 {
			// bad input
			continue
		}
		a, _ := strconv.Atoi(match[1])
		b, _ := strconv.Atoi(match[2])
		ltr := match[3]
		pwd := match[4]
		e := Entry{a, b, ltr, pwd}
		if e.check1() {
			numValid[0]++
		}
		if e.check2() {
			numValid[1]++
		}
	}

	fmt.Println(numValid)
}
