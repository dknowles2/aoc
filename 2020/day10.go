package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"sort"
	"strconv"
	"strings"
)

func parse(in string) []int {
	var ret []int
	lines := strings.Split(in, "\n")
	for _, l := range lines {
		if strings.TrimSpace(l) == "" {
			continue
		}
		n, _ := strconv.Atoi(l)
		ret = append(ret, n)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(ret)))
	return ret
}

func diffs(in, req int, adapters []int) map[int]int {
	ret := map[int]int{}
	for _, a := range adapters {
		ret[a-in]++
		in = a
	}
	ret[req+3-in]++
	return ret
}

func search_dfs(in, req int, adapters []int) int {
	var ret int
	var dfs func(int, []int, map[int]bool) int
	dfs = func(a int, path []int, seen map[int]bool) int {
		var paths int
		seen[a] = true
		path = append(path, a)

		diff := req - a
		if diff > 0 && diff < 4 {
			paths++
		}

		for _, b := range adapters {
			if seen[b] {
				continue
			}
			aDiff := b - a
			if aDiff > 0 && aDiff < 4 {
				paths += dfs(b, copySlice(path), copyMap(seen))
			}
		}
		return paths
	}

	for _, a := range adapters {
		if a-in > 0 && a-in < 4 {
			ret += dfs(a, []int{0}, map[int]bool{})
		}
	}

	return ret
}

func copySlice(s []int) []int {
	ret := make([]int, len(s))
	copy(ret, s)
	return ret
}

func copyMap(m map[int]bool) map[int]bool {
	ret := map[int]bool{}
	for k, v := range m {
		ret[k] = v
	}
	return ret
}

func search(in, req int, adaptersSlice []int) int {
	adapters := map[int]bool{0: true}
	for _, a := range adaptersSlice {
		adapters[a] = true
	}
	combinations := map[int]int{req: 1}

	for i := req; i >= 0; i-- {
		if adapters[i] {
			combinations[i] += combinations[i+1]
			combinations[i] += combinations[i+2]
			combinations[i] += combinations[i+3]
		}
	}
	return combinations[0]
}

func main() {
	contents, err := ioutil.ReadFile("input/10.txt")
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}

	adapters := parse(string(contents))
	fmt.Println(adapters)
	req := adapters[0]
	d := diffs(0, req, adapters)
	fmt.Println(d)
	fmt.Println(d[1] * d[3])
	fmt.Println()
	fmt.Printf("Found %d paths.\n", search(0, req, adapters))
}
