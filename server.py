#!/usr/bin/env python3
"""
Box Tower WebGL 로컬 서버 (Gzip 지원)
Unity WebGL 빌드를 로컬에서 테스트하기 위한 HTTP 서버

Unity WebGL의 Gzip 압축 파일을 올바르게 서빙합니다.
"""

import http.server
import socketserver
import os
import sys
import mimetypes
from pathlib import Path

# 서버 설정
PORT = 8000
HOST = "localhost"

class UnityWebGLHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # CORS 헤더 추가 (개발용)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        
        # Unity WebGL Gzip 파일 처리
        if self.path.endswith('.js.gz'):
            self.send_header('Content-Type', 'application/javascript')
            self.send_header('Content-Encoding', 'gzip')
        elif self.path.endswith('.wasm.gz'):
            self.send_header('Content-Type', 'application/wasm')
            self.send_header('Content-Encoding', 'gzip')
        elif self.path.endswith('.data.gz'):
            self.send_header('Content-Type', 'application/octet-stream')
            self.send_header('Content-Encoding', 'gzip')
        elif self.path.endswith('.symbols.json.gz'):
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Encoding', 'gzip')
        # 압축되지 않은 Unity WebGL 파일들
        elif self.path.endswith('.wasm'):
            self.send_header('Content-Type', 'application/wasm')
        elif self.path.endswith('.js'):
            self.send_header('Content-Type', 'application/javascript')
        elif self.path.endswith('.data'):
            self.send_header('Content-Type', 'application/octet-stream')
        elif self.path.endswith('.symbols.json'):
            self.send_header('Content-Type', 'application/json')
        
        super().end_headers()

    def guess_type(self, path):
        """파일 타입 추측 - Unity WebGL 파일 확장자 지원"""
        mimetype, encoding = mimetypes.guess_type(path)
        
        # Unity WebGL 특수 확장자 처리
        if path.endswith('.unityweb'):
            return 'application/octet-stream', None
        elif path.endswith('.wasm'):
            return 'application/wasm', None
        elif path.endswith('.data'):
            return 'application/octet-stream', None
        elif path.endswith('.framework.js'):
            return 'application/javascript', None
        elif path.endswith('.loader.js'):
            return 'application/javascript', None
            
        return mimetype, encoding

def main():
    print("🎮 Box Tower WebGL 서버 시작 중...")
    print(f"📁 현재 디렉토리: {os.getcwd()}")
    
    # index.html 파일 확인
    if not os.path.exists("index.html"):
        print("❌ index.html 파일을 찾을 수 없습니다!")
        print("💡 Unity WebGL 빌드 폴더에서 이 스크립트를 실행하세요.")
        return
    
    # 빌드 파일들 확인
    build_dir = "Build"
    if os.path.exists(build_dir):
        build_files = os.listdir(build_dir)
        print(f"📦 빌드 파일들: {len(build_files)}개 발견")
        
        # Gzip 압축 파일 확인
        gz_files = [f for f in build_files if f.endswith('.gz')]
        if gz_files:
            print(f"🗜️  Gzip 압축 파일: {len(gz_files)}개")
            print("✅ Gzip Content-Encoding 헤더 지원 활성화됨")
        
        # 주요 파일들 확인
        expected_patterns = ['loader.js', 'framework.js', 'data', 'wasm']
        for pattern in expected_patterns:
            matching_files = [f for f in build_files if pattern in f]
            if matching_files:
                print(f"   ✅ {pattern}: {matching_files[0]}")
            else:
                print(f"   ⚠️  {pattern}: 찾을 수 없음")
    else:
        print("⚠️  Build/ 폴더를 찾을 수 없습니다.")
        print("💡 Unity에서 WebGL 빌드를 완료한 후 다시 시도하세요.")
    
    try:
        with socketserver.TCPServer((HOST, PORT), UnityWebGLHandler) as httpd:
            print(f"\n✅ Unity WebGL 서버가 시작되었습니다!")
            print(f"🌐 브라우저에서 접속: http://{HOST}:{PORT}")
            print(f"🎯 게임 플레이: 스페이스바를 눌러 박스를 떨어뜨리세요!")
            print(f"🗜️  Gzip 압축 지원: Unity WebGL 최적화 활성화")
            print("⏹️  서버 중지: Ctrl+C")
            print("-" * 60)
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 서버가 중지되었습니다.")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 포트 {PORT}가 이미 사용 중입니다.")
            print("💡 다른 터미널에서 서버가 실행 중인지 확인하세요.")
        else:
            print(f"❌ 서버 시작 실패: {e}")

if __name__ == "__main__":
    main()
