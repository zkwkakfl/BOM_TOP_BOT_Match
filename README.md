## Python port: BOM/TOP/BOT 매칭

엑셀(`.xlsx/.xlsm`)에서 BOM/TOP/BOT 시트를 읽고,
각 시트의 **자재이름/좌표명/소요량** 3개 범위를 기반으로

- 좌표명 셀 값을 `,` 기준으로 분리(Trim)
- **기본(자재명 기준)**: 자재별 BOM 수량 vs (TOP 수량 + BOT 수량) 매칭 (좌표는 TOP/BOT에 나뉘어 있어도 자재별 합으로 비교). 옵션으로 좌표+자재 키 기준 매칭도 가능.
- **BOM 기준**으로 TOP/BOT 각각 존재·수량 일치 여부 판정
- 시트별 좌표 중복(동일 좌표가 2회 이상 등장) 검출
- 결과를 새 엑셀 파일에 시트로 기록

을 수행합니다.

### 설치 및 실행

**방법 1) 패키지로 설치 (권장)** — 이 폴더에서:

```bash
pip install .
```

설치 후 어디서든 명령으로 실행:
- **GUI**: `bom-top-bot-match`
- **config**: `bom-top-bot-match --config config.json`

**방법 2) 폴더 복사 후 직접 실행**

1. 이 폴더 전체를 복사한 뒤, 해당 폴더에서:
   ```bash
   pip install -r requirements.txt
   python match_bom_top_bot.py
   ```
2. Windows에서 `run.bat` 더블클릭으로도 GUI 실행 가능.

- **엑셀에서 범위 가져오기**를 쓰려면 Windows에 **Microsoft Excel**이 설치되어 있어야 하며, `pywin32`가 설치됩니다.

### 실행 파일(.exe) 빌드 — 아이콘 클릭으로 실행

Python이 설치되지 않은 PC에서도 **아이콘 더블클릭**으로 실행하려면:

1. 이 폴더에서 **`build_exe.bat`** 더블클릭 (또는 터미널에서 실행)
2. 빌드가 끝나면 **`dist/BOM_TOP_BOT_Match.exe`** 가 생성됨
3. 이 **.exe 파일만** 다른 PC로 복사해 두고 더블클릭하면 프로그램 실행 (Python 설치 불필요)

- 첫 빌드 시 PyInstaller가 자동 설치되며, 완료까지 1~2분 걸릴 수 있습니다.
- **아이콘**을 바꾸려면 프로젝트 폴더에 `icon.ico`를 넣고, `match_bom_top_bot.spec`에서 `icon='icon.ico'` 주석을 해제한 뒤 다시 빌드하세요.

### 패키지 빌드 (pip 배포용)

```bash
pip install build
python -m build
```

`dist/` 폴더에 `.whl`(wheel)과 소스 배포(sdist)가 생성됩니다. 다른 PC에 설치할 때:
```bash
pip install dist/bom_top_bot_match-1.0.0-py3-none-any.whl
```

### 실행

**1) GUI (폼) 실행** — 파일·시트·범위를 화면에서 선택

```bash
python match_bom_top_bot.py
```

- BOM / TOP / BOT 파일 각각 선택, 저장 경로(선택), 시트·자재/좌표/수량 범위 입력 후 **매칭 실행**
- **범위를 엑셀에서 직접 선택**: 각 파일 옆 **엑셀에서 열기**로 파일을 엑셀에서 연 뒤, 시트에서 범위를 드래그하고 자재/좌표/수량 옆 **가져오기**를 누르면 폼에 자동 반영됩니다. (Windows, Microsoft Excel 설치 및 `pywin32` 필요)

**2) config 파일로 실행** — 단일 파일 또는 3개 파일 모드

- 단일 파일: `config_example.json` 참고 (`excel_path` 사용)
- 3개 파일: `config_example_3files.json` 참고 (`bom_file`, `top_file`, `bot_file` 사용)

```bash
python match_bom_top_bot.py --config config.json
```

### 출력 시트

| 시트 | 설명 |
|------|------|
| `Match_Result` | 전체 (coord, material)별 BOM/TOP/BOT 수량 및 상태 |
| `Unmatched` | BOM vs (TOP+BOT) 불일치 전체 |
| `Unmatched_TOP` | **BOM 기준** TOP만 비교 시 불일치 |
| `Unmatched_BOT` | **BOM 기준** BOT만 비교 시 불일치 |
| `Coord_Duplicates` | 시트별 좌표 중복 목록 |
| `Summary` | 매칭됨(OK) 건수, 불일치(TOP/BOT) 건수, 중복 좌표 수 |

### 주의

- 3개 범위는 **모두 1열**이어야 하며, **행 개수도 동일**해야 합니다.
- 좌표가 `A1, A2, A3`처럼 한 셀에 여러 개면 각 좌표로 확장되어 키가 생성됩니다.

