package medium

import "sort"

func numFactoredBinaryTrees(arr []int) int {
	const MOD = 1000000007

	sort.Ints(arr)
	mem := make(map[int]int)
	total := 0

	for i, z := range arr {
		val := 1
		for _, y := range arr[:i] {
			x, r := z/y, z%y

			if r > 0 {
				continue
			}

			xCnt, ok := mem[x]

			if ok {
				val += (xCnt * mem[y]) % MOD
			}
		}
		mem[z] = val
		total = (total + val) % MOD
	}
	return total
}
