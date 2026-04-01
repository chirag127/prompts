# generate the python code for the combining of all files in the directory prompts
# and the generation of the final prompt

import os


def get_files_in_directory(directory):
    """
    Get all files in the given directory.
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def get_file_contents(file_path):
    """
    Get the contents of the given file.
    """
    with open(file_path, "r") as f:
        return f.read()


def main():
    """
    Main function to generate the final prompt.
    """
    directory = "prompts"
    files = get_files_in_directory(directory)
    file_contents = [get_file_contents(os.path.join(directory, f)) for f in files]
    final_prompt = "\n".join(file_contents)

    # Save the final prompt to a file
    with open("final_prompt.txt", "w") as f:
        f.write(final_prompt)


if __name__ == "__main__":
    main()
