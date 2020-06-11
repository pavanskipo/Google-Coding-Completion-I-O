
# Google uses standard Input and Output for it's coding competitions
# I was very confused with this at the beginning and ended up wasting a lot of time
# So here's a simple boilerplate code with sample input and output



#               TAKING INPUTS
# -----------------------------------------------------
# Sample Input below - First line: No. of test cases followed by the test sets 
# 3
# 4 100
# 20 90 40 90
# 4 50
# 30 30 10 10
# 3 300
# 999 999 999

test_cases = int(input())
for i in range(1, t+1):
    integer_variable1, integer_variable2 = [int(x) for x in input().split()]
    list_of_integers = [int(x) for x in input().split()]
    # Logic goes here
    # Usually output (print) goes here, but it depends on your implementation

# -----------------------------------------------------



#               PRINTING OUTPUTS
# -----------------------------------------------------
# Sample Output
# Case #1: 2
# Case #2: 3
# Case #3: 0

print("Case #{}: {}".format(i, result)) # i - index of test set, result - solution for a given test set

# -----------------------------------------------------
