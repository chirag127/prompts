"""
Test Suite for gemini.py

Tests the Gemini API utility script configuration and structure.
Focuses on static analysis and configuration validation.
"""

import ast
import os
import re
import unittest


class TestGeminiConfiguration(unittest.TestCase):
    """Test cases for configuration values in gemini.py."""

    def setUp(self):
        """Read the script file once for all tests."""
        with open("script/gemini.py", "r") as f:
            self.content = f.read()
        self.tree = ast.parse(self.content)

    def test_generation_config_values(self):
        """Test that generation config contains expected values."""
        self.assertIn('"temperature": 1', self.content)
        self.assertIn('"top_p": 0.95', self.content)
        self.assertIn('"top_k": 64', self.content)
        self.assertIn('"max_output_tokens": 65536', self.content)
        self.assertIn('"response_mime_type": "text/plain"', self.content)

    def test_model_name(self):
        """Test that the correct model name is specified."""
        self.assertIn("gemini-2.5-flash-preview-04-17", self.content)

    def test_default_input_placeholder(self):
        """Test that the default input placeholder is present."""
        self.assertIn("INSERT_INPUT_HERE", self.content)

    def test_imports(self):
        """Test that required imports are present."""
        self.assertIn("import os", self.content)
        self.assertIn("import google.generativeai as genai", self.content)

    def test_api_key_from_environment(self):
        """Test that API key is read from environment variable."""
        self.assertIn('os.environ["GEMINI_API_KEY"]', self.content)

    def test_docstring_present(self):
        """Test that the script has a docstring."""
        self.assertIn('"""', self.content)
        self.assertIn("Gemini API Utility Script", self.content)

    def test_temperature_value(self):
        """Test that temperature is set to 1."""
        pattern = r'"temperature":\s*1[,\s]'
        self.assertIsNotNone(re.search(pattern, self.content))

    def test_max_output_tokens(self):
        """Test that max output tokens is 65536."""
        pattern = r'"max_output_tokens":\s*65536'
        self.assertIsNotNone(re.search(pattern, self.content))

    def test_response_mime_type(self):
        """Test that response mime type is text/plain."""
        self.assertIn('"response_mime_type": "text/plain"', self.content)

    def test_top_p_value(self):
        """Test that top_p is 0.95."""
        pattern = r'"top_p":\s*0\.95'
        self.assertIsNotNone(re.search(pattern, self.content))

    def test_top_k_value(self):
        """Test that top_k is 64."""
        pattern = r'"top_k":\s*64'
        self.assertIsNotNone(re.search(pattern, self.content))


class TestGeminiScriptStructure(unittest.TestCase):
    """Test the structure and organization of gemini.py."""

    def setUp(self):
        """Read the script file."""
        with open("script/gemini.py", "r") as f:
            self.content = f.read()

    def test_file_exists(self):
        """Test that gemini.py file exists."""
        self.assertTrue(os.path.exists("script/gemini.py"))

    def test_file_readable(self):
        """Test that gemini.py is readable."""
        self.assertIsNotNone(self.content)
        self.assertGreater(len(self.content), 0)

    def test_configuration_before_model_creation(self):
        """Test that API configuration happens before model creation."""
        config_pos = self.content.find("genai.configure")
        model_pos = self.content.find("GenerativeModel")

        self.assertLess(config_pos, model_pos)
        self.assertGreater(config_pos, 0)

    def test_model_before_chat(self):
        """Test that model is created before chat session."""
        model_pos = self.content.find("GenerativeModel")
        chat_pos = self.content.find("start_chat")

        self.assertLess(model_pos, chat_pos)
        self.assertGreater(model_pos, 0)

    def test_chat_before_message(self):
        """Test that chat is created before sending message."""
        chat_pos = self.content.find("start_chat")
        message_pos = self.content.find("send_message")

        self.assertLess(chat_pos, message_pos)
        self.assertGreater(chat_pos, 0)

    def test_message_before_print(self):
        """Test that message is sent before printing response."""
        message_pos = self.content.find("send_message")
        print_pos = self.content.find("print(response.text)")

        self.assertLess(message_pos, print_pos)
        self.assertGreater(message_pos, 0)

    def test_genai_configure_present(self):
        """Test that genai.configure is called."""
        self.assertIn("genai.configure", self.content)

    def test_generative_model_creation(self):
        """Test that GenerativeModel is instantiated."""
        self.assertIn("genai.GenerativeModel", self.content)

    def test_chat_session_created(self):
        """Test that start_chat is called."""
        self.assertIn("start_chat", self.content)

    def test_message_sent(self):
        """Test that send_message is called."""
        self.assertIn("send_message", self.content)

    def test_response_printed(self):
        """Test that response.text is printed."""
        self.assertIn("print(response.text)", self.content)


