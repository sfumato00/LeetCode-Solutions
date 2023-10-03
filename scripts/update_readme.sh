count_solutions_by_language() {
    language=$1
    ext=$2
    output_file=$3

    easy_count=$(ls ${language}/easy/[0-9]*.${ext} 2> /dev/null | wc -l)
    medium_count=$(ls ${language}/medium/[0-9]*.${ext} 2> /dev/null | wc -l)
    hard_count=$(ls ${language}/hard/[0-9]*.${ext} 2> /dev/null | wc -l)
    total=$((easy_count + medium_count + hard_count))

    echo "Total: $total"

    echo "" >> $output_file
    echo "## $language" >> $output_file
    echo "" >> $output_file
    echo "Easy: $easy_count" >> $output_file
    echo "Medium: $medium_count" >> $output_file
    echo "Hard: $hard_count" >> $output_file
    echo "Total: $total" >> $output_file
}

echo "# My Solutions for LeetCode problems" > README.md
count_solutions_by_language Python py README.md
count_solutions_by_language JAVA java README.md