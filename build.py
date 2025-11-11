#!/usr/bin/env python3
"""
Build Validation Script (build.py)

Purpose:
    Unified build validation system for the prompts repository.
    Validates all Python scripts, checks syntax, runs linting, and executes tests.

Usage:
    python build.py [--verbose] [--fix]

Options:
    --verbose    Show detailed output
    --fix        Auto-fix linting issues where possible

Exit Codes:
    0: All checks passed
    1: Validation failures detected

Author: Chirag Singhal (@chirag127)
"""

import argparse
import ast
import glob
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


class BuildValidator:
    def __init__(self, verbose: bool = False, fix: bool = False):
        self.verbose = verbose
        self.fix = fix
        self.errors = []
        self.warnings = []

    def log(self, message: str, level: str = "INFO"):
        """Log messages based on verbosity settings."""
        if self.verbose or level in ["ERROR", "WARNING"]:
            prefix = {"INFO": "[i]", "ERROR": "[x]", "WARNING": "[!]", "SUCCESS": "[+]"}
            print(f"{prefix.get(level, '[-]')} {message}")

    def find_python_files(self) -> List[Path]:
        """Find all Python files in the repository."""
        python_files = []
        for pattern in ["**/*.py"]:
            python_files.extend(Path(".").glob(pattern))
        return sorted([f for f in python_files if not str(f).startswith(".")])

    def validate_syntax(self, file_path: Path) -> bool:
        """Validate Python syntax by parsing the AST."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                ast.parse(f.read(), filename=str(file_path))
            self.log(f"Syntax valid: {file_path}", "SUCCESS")
            return True
        except SyntaxError as e:
            self.errors.append(f"Syntax error in {file_path}: {e}")
            self.log(f"Syntax error in {file_path}: {e}", "ERROR")
            return False
        except Exception as e:
            self.errors.append(f"Failed to parse {file_path}: {e}")
            self.log(f"Failed to parse {file_path}: {e}", "ERROR")
            return False

    def run_command(self, cmd: List[str], description: str) -> Tuple[bool, str]:
        """Run a shell command and return success status and output."""
        try:
            self.log(f"Running: {description}", "INFO")
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=False,
            )
            output = result.stdout + result.stderr
            if result.returncode == 0:
                self.log(f"{description}: PASSED", "SUCCESS")
                return True, output
            else:
                self.log(f"{description}: FAILED", "ERROR")
                return False, output
        except FileNotFoundError:
            msg = f"{description}: Tool not found ({cmd[0]})"
            self.warnings.append(msg)
            self.log(msg, "WARNING")
            return True, ""
        except Exception as e:
            msg = f"{description}: Exception - {e}"
            self.errors.append(msg)
            self.log(msg, "ERROR")
            return False, str(e)

    def check_flake8(self, files: List[Path]) -> bool:
        """Run flake8 linting on Python files."""
        if not files:
            return True
        cmd = ["flake8"] + [str(f) for f in files]
        success, output = self.run_command(cmd, "Flake8 linting")
        if not success and output:
            self.errors.append(f"Flake8 errors:\n{output}")
            if self.verbose:
                print(output)
        return success

    def check_black(self, files: List[Path]) -> bool:
        """Run black formatting check on Python files."""
        if not files:
            return True
        cmd = ["black", "--check"] if not self.fix else ["black"]
        cmd += [str(f) for f in files]
        action = "Formatting" if self.fix else "Format check"
        success, output = self.run_command(cmd, f"Black {action}")
        if not success and output:
            self.errors.append(f"Black formatting issues:\n{output}")
            if self.verbose:
                print(output)
        return success or self.fix

    def run_tests(self) -> bool:
        """Run pytest if test files exist."""
        test_files = list(Path(".").glob("**/test_*.py")) + list(
            Path(".").glob("**/*_test.py")
        )
        if not test_files:
            self.log("No test files found, skipping tests", "INFO")
            return True

        cmd = ["pytest", "-v"] if self.verbose else ["pytest"]
        success, output = self.run_command(cmd, "Running tests")
        if not success and output:
            self.errors.append(f"Test failures:\n{output}")
            if self.verbose:
                print(output)
        return success

    def validate_all(self) -> bool:
        """Run all validation checks."""
        print("=" * 60)
        print("Build Validation System")
        print("=" * 60)

        # Find Python files
        python_files = self.find_python_files()
        if not python_files:
            self.log("No Python files found", "WARNING")
            return True

        self.log(f"Found {len(python_files)} Python file(s)", "INFO")

        # Syntax validation
        print("\n1. Syntax Validation")
        print("-" * 60)
        syntax_valid = all(self.validate_syntax(f) for f in python_files)

        if not syntax_valid:
            print("\n⚠ Syntax errors detected, skipping further checks")
            return False

        # Linting
        print("\n2. Linting (Flake8)")
        print("-" * 60)
        flake8_passed = self.check_flake8(python_files)

        print("\n3. Formatting (Black)")
        print("-" * 60)
        black_passed = self.check_black(python_files)

        # Tests
        print("\n4. Running Tests")
        print("-" * 60)
        tests_passed = self.run_tests()

        # Summary
        print("\n" + "=" * 60)
        print("Validation Summary")
        print("=" * 60)

        results = {
            "Syntax": syntax_valid,
            "Flake8": flake8_passed,
            "Black": black_passed,
            "Tests": tests_passed,
        }

        for check, passed in results.items():
            status = "[+] PASSED" if passed else "[x] FAILED"
            self.log(f"{check}: {status}", "SUCCESS" if passed else "ERROR")

        if self.warnings:
            print(f"\n[!] Warnings: {len(self.warnings)}")
            for warning in self.warnings:
                print(f"  - {warning}")

        if self.errors:
            print(f"\n[x] Errors: {len(self.errors)}")
            if not self.verbose:
                print("  Run with --verbose for detailed output")

        all_passed = all(results.values())
        print("\n" + "=" * 60)
        if all_passed:
            print("[+] All validations passed!")
        else:
            print("[x] Validation failed")
        print("=" * 60)

        return all_passed


def main():
    parser = argparse.ArgumentParser(
        description="Validate Python scripts in the repository"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show detailed output"
    )
    parser.add_argument(
        "--fix", "-f", action="store_true", help="Auto-fix linting issues where possible"
    )
    args = parser.parse_args()

    validator = BuildValidator(verbose=args.verbose, fix=args.fix)
    success = validator.validate_all()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
