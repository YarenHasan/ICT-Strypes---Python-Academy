# 📂 Simple File Reader (Python)
This is a minimal Python script that demonstrates how to read data from a file safely, with built-in error handling to ensure the file exists before reading.

🧠 What It Does:

  * Reads the first line from a specified text file
  * Checks if the file exists before opening
  * Raises an exception ("Bad File!") if the file is not found


📝 Behavior:

  * If the file exists: returns the first line of the file
  * If the file does not exist: raises an exception


📂 Notes:

  * This script uses the built-in os module for file existence checking.
  * Only reads the first line; can be extended to read more or all lines.


📦 Example Usage:

    try:
        line = readFromFile("example.txt")
        print(f"First line: {line}")
    except Exception as e:
        print(e)
    
    Output:

      First line: Hello, world!
    
    Or if the file doesn't exist:

      Bad File!
