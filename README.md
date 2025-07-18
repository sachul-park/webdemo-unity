# 🏗️ Box Tower WebGL

Unity로 제작된 나무 상자 쌓기 게임의 WebGL 버전입니다.

## 🎮 게임 방법
- **스페이스바**를 눌러 나무 상자를 떨어뜨리세요
- 박스들이 물리 법칙에 따라 쌓여서 탑을 만듭니다
- 얼마나 높은 탑을 만들 수 있을까요?

## 🚀 로컬에서 실행하기

### 방법 1: Python 서버 사용 (권장)
```bash
# 이 폴더에서 실행
python server.py

# 또는 Python3 사용
python3 server.py
```

그 후 브라우저에서 `http://localhost:8000` 접속

### 방법 2: Node.js 서버 사용
```bash
# Node.js가 설치된 경우
npx http-server -p 8000

# 또는 live-server
npx live-server --port=8000
```

### 방법 3: PHP 서버 사용
```bash
# PHP가 설치된 경우
php -S localhost:8000
```

## 📁 파일 구조

```
Build/WebGL/
├── index.html          # 게임 메인 페이지
├── server.py           # Python 로컬 서버
├── README.md          # 이 파일
└── Build/             # Unity WebGL 빌드 파일들
    ├── BoxTower.loader.js
    ├── BoxTower.framework.js
    ├── BoxTower.data
    └── BoxTower.wasm
```

## 🔧 Unity 빌드 방법

Unity Editor에서 WebGL 빌드를 완료하려면:

1. **File → Build Settings** 열기
2. **Platform**을 **WebGL**로 변경
3. **Switch Platform** 클릭
4. **Build** 클릭하고 이 폴더 선택
5. 빌드 완료 후 위의 서버 방법 중 하나 사용

## 🌐 웹 배포하기

### GitHub Pages
1. GitHub 저장소에 이 폴더 업로드
2. Settings → Pages에서 배포 설정
3. `https://username.github.io/repository-name/` 접속

### Netlify
1. [Netlify](https://netlify.com)에 이 폴더 드래그&드롭
2. 자동으로 URL 생성됨

### Vercel
1. [Vercel](https://vercel.com)에 연결
2. 자동 배포 및 URL 생성

## 🎯 게임 기능

- ✅ 물리 기반 박스 쌓기
- ✅ 실시간 중력 시뮬레이션
- ✅ 나무 텍스처 적용
- ✅ 반응형 웹 디자인
- ✅ 키보드 입력 지원
- ✅ 웹 브라우저 최적화

## 🐛 문제 해결

### "게임이 로드되지 않음"
- Unity WebGL 빌드 파일들이 Build/ 폴더에 있는지 확인
- 브라우저 콘솔에서 오류 메시지 확인
- HTTPS 또는 로컬 서버에서 실행 (file:// 프로토콜 사용 안 함)

### "스페이스바가 작동하지 않음"
- 게임 화면을 한 번 클릭해서 포커스 활성화
- 브라우저가 WebGL을 지원하는지 확인

### "로딩이 너무 느림"
- 인터넷 연결 확인
- 브라우저 캐시 클리어
- 다른 브라우저에서 시도

## 📱 지원 브라우저

- ✅ Chrome (권장)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ❌ Internet Explorer (지원 안 함)

## 👨‍💻 개발 정보

- **엔진**: Unity 2022.3 LTS
- **플랫폼**: WebGL
- **언어**: C#, JavaScript, HTML5
- **텍스처**: 나무 재질 적용
- **물리**: Unity Physics System

---

🎮 **즐거운 게임 되세요!** 🏗️