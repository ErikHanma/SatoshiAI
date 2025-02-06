print_directory() {
    local dir="$1"
    local indent="$2"

    echo "${indent}$(basename "$dir")/"
    
    for file in "$dir"/*; do
        if [ -d "$file" ]; then
            print_directory "$file" "  ${indent}"
        elif [ -f "$file" ]; then
            echo "${indent}  $(basename "$file")"
            echo "${indent}  --------------------"
            cat "$file"
            echo ""
            echo "${indent}  --------------------"
        fi
    done
}

print_directory "." ""