class TestGeminiAPIConfig(unittest.TestCase):
    """Test API configuration details."""

    def setUp(self):
        """Read the script file."""
        with open("script/gemini.py", "r") as f:
            self.content = f.read()

    def test_model_name_format(self):
        """Test that model name follows expected format."""
        self.assertIn("gemini-2.5-flash-preview-04-17", self.content)

    def test_generation_config_dict(self):
        """Test that generation_config is a dictionary."""
        self.assertIn("generation_config = {", self.content)

    def test_generation_config_assignment(self):
        """Test that generation_config is assigned to model."""
        self.assertIn("generation_config=generation_config", self.content)

    def test_chat_history_empty(self):
        """Test that chat history starts empty."""
        self.assertIn("history=[\n  ]", self.content)

    def test_api_key_variable_name(self):
        """Test that correct environment variable name is used."""
        self.assertIn("GEMINI_API_KEY", self.content)

    def test_model_variable_name(self):
        """Test that model is assigned to 'model' variable."""
        pattern = r"model\s*=\s*genai\.GenerativeModel"
        self.assertIsNotNone(re.search(pattern, self.content))

    def test_chat_session_variable(self):
        """Test that chat session is assigned to 'chat_session' variable."""
        pattern = r"chat_session\s*=\s*model\.start_chat"
        self.assertIsNotNone(re.search(pattern, self.content))

    def test_response_variable(self):
        """Test that response is assigned to 'response' variable."""
        pattern = r"response\s*=\s*chat_session\.send_message"
        self.assertIsNotNone(re.search(pattern, self.content))


class TestGeminiDocumentation(unittest.TestCase):
    """Test documentation and comments in gemini.py."""

    def setUp(self):
        """Read the script file."""
        with open("script/gemini.py", "r") as f:
            self.content = f.read()

    def test_module_docstring_exists(self):
        """Test that module has a docstring."""
        self.assertTrue(self.content.strip().startswith('"""'))

    def test_purpose_documented(self):
        """Test that purpose is documented."""
        self.assertIn("Purpose:", self.content)

    def test_usage_documented(self):
        """Test that usage is documented."""
        self.assertIn("Usage:", self.content)

    def test_configuration_documented(self):
        """Test that configuration is documented."""
        self.assertIn("Configuration:", self.content)

    def test_author_documented(self):
        """Test that author is documented."""
        self.assertIn("Author:", self.content)


class TestGeminiSyntax(unittest.TestCase):
    """Test Python syntax and structure."""

    def test_valid_python_syntax(self):
        """Test that the script has valid Python syntax."""
        with open("script/gemini.py", "r") as f:
            content = f.read()

        try:
            ast.parse(content)
            valid = True
        except SyntaxError:
            valid = False

        self.assertTrue(valid)

    def test_imports_at_top(self):
        """Test that imports are at the beginning of the file."""
        with open("script/gemini.py", "r") as f:
            content = f.read()

        # Find first import statement
        import_pos = content.find("import")

        # Check that imports appear early in file (within first 1000 chars)
        self.assertGreater(import_pos, 0)
        self.assertLess(import_pos, 1000)

    def test_no_syntax_errors(self):
        """Test that file can be parsed without syntax errors."""
        with open("script/gemini.py", "r") as f:
            content = f.read()

        try:
            compile(content, "gemini.py", "exec")
            has_errors = False
        except SyntaxError:
            has_errors = True

        self.assertFalse(has_errors)


class TestGeminiConstants(unittest.TestCase):
    """Test that constants are properly defined."""

    def setUp(self):
        """Read the script file."""
        with open("script/gemini.py", "r") as f:
            self.content = f.read()

    def test_model_name_constant(self):
        """Test that model name is defined."""
        self.assertIn("model_name=", self.content)

    def test_generation_config_defined(self):
        """Test that generation_config variable is defined."""
        self.assertIn("generation_config", self.content)

    def test_all_config_keys_present(self):
        """Test that all configuration keys are present."""
        required_keys = ["temperature", "top_p", "top_k", "max_output_tokens", "response_mime_type"]
        for key in required_keys:
            self.assertIn(f'"{key}"', self.content)


if __name__ == "__main__":
    unittest.main()
