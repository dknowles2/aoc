package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

var (
	filename string
	preamble int

	exampleSet = false
)

func init() {
	if exampleSet {
		filename = "input/09-example.txt"
		preamble = 5
	} else {
		filename = "input/09.txt"
		preamble = 25
	}
}

func isValid(i, num int, nums []int) bool {
	if i < preamble {
		return true
	}
	for j := i - preamble; j < i; j++ {
		for k := j + 1; k < i; k++ {
			if nums[j]+nums[k] == num {
				return true
			}
		}
	}
	return false
}

func main() {
	f, err := os.Open(filename)
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}
	scanner := bufio.NewScanner(f)
	var i, invalid int
	var nums []int

	for scanner.Scan() {
		num, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatalf("Not a number: %v", err)
		}
		nums = append(nums, num)
		if invalid == 0 && !isValid(i, num, nums) {
			fmt.Printf("INVALID NUMBER: %d\n", num)
			invalid = num
			break
		}
		i++
	}

	var sum, min, max int
	for i, n := range nums {
		sum = n
		min = n
		max = n
		for _, n := range nums[i+1 : len(nums)] {
			sum += n
			if n > max {
				max = n
			}
			if n < min {
				min = n
			}
			if sum == invalid {
				fmt.Printf("WEAKNESS FOUND: %d\n", min+max)
				return
			}
			if sum > invalid {
				break
			}

		}
	}
}
