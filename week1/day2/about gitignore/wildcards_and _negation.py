#Wildcards
#Wildcards let you match many files or folders at once:
# 1. * matches any number of characters
# 2. ? matches a single character
# 3. [abc] matches any character in the set
# 4. [!abc] matches any character not in the set
#Example:   *.tmp      # all .tmp files

#Negation
#Use ! to not ignore something that would otherwise be ignored. This is called an exception:
#Example:
# *.log
#!important.log  # important.log is not to be ignored but all other files in.log has to be ignored.