#!/bin/bash
# validate.sh - Unified validation script for all languages (Python/JS/Markdown)
#
# Purpose:
#   Runs all linters and validation checks across the repository
#
# Usage:
#   ./validate.sh [--fix] [--verbose]
#
# Options:
#   --fix       Auto-fix issues where possible
#   --verbose   Show detailed output
#
# Exit Codes:
#   0: All validations passed
#   1: Validation failures detected

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Parse arguments
VERBOSE=false
FIX=false
for arg in "$@"; do
    case $arg in
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --fix|-f)
            FIX=true
            shift
            ;;
        *)
            ;;
    esac
done

# Track failures
FAILURES=0

# Helper functions
log_header() {
    echo -e "${BLUE}================================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}================================================${NC}"
}

log_section() {
    echo -e "\n${BLUE}$1${NC}"
    echo -e "${BLUE}------------------------------------------------${NC}"
}

log_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

log_error() {
    echo -e "${RED}✗ $1${NC}"
    ((FAILURES++))
}

log_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

log_info() {
    if [ "$VERBOSE" = true ]; then
        echo -e "  $1"
    fi
}

# Start validation
log_header "Repository Validation System"

# 1. Python Validation
log_section "1. Python Scripts"
if [ -f "build.py" ]; then
    PYTHON_CMD="python build.py"
    [ "$VERBOSE" = true ] && PYTHON_CMD="$PYTHON_CMD --verbose"
    [ "$FIX" = true ] && PYTHON_CMD="$PYTHON_CMD --fix"
    
    if $PYTHON_CMD; then
        log_success "Python validation passed"
    else
        log_error "Python validation failed"
    fi
else
    log_warning "build.py not found, skipping Python validation"
fi

# 2. JavaScript Validation
log_section "2. JavaScript Files"
JS_FILES=$(find . -name "*.js" -not -path "./node_modules/*" -not -path "./.git/*" 2>/dev/null || echo "")

if [ -n "$JS_FILES" ]; then
    # Check if Node.js is available
    if command -v node &> /dev/null; then
        log_info "Found JavaScript files, validating syntax..."
        
        for file in $JS_FILES; do
            if node -c "$file" 2>/dev/null; then
                log_info "  ✓ $file"
            else
                log_error "JavaScript syntax error in $file"
            fi
        done
        
        # Check if eslint is available
        if command -v eslint &> /dev/null; then
            ESLINT_CMD="eslint $JS_FILES"
            [ "$FIX" = true ] && ESLINT_CMD="$ESLINT_CMD --fix"
            
            if $ESLINT_CMD 2>/dev/null; then
                log_success "ESLint passed"
            else
                log_warning "ESLint found issues (not blocking)"
            fi
        else
            log_info "ESLint not installed, skipping JS linting"
        fi
    else
        log_warning "Node.js not found, skipping JavaScript validation"
    fi
else
    log_info "No JavaScript files found"
fi

# 3. Markdown Validation
log_section "3. Markdown Files"
MD_FILES=$(find . -name "*.md" -not -path "./node_modules/*" -not -path "./.git/*" 2>/dev/null || echo "")

if [ -n "$MD_FILES" ]; then
    MD_COUNT=$(echo "$MD_FILES" | wc -l)
    log_info "Found $MD_COUNT Markdown files"
    
    # Check if markdownlint is available
    if command -v markdownlint &> /dev/null || command -v markdownlint-cli &> /dev/null; then
        MDL_CMD="markdownlint"
        command -v markdownlint-cli &> /dev/null && MDL_CMD="markdownlint-cli"
        
        [ "$FIX" = true ] && MDL_CMD="$MDL_CMD --fix"
        
        if $MDL_CMD $MD_FILES 2>/dev/null; then
            log_success "Markdown linting passed"
        else
            log_warning "Markdown linting found issues (not blocking)"
        fi
    else
        log_info "markdownlint not installed, skipping Markdown linting"
        log_info "Install with: npm install -g markdownlint-cli"
    fi
else
    log_info "No Markdown files found"
fi

# 4. JSON Validation
log_section "4. JSON Files"
JSON_FILES=$(find . -name "*.json" -not -path "./node_modules/*" -not -path "./.git/*" 2>/dev/null || echo "")

if [ -n "$JSON_FILES" ]; then
    log_info "Validating JSON files..."
    
    for file in $JSON_FILES; do
        if python -m json.tool "$file" > /dev/null 2>&1 || jq empty "$file" > /dev/null 2>&1; then
            log_info "  ✓ $file"
        else
            log_error "Invalid JSON in $file"
        fi
    done
else
    log_info "No JSON files found"
fi

# Summary
log_section "Validation Summary"

if [ $FAILURES -eq 0 ]; then
    log_success "All validations passed!"
    exit 0
else
    log_error "Validation failed with $FAILURES error(s)"
    exit 1
fi
