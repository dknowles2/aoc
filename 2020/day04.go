package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"regexp"
	"strconv"
	"strings"
)

func parseEntry(e string) map[string]string {
	ret := map[string]string{}
	for _, kv := range strings.Fields(e) {
		kvs := strings.SplitN(kv, ":", 2)
		ret[kvs[0]] = kvs[1]
	}
	return ret
}

type validator func(v string) bool

func validate(m map[string]string, req map[string]validator) bool {
	for k, validate := range req {
		if !validate(m[k]) {
			return false
		}
	}
	return true
}

func nonEmpty(v string) bool {
	return v != ""
}

func alwaysTrue(v string) bool {
	return true
}

func intBetween(x, y int) validator {
	return func(v string) bool {
		i, err := strconv.Atoi(v)
		if err != nil {
			return false
		}
		return i >= x && i <= y

	}
}

func matchesRegexp(r string) validator {
	re := regexp.MustCompile(r)
	return func(v string) bool {
		return re.MatchString(v)
	}
}

func main() {
	contents, err := ioutil.ReadFile("input/04.txt")
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}

	req := map[string]validator{
		"byr": nonEmpty,
		"iyr": nonEmpty,
		"eyr": nonEmpty,
		"hgt": nonEmpty,
		"hcl": nonEmpty,
		"ecl": nonEmpty,
		"pid": nonEmpty,
		"cid": alwaysTrue,
	}
	req2 := map[string]validator{
		"byr": intBetween(1920, 2002),
		"iyr": intBetween(2010, 2020),
		"eyr": intBetween(2020, 2030),
		"hgt": func(v string) bool {
			re := regexp.MustCompile("^([0-9]+)(cm|in)$")
			match := re.FindStringSubmatch(v)
			if len(match) != 3 {
				return false
			}
			prefix := match[1]
			suffix := match[2]
			if suffix == "cm" {
				return intBetween(150, 193)(prefix)
			}
			if suffix == "in" {
				return intBetween(50, 76)(prefix)
			}
			return false
		},
		"hcl": matchesRegexp("^#[0-9a-f]{6}$"),
		"ecl": matchesRegexp("^(amb|blu|brn|gry|grn|hzl|oth)$"),
		"pid": matchesRegexp("^[0-9]{9}$"),
		"cid": alwaysTrue,
	}

	numValid := []int{0, 0}

	for _, r := range bytes.Split(contents, []byte("\n\n")) {
		e := parseEntry(string(r))
		valid1 := validate(e, req)
		if valid1 {
			numValid[0]++
		}
		valid2 := validate(e, req2)
		if valid2 {
			numValid[1]++
		}
	}

	fmt.Printf("Number valid: %d\n", numValid)
}
