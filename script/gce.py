"""
Prompt Combiner Script (gce.py)

Purpose:
    Combines all prompt template files from the 'prompts/' directory into a single
    'final_prompt.txt' file for easy distribution and usage.

Usage:
    python script/gce.py

Output:
    Creates/updates 'final_prompt.txt' in the repository root with combined content
    from all files in the prompts/ directory.

Author: Chirag Singhal (@chirag127)
"""

import os
import re
import json
import glob
import shutil

def get_files_in_directory(directory):
    """
    Get all files in the given directory.
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_file_contents(file_path):
    """
    Get the contents of the given file.
    """
    with open(file_path, 'r') as f:
        return f.read()

def main():
    """
    Main function to generate the final prompt.
    """
    directory = 'prompts'
    files = get_files_in_directory(directory)
    file_contents = [get_file_contents(os.path.join(directory, f)) for f in files]
    final_prompt = '\n'.join(file_contents)

    # Save the final prompt to a file
    with open('final_prompt.txt', 'w') as f:
        f.write(final_prompt)

if __name__ == '__main__':
    main()
