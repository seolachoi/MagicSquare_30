# MagicSquare_sa

4×4 부분 마방진(빈칸 2) — Dual-Track UI + Logic TDD 연습 프로젝트

## 구조

| 경로 | 설명 |
|------|------|
| `Report/` | 01~04 설계·문제정의 보고서 |
| `docs/` | PRD, To-Do |
| `Prompt/` | 대화형 프롬프트 · transcript |
| `src/boundary/` | 입력 검증, UIBoundary |
| `src/control/` | SolvePartialMagicSquare |
| `src/entity/` | 도메인 서비스 |
| `tests/` | Boundary + Entity + Golden Master |

## 진행 상태

- [x] 문제 인식 (STEP 1~5)
- [x] 아키텍처 / User Journey / PRD
- [x] `.cursorrules` + ECB 구현
- [x] Boundary + Domain 테스트 (GREEN)
- [x] Golden Master (G1)
- [ ] PyQt Screen UI (선택)
- [ ] 전체 RED 스켈레톤 50+건 (워크북 확장)

## 고정 계약

- 입력: 4×4, `0`=빈칸(2개), 값 `0` 또는 `1~16`
- 출력: `int[6]` `[r1,c1,n1,r2,c2,n2]` (1-index)
- Magic Constant: **34**

## 실행

```bash
cd magic_square
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest tests/ -v
```

## G1 예시

```python
from boundary.ui_boundary import UIBoundary

grid = [[16,2,3,13],[5,11,10,8],[9,7,0,12],[4,14,15,0]]
r = UIBoundary().solve(grid)
# OK -> data == [3, 3, 6, 4, 4, 1]
```

## 문서

- [문제 인식](Report/4x4-magic-square-problem-recognition.md)
- [PRD](docs/PRD_MagicSquare.md)
- [To-Do](docs/TODO_DEVELOPMENT.md)
