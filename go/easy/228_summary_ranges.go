func summaryRanges(nums []int) []string {

	n := len(nums)
	output := []string{}

	for i := 0; i < n; {
		j := i
		for j < n-1 && nums[j]+1 == nums[j+1] {
			j++
		}

		if i == j {
			output = append(output, strconv.Itoa(nums[i]))
		} else {
			output = append(output, strconv.Itoa(nums[i])+"->"+strconv.Itoa(nums[j]))
		}
		i = j + 1
	}

	// for end, x := range nums {
	//     if end == n - 1 || nums[end + 1] != x + 1 {
	//         if start == end {
	//             output = append(output, strconv.Itoa(nums[start]))
	//         } else {
	//             output = append(output, strconv.Itoa(nums[start]) + "->" + strconv.Itoa(x))
	//         }
	//         start = end + 1
	//     }
	// }
	return output
}