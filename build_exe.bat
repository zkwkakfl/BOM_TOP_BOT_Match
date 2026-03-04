@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo PyInstaller 설치 중...
pip install pyinstaller -q
echo.
echo 실행 파일(.exe) 빌드 중...
pyinstaller --noconfirm match_bom_top_bot.spec
echo.
if exist "dist\BOM_TOP_BOT_Match.exe" (
    echo 완료. dist\BOM_TOP_BOT_Match.exe 를 더블클릭하면 실행됩니다.
    explorer dist
) else (
    echo 빌드 실패. 위 오류 메시지를 확인하세요.
)
pause
