package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

type StateMachine struct {
	acc, pos int
	inss     []Instruction
	seen     map[int]bool
}

func New(inss []Instruction) *StateMachine {
	return &StateMachine{
		inss: inss[:],
		seen: map[int]bool{},
	}
}

func (s *StateMachine) Run() bool {
	for s.pos < len(s.inss) {
		ins := s.inss[s.pos]
		if s.seen[s.pos] {
			return false
		}
		s.seen[s.pos] = true
		ops[ins.op](s, ins.arg)
	}
	return true
}

type Operation func(*StateMachine, int)

var ops = map[string]Operation{
	"acc": func(s *StateMachine, arg int) {
		s.acc += arg
		s.pos += 1
	},
	"jmp": func(s *StateMachine, arg int) {
		s.pos += arg
	},
	"nop": func(s *StateMachine, arg int) {
		s.pos += 1
	},
}

type Instruction struct {
	op  string
	arg int
}

func parse(contents string) []Instruction {
	var ret []Instruction
	for _, line := range strings.Split(contents, "\n") {
		if strings.TrimSpace(line) == "" {
			continue
		}
		spl := strings.Split(line, " ")
		arg, err := strconv.Atoi(spl[1])
		if err != nil {
			panic(fmt.Sprintf("Not a number: %s", spl[1]))
		}
		ret = append(ret, Instruction{spl[0], arg})
	}
	return ret
}

func main() {
	contents, err := ioutil.ReadFile("input/08.txt")
	if err != nil {
		log.Fatalf("failed to read file: %f", err)
	}
	inss0 := parse(string(contents))

	var pos int
	var res bool
	for !res && pos < len(inss0) {
		inss := make([]Instruction, len(inss0))
		copy(inss, inss0)
		for i := pos; i < len(inss); i++ {
			if inss[i].op == "jmp" {
				newOp := "nop"
				pos = i + 1
				inss[i].op = newOp
				break
			} else if inss[i].op == "nop" {
				newOp := "jmp"
				pos = i + 1
				inss[i].op = newOp
				break
			}
			pos = i + 1
		}
		sm := New(inss)
		res := sm.Run()
		if res {
			fmt.Println(sm.acc)
			return
		}
	}
}
