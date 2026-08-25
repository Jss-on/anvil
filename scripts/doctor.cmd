@echo off
rem doctor.cmd — Windows entry point for scripts/doctor.sh.
rem
rem In PowerShell/cmd, bare `bash` resolves to the WSL relay stub
rem (C:\Windows\System32\bash.exe) and dies with "execvpe(/bin/bash) failed"
rem when no WSL distro is installed. This shim finds Git for Windows' bash
rem and runs the real script with it. It NEVER falls back to bare `bash`.
rem
rem Override: set ANVIL_BASH to a specific bash.exe path.
setlocal enabledelayedexpansion

set "BASH="
if defined ANVIL_BASH if exist "%ANVIL_BASH%" set "BASH=%ANVIL_BASH%"

if not defined BASH (
  for /f "delims=" %%G in ('where git 2^>nul') do (
    if not defined BASH (
      if exist "%%~dpG..\bin\bash.exe" set "BASH=%%~dpG..\bin\bash.exe"
    )
  )
)
if not defined BASH if exist "%ProgramFiles%\Git\bin\bash.exe" set "BASH=%ProgramFiles%\Git\bin\bash.exe"
if not defined BASH if exist "%ProgramFiles(x86)%\Git\bin\bash.exe" set "BASH=%ProgramFiles(x86)%\Git\bin\bash.exe"
if not defined BASH if exist "%LocalAppData%\Programs\Git\bin\bash.exe" set "BASH=%LocalAppData%\Programs\Git\bin\bash.exe"

if not defined BASH (
  echo doctor.cmd: Git for Windows bash.exe not found.
  echo Install Git for Windows ^(winget install Git.Git^) or set ANVIL_BASH
  echo to a bash.exe path. The WSL bash stub in System32 is not usable here.
  exit /b 2
)

"%BASH%" "%~dp0doctor.sh" %*
exit /b %errorlevel%
