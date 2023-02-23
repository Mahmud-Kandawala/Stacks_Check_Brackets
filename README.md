# Stacks: Check Brackets

## Asignment

Stacks are used to check that parentheses match in an equation.
Write a program that asks the user to input a string containing parentheses of the three types:   "( )"  "[  ]" and "{  }" and then tell him/her whether they are right or wrong.

For example:

```
Abc(xyz)mnv             Correct
Abc(xyz]bnm             Wrong mismatched brackets
Abc( xcvbnm,m           Wrong bracket opened but never closed
Abc(cvb{bgt}vde)dfg     Correct
Abc(fgfd{gg)dfg}nn      Wrong mismatched brackets
Abc)nmg                 Wrong bracket closed but never opened 

```

Hint: The trick here is to  push an “open” bracket to the stack and pop when you find a “closed” bracket 

## Development

The code was developed using Python.

## Testing 

The test for this project is in `stack.py`. The test will run automatically when you hit the "Run" button.
