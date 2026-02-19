
"""
Notes:
- An infinite loop occurs when a loop's condition never becomes False.
- Typical cause: forgetting to update the variable that the condition depends on.
- To stop a stuck program in a terminal, press CTRL+C (KeyboardInterrupt).
- In some editors (e.g., VS Code), the output is embedded; be sure the output
  pane has focus when pressing CTRL+C.

Example (do NOT run the infinite version):
"""

 Correct counting loop (prints 1..5):
x = 1
while x <= 5:
    print(x)
    x += 1

 Infinite loop example (COMMENTED OUT on purpose):
 x = 1
 while x <= 5:
    print(x)   # Forgot: x += 1
     # This loop never ends because x never changes.
