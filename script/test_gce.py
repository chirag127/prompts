"""
Test Suite for gce.py

Tests the prompt combiner script including file operations, content reading,
and final prompt generation.
"""

import os
import shutil
import sys
import tempfile
import unittest

# Import the functions from gce.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from gce import get_file_contents, get_files_in_directory, main


class TestGetFilesInDirectory(unittest.TestCase):
    """Test cases for get_files_in_directory function."""

    def setUp(self):
        """Create a temporary directory for testing."""
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Remove the temporary directory after testing."""
        shutil.rmtree(self.test_dir)

    def test_empty_directory(self):
        """Test getting files from an empty directory."""
        files = get_files_in_directory(self.test_dir)
        self.assertEqual(files, [])

    def test_directory_with_files(self):
        """Test getting files from a directory with multiple files."""
        # Create test files
        test_files = ["file1.txt", "file2.md", "file3.py"]
        for filename in test_files:
            open(os.path.join(self.test_dir, filename), "w").close()

        files = get_files_in_directory(self.test_dir)
        self.assertEqual(sorted(files), sorted(test_files))

    def test_directory_with_subdirectories(self):
        """Test that subdirectories are not included in the file list."""
        # Create files and subdirectories
        test_files = ["file1.txt", "file2.txt"]
        for filename in test_files:
            open(os.path.join(self.test_dir, filename), "w").close()

        os.mkdir(os.path.join(self.test_dir, "subdir1"))
        os.mkdir(os.path.join(self.test_dir, "subdir2"))

        files = get_files_in_directory(self.test_dir)
        self.assertEqual(sorted(files), sorted(test_files))
        self.assertEqual(len(files), 2)

    def test_mixed_files_and_directories(self):
        """Test directory with both files and subdirectories."""
        # Create mixed content
        test_files = ["readme.md", "config.json"]
        for filename in test_files:
            with open(os.path.join(self.test_dir, filename), "w") as f:
                f.write("test content")

        os.mkdir(os.path.join(self.test_dir, "subdir"))

        files = get_files_in_directory(self.test_dir)
        self.assertEqual(sorted(files), sorted(test_files))


class TestGetFileContents(unittest.TestCase):
    """Test cases for get_file_contents function."""

    def setUp(self):
        """Create a temporary directory for testing."""
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Remove the temporary directory after testing."""
        shutil.rmtree(self.test_dir)

    def test_read_simple_file(self):
        """Test reading a simple text file."""
        test_content = "Hello, World!"
        test_file = os.path.join(self.test_dir, "test.txt")

        with open(test_file, "w") as f:
            f.write(test_content)

        content = get_file_contents(test_file)
        self.assertEqual(content, test_content)

    def test_read_multiline_file(self):
        """Test reading a file with multiple lines."""
        test_content = "Line 1\nLine 2\nLine 3\n"
        test_file = os.path.join(self.test_dir, "multiline.txt")

        with open(test_file, "w") as f:
            f.write(test_content)

        content = get_file_contents(test_file)
        self.assertEqual(content, test_content)

    def test_read_empty_file(self):
        """Test reading an empty file."""
        test_file = os.path.join(self.test_dir, "empty.txt")
        open(test_file, "w").close()

        content = get_file_contents(test_file)
        self.assertEqual(content, "")

    def test_read_file_with_special_characters(self):
        """Test reading a file with special characters."""
        test_content = 'Special chars: !@#$%^&*()_+-={}[]|\\:";<>?,./~`'
        test_file = os.path.join(self.test_dir, "special.txt")

        with open(test_file, "w") as f:
            f.write(test_content)

        content = get_file_contents(test_file)
        self.assertEqual(content, test_content)

    def test_read_markdown_file(self):
        """Test reading a markdown file."""
        test_content = "# Header\n\n## Subheader\n\n- Item 1\n- Item 2\n"
        test_file = os.path.join(self.test_dir, "test.md")

        with open(test_file, "w") as f:
            f.write(test_content)

        content = get_file_contents(test_file)
        self.assertEqual(content, test_content)


