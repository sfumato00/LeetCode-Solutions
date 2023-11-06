function inner_function() {
    echo "I am the inner function."
    path=$1
    ext=$2
    echo "Debugging: $path, $ext"
    local count=$(find ${path} -type f -name "[0-9]*.${ext}" 2> /dev/null | wc -l)
    echo "$count"
}

function outer_function() {
    echo "I am the outer function, calling inner_function now."
    inner_function somePath someExt
    
    language=$1
    ext=$2
    output_file=$3
    
    easy_count=$(inner_function "${language}/easy" "py")
}

# Calling the outer function, which in turn calls the inner function
outer_function python py