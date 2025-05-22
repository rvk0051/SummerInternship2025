# Scope in Python

#Scope refers to the region of a program where a name (identifier) is recognized.
# If a name is not in the current scope, Python will search for it in outer scopes using the LEGB rule.

# 1. Local (L): Names assigned within a function.
# 2. Enclosing (E): Names in the local scope of enclosing functions (for nested functions).
# 3. Global (G): Names assigned at the top-level of a module or declared global within a function.
# 4. Built-in (B): Names preassigned in the built-in names module.

# This hierarchy ensures that Python searches for names in the correct order,
# preventing unintended overwrites and aiding in code clarity.