class TestMainFunction(unittest.TestCase):
    """Test cases for the main function."""

    def setUp(self):
        """Create temporary directories and files for testing."""
        self.test_dir = tempfile.mkdtemp()
        self.prompts_dir = os.path.join(self.test_dir, "prompts")
        os.mkdir(self.prompts_dir)

        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        """Clean up temporary directories and restore original directory."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir)

    def test_main_creates_final_prompt(self):
        """Test that main function creates final_prompt.txt."""
        # Create test files
        with open(os.path.join(self.prompts_dir, "prompt1.txt"), "w") as f:
            f.write("Prompt 1 content")
        with open(os.path.join(self.prompts_dir, "prompt2.txt"), "w") as f:
            f.write("Prompt 2 content")

        main()

        self.assertTrue(os.path.exists("final_prompt.txt"))

    def test_main_combines_file_contents(self):
        """Test that main function combines all file contents."""
        # Create test files with specific content
        content1 = "First prompt content"
        content2 = "Second prompt content"
        content3 = "Third prompt content"

        with open(os.path.join(self.prompts_dir, "prompt1.txt"), "w") as f:
            f.write(content1)
        with open(os.path.join(self.prompts_dir, "prompt2.txt"), "w") as f:
            f.write(content2)
        with open(os.path.join(self.prompts_dir, "prompt3.txt"), "w") as f:
            f.write(content3)

        main()

        with open("final_prompt.txt", "r") as f:
            final_content = f.read()

        # All content should be present
        self.assertIn(content1, final_content)
        self.assertIn(content2, final_content)
        self.assertIn(content3, final_content)

    def test_main_with_empty_directory(self):
        """Test main function with empty prompts directory."""
        main()

        with open("final_prompt.txt", "r") as f:
            content = f.read()

        self.assertEqual(content, "")

    def test_main_with_single_file(self):
        """Test main function with a single file."""
        test_content = "Single prompt file content"
        with open(os.path.join(self.prompts_dir, "single.txt"), "w") as f:
            f.write(test_content)

        main()

        with open("final_prompt.txt", "r") as f:
            content = f.read()

        self.assertEqual(content, test_content)

    def test_main_joins_with_newline(self):
        """Test that main function joins files with newline."""
        with open(os.path.join(self.prompts_dir, "a.txt"), "w") as f:
            f.write("Content A")
        with open(os.path.join(self.prompts_dir, "b.txt"), "w") as f:
            f.write("Content B")

        main()

        with open("final_prompt.txt", "r") as f:
            content = f.read()

        # Content should be joined with newline
        self.assertIn("\n", content)
        parts = content.split("\n")
        self.assertEqual(len(parts), 2)

    def test_main_overwrites_existing_file(self):
        """Test that main function overwrites existing final_prompt.txt."""
        # Create existing file
        with open("final_prompt.txt", "w") as f:
            f.write("Old content that should be replaced")

        # Create new prompts
        with open(os.path.join(self.prompts_dir, "new.txt"), "w") as f:
            f.write("New content")

        main()

        with open("final_prompt.txt", "r") as f:
            content = f.read()

        self.assertEqual(content, "New content")
        self.assertNotIn("Old content", content)

    def test_main_handles_markdown_files(self):
        """Test main function with markdown files."""
        md_content = "# Title\n\n## Section\n\nSome text."
        with open(os.path.join(self.prompts_dir, "prompt.md"), "w") as f:
            f.write(md_content)

        main()

        with open("final_prompt.txt", "r") as f:
            content = f.read()

        self.assertEqual(content, md_content)

    def test_main_preserves_file_content_integrity(self):
        """Test that main function preserves exact file content."""
        content_with_special = "Line1\n\nLine2\n  Indented\n\nLine3"
        with open(os.path.join(self.prompts_dir, "special.txt"), "w") as f:
            f.write(content_with_special)

        main()

        with open("final_prompt.txt", "r") as f:
            content = f.read()

        self.assertEqual(content, content_with_special)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete workflow."""

    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp()
        self.prompts_dir = os.path.join(self.test_dir, "prompts")
        os.mkdir(self.prompts_dir)
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        """Clean up test environment."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir)

    def test_complete_workflow(self):
        """Test the complete workflow from multiple files to final prompt."""
        # Create multiple prompt files
        prompts = {
            "system.md": "# System Prompt\n\nYou are an AI assistant.",
            "guidelines.md": "# Guidelines\n\n1. Be helpful\n2. Be accurate",
            "examples.md": "# Examples\n\nExample 1: ...\nExample 2: ...",
        }

        for filename, content in prompts.items():
            with open(os.path.join(self.prompts_dir, filename), "w") as f:
                f.write(content)

        # Run main function
        main()

        # Verify output
        self.assertTrue(os.path.exists("final_prompt.txt"))

        with open("final_prompt.txt", "r") as f:
            final_content = f.read()

        # All prompts should be in final content
        for content in prompts.values():
            self.assertIn(content, final_content)

    def test_multiple_runs_produce_consistent_results(self):
        """Test that running main multiple times produces consistent results."""
        with open(os.path.join(self.prompts_dir, "test.txt"), "w") as f:
            f.write("Test content")

        # Run main twice
        main()
        with open("final_prompt.txt", "r") as f:
            content1 = f.read()

        main()
        with open("final_prompt.txt", "r") as f:
            content2 = f.read()

        self.assertEqual(content1, content2)


if __name__ == "__main__":
    unittest.main()
