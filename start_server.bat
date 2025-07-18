@echo off
echo 🎮 Box Tower WebGL 서버 시작 중...
echo.

REM Python 설치 확인
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python이 설치되어 있지 않습니다!
    echo 💡 https://python.org 에서 Python을 다운로드하세요.
    pause
    exit /b 1
)

REM index.html 파일 확인
if not exist "index.html" (
    echo ❌ index.html 파일을 찾을 수 없습니다!
    echo 💡 Unity WebGL 빌드 폴더에서 이 배치 파일을 실행하세요.
    pause
    exit /b 1
)

echo ✅ Python 설치 확인됨
echo 🌐 브라우저에서 http://localhost:8000 으로 접속하세요
echo ⏹️  서버 중지: Ctrl+C
echo.
echo 🚀 서버 시작 중...
echo.

REM Python 서버 시작
python server.py

pause