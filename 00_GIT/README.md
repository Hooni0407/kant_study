# Git Tutorial

```bash # bash도 가능하고 shell도 가능함
# 깃 초기화
git init

# 스테이징에 추가
git add . # 현재폴더를 기준으로 해서 전부다 커밋하는 명령어
git add -A  # 폴더 전체 커밋하는 명령어
```

```bash
# Commit
git commit -m "commit message..."
```

```bash
# push command
git push origin main
```

```sh
# git 로그 명령어

git log
git log --oneline
git log --oneline --all

```

### 브랜치 생성 및 스위치

```sh
git branch 브랜치명
git checkout 브랜치명

git checkout -b 브랜치명
```