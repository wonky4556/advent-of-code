package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	input []string
)

func main() {
	loadFile()
	fmt.Println("-----PART 1-----")
	partOne()
	fmt.Println("-----PART 2-----")
	partTwo()
}

func partTwo() {
	spot := 50
	countZero := 0

	for _, rotation := range input {
		direction := strings.ToUpper(string(rotation[0]))
		distance, _ := strconv.Atoi(rotation[1:])

		zeroCrossings := calculateZeroCrossings(direction, spot, distance)

		spot = calculateSpot(spot, direction, distance)

		countZero += zeroCrossings
	}

	fmt.Println(countZero)
}

func calculateZeroCrossings(direction string, spot, distance int) int {
	// firstHit := 0
	switch direction {
	case "R":
		return countHitsRight(spot, distance)
	case "L":
		return countHitsLeft(spot, distance)
	}

	return 0
}

func countHitsRight(p, num int) int {
	pMod := p % 100
	k0 := (100 - pMod) % 100 // first step where we hit 0

	if k0 == 0 {
		// first hit is one full cycle away
		return num / 100
	}
	if k0 > num {
		// never reaches 0 during this rotation
		return 0
	}
	// one hit at k0 plus periodic every 100 steps
	return 1 + (num-k0)/100
}

func countHitsLeft(p, num int) int {
	pMod := p % 100
	k0 := pMod % 100 // first step backwards to reach 0

	if k0 == 0 {
		return num / 100
	}
	if k0 > num {
		return 0
	}
	return 1 + (num-k0)/100
}

func partOne() {
	spot := 50
	countZero := 0
	for _, rotation := range input {
		direction := strings.ToUpper(string(rotation[0]))
		distance, _ := strconv.Atoi(rotation[1:])

		spot = calculateSpot(spot, direction, distance)

		if spot == 0 {
			countZero++
		}
	}

	fmt.Println(countZero)
}

func calculateSpot(start int, direction string, distance int) int {
	result := 0
	switch direction {
	case "R":
		result = (start + distance) % 100
	case "L":
		result = (start - distance) % 100
	}

	// normalize result
	if result < 0 {
		result = 100 + result
	}

	return result
}

func loadFile() {
	file, err := os.Open("_input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}
}
