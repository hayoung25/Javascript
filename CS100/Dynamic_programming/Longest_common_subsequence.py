dna_1 = "ACCGTT"
dna_2 = "CCAGCA"

def longest_common_subsequence(string_1, string_2):
    print(f"Finding longest common subsequence of {string_1} and {string_2}")

    grid = [[0 for i in range(len(string_1) + 1)] for i in range(len(string_2) + 1)]
    print(grid)

    for row in range(1, len(string_2) + 1):
        print(f'Comparing: {string_2[row - 1]}')
        for col in range(1, len(string_1) + 1):
            print(f'Against: {string_1[col - 1]}')
            
            # Found same value -> 1 + subproblem's value
            if string_1[col - 1] == string_2[row - 1]:
                grid[row][col] = grid[row - 1][col - 1] + 1
            
            # IF it is not same value -> find max between two subproblems'(this time each sub is 1 away from row and col) value
            else:
                grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])
    print(grid)
    answer = grid[len(string_1)][len(string_2)]
    print(answer)

longest_common_subsequence(dna_1, dna_2)
