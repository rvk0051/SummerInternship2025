#Fizz Buzz Problem involves that given an integer n, for every integer 0 < i <= n, the task is to output,

#"FizzBuzz" if i is divisible by 3 and 5,
#"Fizz" if i is divisible by 3,
#"Buzz" if i is divisible by 5
#"i" as a string, if none of the conditions are true.
#Return an array of strings.

#Example:-
# Input: n = 3
#Output: ["1", "2", "Fizz"]
#Explanation: 1 and 2 are neither divisible by 3 nor 5, so we just output 1 and 2,
# and 3 is divisible by 3 so we output "Fizz"


#Approach 1
def fizzBuzz(self, n: int):
    res = [] # Initializing list res
    for i in range(1, n + 1):
# Checking divisibility of i, and depending upon divisibility appending the result list.
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res

#Time Complexity: O(n)
#Space Complexity: O(n)

#Better Approach
def fizzBuzz(self, n: int):
    # code here
    res = [] # Initializing result list
    mp = {3: 'Fizz', 5: 'Buzz'}  # Creating a map, mapping divisors with corresponding strings
    divisors = [3, 5]  # Creating list of divisors

    for i in range(1, n + 1):
        s = '' # initiating an empty string
        for d in divisors:
            if i % d == 0:
                s += mp[d] # adding the string corresponding to the divisor which satisfies condition
        # if string is empty, the number 'i' is itself converted into a string and added into the empty string
        if not s: s += str(i)

        #Then, the final string is appended into 'res' list
        res.append(s)
    return res
#Time Complexity: O(n)
#Space Complexity: O(n)
