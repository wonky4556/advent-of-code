package main

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
	"strconv"
)

var (
	lines []string
	ONE   = []string{"o", "n", "e"}
	TWO   = []string{"t", "w", "o"}
	THREE = []string{"t", "h", "r", "e", "e"}
	FOUR  = []string{"f", "o", "u", "r"}
	FIVE  = []string{"f", "i", "v", "e"}
	SIX   = []string{"s", "i", "x"}
	SEVEN = []string{"s", "e", "v", "e", "n"}
	EIGHT = []string{"e", "i", "g", "h", "t"}
	NINE  = []string{"n", "i", "n", "e"}
)

func main() {
	readFile()
	fmt.Println("------------Part 1 Result--------------")
	solvePart1()
	fmt.Println("------------Part 2 Result--------------")
	solvePart2()
}

func solvePart2() {
	var calibrationVals []int
	for _, line := range lines {
		chars := splitIntoCharacters(line)
		ints := []int{}
		for idx, c := range chars {
			i, err := strconv.Atoi(c)
			if err != nil {
				if r, v := traslateWordToInt(chars[idx:]); v {
					ints = append(ints, r)
				}
				continue
			}
			ints = append(ints, i)
		}
		calVal := concatDigits(ints[0], ints[len(ints)-1])
		calibrationVals = append(calibrationVals, calVal)

	}
	result := 0
	for _, v := range calibrationVals {
		result += v
	}

	fmt.Println(result)

}

func traslateWordToInt(remnant []string) (int, bool) {
	if checkNumber(ONE, remnant) {
		return 1, true
	} else if checkNumber(TWO, remnant) {
		return 2, true
	} else if checkNumber(THREE, remnant) {
		return 3, true
	} else if checkNumber(FOUR, remnant) {
		return 4, true
	} else if checkNumber(FIVE, remnant) {
		return 5, true
	} else if checkNumber(SIX, remnant) {
		return 6, true
	} else if checkNumber(SEVEN, remnant) {
		return 7, true
	} else if checkNumber(EIGHT, remnant) {
		return 8, true
	} else if checkNumber(NINE, remnant) {
		return 9, true
	}

	return 0, false
}

func checkNumber(num []string, partial []string) bool {

	if len(num) > len(partial) {
		return false
	}

	return reflect.DeepEqual(num, partial[:len(num)])
}

func solvePart1() {
	var calibrationVals []int
	for _, line := range lines {
		chars := splitIntoCharacters(line)
		ints := []int{}
		for _, c := range chars {
			i, err := strconv.Atoi(c)
			if err != nil {
				continue
			}
			ints = append(ints, i)
		}

		calVal := concatDigits(ints[0], ints[len(ints)-1])
		calibrationVals = append(calibrationVals, calVal)
	}

	result := 0
	for _, v := range calibrationVals {
		result += v
	}

	fmt.Println(result)
}

func readFile() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}
}

// splitIntoCharacters converts the provided string into a slice of
// single-character strings, handling multi-byte runes correctly.
func splitIntoCharacters(s string) []string {
	runes := []rune(s)
	chars := make([]string, len(runes))
	for i, r := range runes {
		chars[i] = string(r)
	}
	return chars
}

func concatDigits(a, b int) int {
	return a*10 + b
}
