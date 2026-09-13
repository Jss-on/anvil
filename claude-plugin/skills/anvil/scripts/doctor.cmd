@echo off
rem Windows launcher: use Git Bash, never the System32 WSL relay.
rem Keep this file ASCII with CRLF for Windows command processors.
setlocal
set "ANVIL_BASH_EXE="
if defined ANVIL_BASH if exist "%ANVIL_BASH%" set "ANVIL_BASH_EXE=%ANVIL_BASH%"
if not defined ANVIL_BASH_EXE (
  for /f "delims=" %%G in ('where git 2^>nul') do (
    if not defined ANVIL_BASH_EXE (
      if exist "%%~dpG..\bin\bash.exe" set "ANVIL_BASH_EXE=%%~dpG..\bin\bash.exe"
    )
  )
)
if not defined ANVIL_BASH_EXE if exist "%ProgramFiles%\Git\bin\bash.exe" set "ANVIL_BASH_EXE=%ProgramFiles%\Git\bin\bash.exe"
if not defined ANVIL_BASH_EXE if exist "%ProgramFiles(x86)%\Git\bin\bash.exe" set "ANVIL_BASH_EXE=%ProgramFiles(x86)%\Git\bin\bash.exe"
if not defined ANVIL_BASH_EXE if exist "%LocalAppData%\Programs\Git\bin\bash.exe" set "ANVIL_BASH_EXE=%LocalAppData%\Programs\Git\bin\bash.exe"
if not defined ANVIL_BASH_EXE (
  echo doctor.cmd: install Git for Windows or set ANVIL_BASH to its bash.exe.
  exit /b 2
)
"%ANVIL_BASH_EXE%" "%~dp0doctor.sh" %*
exit /b %errorlevel%
