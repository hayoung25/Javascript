## Define pattern_search
def pattern_search(text, pattern):  
    print("Input Text:", text, "Input Pattern:", pattern)
    
    # Loop through each index of text
    for index in range(len(text)):
        print("Text Index:", index)
        match_count = 0

        # Compare each index of text and the pattern we are looking for
        for char in range(len(pattern)):
            print("Pattern Index:", char)
            if pattern[char] == text[index + char]:
                match_count += 1
            
            # If the first character does not match, move to next index
            else:
                break
        if match_count == len(pattern):
            print(pattern, "found at index", index)

## Testing
text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
pattern_search(text, pattern)


