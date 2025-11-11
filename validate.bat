@echo off
REM validate.bat - Unified validation script for Windows (Python/JS/Markdown)
REM
REM Purpose:
REM   Runs all linters and validation checks across the repository
REM
REM Usage:
REM   validate.bat [--fix] [--verbose]
REM
REM Options:
REM   --fix       Auto-fix issues where possible
REM   --verbose   Show detailed output
REM
REM Exit Codes:
REM   0: All validations passed
REM   1: Validation failures detected

setlocal enabledelayedexpansion

REM Parse arguments
set VERBOSE=0
set FIX=0
set FAILURES=0

:parse_args
if "%~1"=="" goto :done_parsing
if /i "%~1"=="--verbose" set VERBOSE=1
if /i "%~1"=="-v" set VERBOSE=1
if /i "%~1"=="--fix" set FIX=1
if /i "%~1"=="-f" set FIX=1
shift
goto :parse_args
:done_parsing

REM Color codes (basic Windows CMD)
REM Note: Windows doesn't support ANSI colors in older versions
REM For better colors, use PowerShell or install Windows Terminal

echo ================================================
echo Repository Validation System
echo ================================================

REM 1. Python Validation
echo.
echo ------------------------------------------------
echo 1. Python Scripts
echo ------------------------------------------------

if exist "build.py" (
    set PYTHON_CMD=python build.py
    if %VERBOSE%==1 set PYTHON_CMD=!PYTHON_CMD! --verbose
    if %FIX%==1 set PYTHON_CMD=!PYTHON_CMD! --fix
    
    call !PYTHON_CMD!
    if errorlevel 1 (
        echo [FAIL] Python validation failed
        set /a FAILURES+=1
    ) else (
        echo [PASS] Python validation passed
    )
) else (
    echo [WARN] build.py not found, skipping Python validation
)

REM 2. JavaScript Validation
echo.
echo ------------------------------------------------
echo 2. JavaScript Files
echo ------------------------------------------------

set JS_FOUND=0
for /r %%f in (*.js) do (
    set filepath=%%f
    set filepath=!filepath:%CD%\=!
    
    REM Skip node_modules and .git
    echo !filepath! | findstr /i "node_modules .git" >nul
    if errorlevel 1 (
        set JS_FOUND=1
        
        REM Check Node.js syntax
        where node >nul 2>&1
        if !errorlevel! equ 0 (
            node -c "!filepath!" >nul 2>&1
            if !errorlevel! equ 0 (
                if %VERBOSE%==1 echo   [OK] !filepath!
            ) else (
                echo [FAIL] JavaScript syntax error in !filepath!
                set /a FAILURES+=1
            )
        )
    )
)

if %JS_FOUND%==0 (
    echo [INFO] No JavaScript files found
) else (
    REM Check if ESLint is available
    where eslint >nul 2>&1
    if !errorlevel! equ 0 (
        set ESLINT_CMD=eslint script/*.js
        if %FIX%==1 set ESLINT_CMD=!ESLINT_CMD! --fix
        
        call !ESLINT_CMD! >nul 2>&1
        if !errorlevel! equ 0 (
            echo [PASS] ESLint passed
        ) else (
            echo [WARN] ESLint found issues ^(not blocking^)
        )
    ) else (
        if %VERBOSE%==1 echo [INFO] ESLint not installed, skipping JS linting
    )
)

REM 3. Markdown Validation
echo.
echo ------------------------------------------------
echo 3. Markdown Files
echo ------------------------------------------------

set MD_COUNT=0
for /r %%f in (*.md) do (
    set filepath=%%f
    set filepath=!filepath:%CD%\=!
    
    REM Skip node_modules and .git
    echo !filepath! | findstr /i "node_modules .git" >nul
    if errorlevel 1 (
        set /a MD_COUNT+=1
    )
)

if %MD_COUNT% gtr 0 (
    echo [INFO] Found %MD_COUNT% Markdown files
    
    REM Check if markdownlint is available
    where markdownlint >nul 2>&1
    if !errorlevel! equ 0 (
        set MDL_CMD=markdownlint **/*.md
        if %FIX%==1 set MDL_CMD=!MDL_CMD! --fix
        
        call !MDL_CMD! >nul 2>&1
        if !errorlevel! equ 0 (
            echo [PASS] Markdown linting passed
        ) else (
            echo [WARN] Markdown linting found issues ^(not blocking^)
        )
    ) else (
        if %VERBOSE%==1 echo [INFO] markdownlint not installed, skipping
    )
) else (
    echo [INFO] No Markdown files found
)

REM 4. JSON Validation
echo.
echo ------------------------------------------------
echo 4. JSON Files
echo ------------------------------------------------

set JSON_FOUND=0
for /r %%f in (*.json) do (
    set filepath=%%f
    set filepath=!filepath:%CD%\=!
    
    REM Skip node_modules and .git
    echo !filepath! | findstr /i "node_modules .git" >nul
    if errorlevel 1 (
        set JSON_FOUND=1
        
        REM Validate JSON using Python
        python -m json.tool "!filepath!" >nul 2>&1
        if !errorlevel! equ 0 (
            if %VERBOSE%==1 echo   [OK] !filepath!
        ) else (
            echo [FAIL] Invalid JSON in !filepath!
            set /a FAILURES+=1
        )
    )
)

if %JSON_FOUND%==0 (
    echo [INFO] No JSON files found
)

REM Summary
echo.
echo ------------------------------------------------
echo Validation Summary
echo ------------------------------------------------

if %FAILURES%==0 (
    echo [PASS] All validations passed!
    exit /b 0
) else (
    echo [FAIL] Validation failed with %FAILURES% error^(s^)
    exit /b 1
)
