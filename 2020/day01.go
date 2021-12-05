package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func partA(nums []int) int {
	var i, j int
	for i < len(nums) {
		for j < len(nums) {
			if nums[i]+nums[j] == 2020 {
				return nums[i] * nums[j]
			}
			j++
		}
		j = i
		i++
	}
	return 0
}

func partB(nums []int) int {
	var i, j, k int
	for i < len(nums) {
		for j < len(nums) {
			for k < len(nums) {
				if nums[i]+nums[j]+nums[k] == 2020 {
					return nums[i] * nums[j] * nums[k]
				}
				k++
			}
			j++
			k = 0
		}
		j = 0
		k = i
		i++
	}
	return 0
}

func main() {
	f, err := os.Open("input/01.txt")
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}
	scanner := bufio.NewScanner(f)
	var nums []int
	for scanner.Scan() {
		num, err := strconv.Atoi(scanner.Text())
		if err != nil {
			log.Fatalf("Not a number: %s", err)
		}
		nums = append(nums, num)
	}

	fmt.Println(partA(nums))
	fmt.Println(partB(nums))
}
