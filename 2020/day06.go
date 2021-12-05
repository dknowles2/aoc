package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

func parseEntryA(e string) int {
	seen := map[string]int{}
	people := strings.Split(e, "\n")
	for _, p := range people {
		for _, c := range strings.Split(p, "") {
			if strings.TrimSpace(c) == "" {
				continue
			}
			seen[c]++
		}
	}
	fmt.Println(seen)
	return len(seen)
}

func parseEntryB(e string) int {
	e = strings.TrimSpace(e)
	seen := map[string]int{}
	people := strings.Split(e, "\n")
	for _, p := range people {
		for _, c := range strings.Split(p, "") {
			if strings.TrimSpace(c) == "" {
				continue
			}
			seen[c]++
		}
	}
	var n int
	for _, v := range seen {
		if v == len(people) {
			n++
		}
	}
	return n
}

func main() {
	contents, err := ioutil.ReadFile("input/06.txt")
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}
	var sum int
	for _, r := range bytes.Split(contents, []byte("\n\n")) {
		sum += parseEntryB(string(r))
	}
	fmt.Println(sum)
}
