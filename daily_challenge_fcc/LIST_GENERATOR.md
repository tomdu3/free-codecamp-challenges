# List Generator Documentation

This document describes the process used to generate the list of solved problems in `README.md`.

## 1. Data Extraction

We extracted the list of problems and their titles using a shell command that combines `find` and `grep`.

### Command
```bash
find . -name "problem.md" -exec grep -H "^# " {} \; | sort > problems_list.txt
```

### Explanation
- `find . -name "problem.md"`: Recursively searches the current directory for all files named `problem.md`.
- `-exec grep -H "^# " {} \;`: For each file found:
  - `grep` searches for lines starting with `# ` (Markdown H1 headers).
  - `-H` ensures the filename is printed along with the matching line.
  - `{}` is replaced by the filename.
- `| sort`: Sorts the output alphabetically/chronologically ensuring a consistent order.
- `> problems_list.txt`: Redirects the output to a file for processing.

### Output Format
The resulting `problems_list.txt` contains lines in the format:
```
./YYYY-MM/YY-MM-DD/problem.md:# Title
```
Example:
```
./2025-08/25-08-11/problem.md:# Vowel Balance
```

## 2. Markdown Generation

A Python script `generate_readme.py` was used to parse `problems_list.txt` and generate the formatted Markdown for `README.md`.

### Core Functionality
1. **Parsing**: 
   - Reads `problems_list.txt`.
   - Uses Regular Expressions to extract:
     - Month (`YYYY-MM`)
     - Date (`YY-MM-DD`)
     - Title (Problem Name)
     - File Path

2. **Grouping & Sorting**:
   - Groups problems by Month.
   - Sorts months chronologically.
   - Sorts problems within each month by date.

3. **Formatting**:
   - Converts month strings (e.g., "2025-08") to readable names (e.g., "August 2025").
   - Generates a Markdown list for each month:
     - `- [YY-MM-DD: Title](./path/to/problem.md)`

### Usage
```bash
python3 generate_readme.py
```
this prints the generated markdown to stdout, which can then be redirected to `README.md`.
