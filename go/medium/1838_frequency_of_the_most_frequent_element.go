package medium

import (
	"sort"
)

func maxFrequency(nums []int, k int) int {
	n := len(nums)

	if n < 2 {
		return n
	}
	sort.Ints(nums)
	l, max_freq := 0, 1

	for r := 1; r < n; r++ {
		ops := (nums[r] - nums[r-1]) * (r - l)

		for l < r && k < ops {
			ops -= nums[r] - nums[l]
			l += 1
		}
		k -= ops
		max_freq = max(max_freq, r-l+1)
	}

	return max_freq
}
