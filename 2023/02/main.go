package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	lines    []string
	inputMap map[int][]map[string]int //map[game#]map[color]number
)

func main() {
	readFile()
	buildInputMap()

	fmt.Println("-----part 1------")
	part1()
	fmt.Println("-----part 2------")
	part2()
}

func part1() {
	result := 0
	for gameNumber, gameDraws := range inputMap {
		if validGame(gameDraws) {
			result += gameNumber
		}
	}
	fmt.Println(result)
}

func part2() {
	result := 0
	for _, gameDraws := range inputMap {
		result += drawPower(gameDraws)
	}

	fmt.Println(result)
}

func drawPower(gameDraws []map[string]int) int {
	resultMap := map[string]int{
		"red":   1,
		"blue":  1,
		"green": 1,
	}

	for _, draw := range gameDraws {
		if val, found := draw["red"]; found && val > resultMap["red"] {
			resultMap["red"] = val
		}

		if val, found := draw["green"]; found && val > resultMap["green"] {
			resultMap["green"] = val
		}

		if val, found := draw["blue"]; found && val > resultMap["blue"] {
			resultMap["blue"] = val
		}
	}

	return resultMap["red"] * resultMap["green"] * resultMap["blue"]
}

func buildInputMap() {
	inputMap = make(map[int][]map[string]int)
	for _, line := range lines {
		gameLine := strings.Split(line, ":")
		gameNumber, _ := strconv.Atoi(strings.Split(gameLine[0], " ")[1])
		gameDraws := strings.Split(gameLine[1], ";")
		for _, draw := range gameDraws {
			drawColors := strings.Split(draw, ",")
			colorMap := make(map[string]int)
			for _, drawColor := range drawColors {
				quantity, _ := strconv.Atoi(strings.Split(strings.TrimSpace(drawColor), " ")[0])
				color := strings.Split(strings.TrimSpace(drawColor), " ")[1]
				colorMap[color] = quantity
			}

			inputMap[gameNumber] = append(inputMap[gameNumber], colorMap)
		}
	}
}

func validGame(gameDraws []map[string]int) bool {
	for _, draw := range gameDraws {
		if val, found := draw["red"]; found && val > 12 {
			return false
		}

		if val, found := draw["green"]; found && val > 13 {
			return false
		}

		if val, found := draw["blue"]; found && val > 14 {
			return false
		}
	}
	return true
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
