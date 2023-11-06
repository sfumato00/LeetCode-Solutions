function count_files {
    path=$1
    ext=$2
    # echo "Debugging: $path, $ext"
    local count = $(find ${path} -type f -name "[0-9]*.${ext}" 2> /dev/null | wc -l)
    echo "$count"
}

function count_solutions_by_language {
    language=$1
    ext=$2
    output_file=$3
    
    easy_count=$(find ${language}/easy -type f -name "[0-9]*.${ext}" 2> /dev/null | wc -l)
    # medium_count=$(find ${language}/medium -type f -name "[0-9]*.${ext}" 2> /dev/null | wc -l)
    medium_count=count_files ${language}/medium $ext
    hard_count=$(find ${language}/hard -type f -name "[0-9]*.${ext}" 2> /dev/null | wc -l)
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

echo "# My Solutions for LeetCode Problems" > README.md
count_solutions_by_language Python py README.md
count_solutions_by_language JAVA java README.md