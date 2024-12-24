# Name Matching Program

This program reads names from a file and randomly pairs them. It is particularly useful for activities like gift exchanges.

## Features

- Names are read from the `names.txt` file.
- Each name should be written on a new line in the file.
- The names are randomly matched, and the results are displayed in the console.
- Provides informative messages in case of errors.

## Requirements

- Python 3.6 or higher

## Usage

1. **Create the File:**

   - Create a file named `names.txt` in the same directory as the program.
   - Add names to the file, with one name per line.
     
     Example file content:
     ```
     Emir
     John
     Sarah
     Michael
     Emily
     David
     Anna
     ```

2. **Run the Program:**

   - In your terminal or command line, run the following command:
     ```
     python matcher.py
     ```

3. **View Results:**

   - The program will randomly pair the names and display the matches in the console.

     Example Output:
     ```
      Matches:
      Anna -> Emily
      Emily -> John
      John -> Sarah
      Sarah -> Emir
      Emir -> Michael
      Michael -> David
      David -> Anna
     ```

## Possible Error Messages

- **'names.txt' file not found:** Ensure that the file exists in the same directory as the program.
- **Please add at least 4 names to 'names.txt':** The file must contain at least 4 names.

## Contribution and Development

- Feel free to submit a pull request if you'd like to improve the program.
- If you encounter any issues, you can open an issue to report them.
