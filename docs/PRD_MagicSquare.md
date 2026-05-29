# PRD — Magic Square 4×4 TDD Practice

## 1. Executive Summary

4×4 부분 마방진(빈칸 2) 해결. 목표는 알고리즘보다 **계약·Dual-Track TDD·ECB·회귀 보호** 훈련.

## 2–4. Background / Problem / Why

Report/01 참조. "마방진 완성"이 아니라 **검증 가능한 불변식 만족**이 목표.

## 5. Target Users

TDD 학습자, ECB 연습자. 콘솔/pytest 중심 (UI 선택).

## 9. Scope

**In:** FR-01~05 (검증, 빈칸, 누락수, 판정, solver)  
**Out:** N×N 일반화, DB, Web API, 완전 생성 알고리즘

## 10. Functional Requirements

| FR | 설명 | Layer |
|----|------|-------|
| FR-01 | 입력 검증 | Boundary |
| FR-02 | 빈칸 2개 row-major | Entity |
| FR-03 | 누락 숫자 2개 오름차순 | Entity |
| FR-04 | 행·열·대각 합 34 | Entity |
| FR-05 | 두 조합 시도 → int[6] | Control+Entity |

## 12. I/O Contract

- 입력: `list[list[int]]` 4×4
- 성공: `{type:"OK", data:[r1,c1,n1,r2,c2,n2]}`
- 실패: `{type:"ERROR", error:{code, message}}`

## 13. Error Policy

E003(null), E001(size), E002(blanks), E004(range), E005(dup), E006(no solution). invalid 시 resolve 0회.

## 15. Dual-Track

Track A: `tests/boundary/` — 계약·격리  
Track B: `tests/entity/` — 불변식·solver

## 21. Traceability (요약)

| Invariant | Test |
|-----------|------|
| 4×4 | test_invalid_size |
| 빈칸 2 | test_blank_count |
| 합 34 | test_is_magic_square |
| int[6] 1-index | test_g1_reverse_success |
