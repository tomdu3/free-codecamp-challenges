import os
import re
from collections import defaultdict
from datetime import datetime

# Read the problems list
with open('problems_list.txt', 'r') as f:
    lines = f.readlines()

problems = []

# Regex to parse the line: ./2025/2025-08/25-08-11/problem.md:# Vowel Balance or ./2025-08/25-08-11/problem.md:# Vowel Balance
# Matches optional year group (group 1), month (group 2), date (group 3), title (group 4)
pattern = re.compile(r'\./(?:(\d{4})/)?(\d{4}-\d{2})/(\d{2}-\d{2}-\d{2})/problem\.md:# (.+)')

for line in lines:
    line = line.strip()
    match = pattern.match(line)
    if match:
        year_dir = match.group(1)
        month_str = match.group(2)
        date_str = match.group(3) 
        title = match.group(4)
        
        # Construct path based on whether year_dir exists
        if year_dir:
            file_path = f'./{year_dir}/{month_str}/{date_str}/problem.md'
        else:
            file_path = f'./{month_str}/{date_str}/problem.md'
            
        problems.append({
            'month': month_str,
            'date': date_str,
            'title': title,
            'path': file_path
        })

# Group by month
grouped = defaultdict(list)
for p in problems:
    grouped[p['month']].append(p)

# Sort months
months_sorted = sorted(grouped.keys())

# Generate Markdown
output = "# Daily Challenge FCC\n\nThis repository contains my solutions to daily FreeCodeCamp challenges.\n\n"
output += "# Solved Problems\n\n"

for month in months_sorted:
    # Convert "2025-08" to "August 2025"
    try:
        dt = datetime.strptime(month, "%Y-%m")
        month_name = dt.strftime("%B %Y")
    except ValueError:
        month_name = month
    
    output += f"## {month_name}\n\n"
    
    # Sort problems by date within month
    # date_str is YY-MM-DD, e.g., 25-08-11
    month_problems = sorted(grouped[month], key=lambda x: x['date'])
    
    for p in month_problems:
        output += f"- [{p['date']}: {p['title']}]({p['path']})\n"
    
    output += "\n"

# Only print output, don't write directly yet
print(output)
