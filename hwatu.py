import os
import subprocess
import sys

# Pillow 라이브러리 자동 설치 확인
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("필요한 이미지 라이브러리를 설치합니다...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw, ImageFont

# hwatu 폴더 생성
os.makedirs("hwatu", exist_ok=True)

# 1~12월 화투패 그림을 정교하게 그려주는 함수
def draw_hwatu_card(month):
    # 카드 기본 캔버스 생성 (300x450 크기, 화투 고유의 미색 배경)
    img = Image.new("RGB", (300, 450), color=(253, 251, 238))
    draw = ImageDraw.Draw(img)

    # 전통 화투 테두리 (바깥 붉은색, 안쪽 금색 선)
    draw.rectangle([8, 8, 292, 442], outline=(185, 28, 28), width=8)
    draw.rectangle([16, 16, 284, 434], outline=(234, 179, 8), width=2)

    # 상단 월 표시 배지 (붉은 바탕에 흰 글자)
    draw.rectangle([65, 30, 235, 90], fill=(185, 28, 28))
    
    # 폰트 설정 (맥 기본 고딕 폰트)
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/AppleGothic.ttf", 34)
        font_mid = ImageFont.truetype("/System/Library/Fonts/AppleGothic.ttf", 26)
        font_small = ImageFont.truetype("/System/Library/Fonts/AppleGothic.ttf", 22)
    except:
        font_large = ImageFont.load_default()
        font_mid = ImageFont.load_default()
        font_small = ImageFont.load_default()

    draw.text((150, 60), f"{month}월 화투", fill=(255, 255, 255), anchor="mm", font=font_large)

    # 중앙 그림 영역 박스 (기본 테두리)
    draw.rectangle([35, 110, 265, 335], fill=(245, 240, 220), outline=(20, 20, 20), width=2)

    # 각 월별 화투패 '알맹이(문양)' 정밀 드로잉
    if month == 1:  # 1월 송학 (붉은 해, 소나무, 학)
        draw.rectangle([35, 110, 265, 335], fill=(20, 83, 45)) # 짙은 녹색 배경
        draw.ellipse([110, 125, 215, 230], fill=(220, 38, 38)) # 붉은 해
        draw.rectangle([140, 180, 160, 310], fill=(69, 26, 3))  # 소나무 기둥
        draw.ellipse([100, 150, 200, 200], fill=(21, 128, 61)) # 소나무 잎
        draw.text((150, 255), "🦩", fill=(255, 255, 255), anchor="mm", font=font_large) # 학 심볼
        name_str = "송학 (소나무·학)"

    elif month == 2:  # 2월 매조 (매화 가지, 꾀꼬리)
        draw.rectangle([35, 110, 265, 335], fill=(255, 241, 242))
        draw.arc([50, 130, 250, 310], start=180, end=360, fill=(90, 50, 20), width=10) # 매화 가지
        draw.ellipse([80, 170, 115, 205], fill=(244, 63, 94)) # 분홍 매화꽃
        draw.ellipse([170, 140, 205, 175], fill=(244, 63, 94))
        draw.text((130, 230), "🐦", font=font_large, anchor="mm") # 꾀꼬리
        name_str = "매조 (매화·꾀꼬리)"

    elif month == 3:  # 3월 벚꽃 (만막)
        draw.rectangle([35, 110, 265, 335], fill=(252, 231, 243))
        draw.ellipse([60, 130, 130, 200], fill=(244, 114, 182)) # 벚꽃송이 1
        draw.ellipse([140, 160, 220, 240], fill=(244, 114, 182)) # 벚꽃송이 2
        draw.polygon([(35, 300), (150, 240), (265, 300)], fill=(185, 28, 28)) # 막 커튼
        name_str = "벚꽃 (만막·광)"

    elif month == 4:  # 4월 흑싸리 (두견새)
        draw.rectangle([35, 110, 265, 335], fill=(220, 225, 230))
        draw.line([(80, 325), (110, 130)], fill=(30, 30, 30), width=8) # 싸리 나뭇가지
        draw.line([(200, 325), (170, 150)], fill=(30, 30, 30), width=8)
        draw.ellipse([90, 150, 125, 185], fill=(225, 29, 72)) # 붉은 꽃망울
        draw.text((150, 210), "🕊️", font=font_large, anchor="mm")
        name_str = "흑싸리 (두견새)"

    elif month == 5:  # 5월 난초 (창포)
        draw.rectangle([35, 110, 265, 335], fill=(243, 232, 255))
        draw.line([(80, 335), (100, 140)], fill=(22, 163, 74), width=6) # 창포 잎
        draw.line([(215, 335), (180, 140)], fill=(22, 163, 74), width=6)
        draw.ellipse([120, 160, 180, 220], fill=(147, 51, 234)) # 보라색 난초꽃
        name_str = "난초 (창포)"

    elif month == 6:  # 6월 모란 (나비)
        draw.rectangle([35, 110, 265, 335], fill=(254, 226, 226))
        draw.ellipse([90, 140, 210, 260], fill=(220, 38, 38)) # 모란 꽃잎
        draw.ellipse([115, 165, 185, 235], fill=(254, 202, 202))
        draw.text((150, 285), "🦋", font=font_large, anchor="mm") # 나비
        name_str = "모란 (나비)"

    elif month == 7:  # 7월 홍싸리 (멧돼지)
        draw.rectangle([35, 110, 265, 335], fill=(254, 215, 170))
        draw.line([(90, 335), (120, 130)], fill=(154, 52, 18), width=8) # 홍싸리 가지
        draw.ellipse([110, 140, 145, 175], fill=(234, 88, 12)) # 주황 꽃망울
        draw.text((150, 250), "🐗", font=font_large, anchor="mm") # 멧돼지
        name_str = "홍싸리 (멧돼지)"

    elif month == 8:  # 8월 공산 (보름달, 기러기)
        draw.rectangle([35, 110, 265, 335], fill=(17, 24, 39)) # 밤하늘
        draw.ellipse([95, 135, 205, 245], fill=(253, 224, 71)) # 보름달
        draw.text((110, 265), "🪿", font=font_small, anchor="mm") # 기러기 1
        draw.text((190, 285), "🪿", font=font_small, anchor="mm") # 기러기 2
        name_str = "공산 (보름달·기러기)"

    elif month == 9:  # 9월 국진 (국화, 술잔)
        draw.rectangle([35, 110, 265, 335], fill=(254, 249, 195))
        draw.ellipse([85, 130, 215, 260], fill=(234, 179, 8)) # 노란 국화
        draw.ellipse([115, 160, 185, 230], fill=(250, 204, 21))
        # 가운데 술잔(초장) 표현
        draw.rectangle([130, 280, 170, 320], fill=(220, 38, 38))
        draw.text((150, 300), "壽", fill=(254, 240, 138), font=font_small, anchor="mm")
        name_str = "국진 (국화·술잔)"

    elif month == 10: # 10월 단풍 (사슴)
        draw.rectangle([35, 110, 265, 335], fill=(254, 215, 170))
        draw.polygon([(150, 120), (100, 200), (200, 200)], fill=(194, 65, 12)) # 단풍잎
        draw.polygon([(150, 160), (110, 240), (190, 240)], fill=(220, 38, 38))
        draw.text((150, 275), "🦌", font=font_large, anchor="mm") # 사슴
        name_str = "단풍 (사슴)"

    elif month == 11: # 11월 오동 (봉황)
        draw.rectangle([35, 110, 265, 335], fill=(254, 252, 232))
        draw.rectangle([60, 130, 240, 155], fill=(31, 41, 55)) # 오동잎 1
        draw.rectangle([60, 170, 240, 195], fill=(31, 41, 55)) # 오동잎 2
        draw.text((150, 250), "🦅", font=font_large, anchor="mm") # 봉황
        name_str = "오동 (봉황·광)"

    else:             # 12월 비 (우산, 제비)
        draw.rectangle([35, 110, 265, 335], fill=(219, 234, 254))
        draw.line([(50, 130), (250, 130)], fill=(37, 99, 235), width=3) # 빗줄기
        draw.line([(50, 170), (250, 170)], fill=(37, 99, 235), width=3)
        draw.text((120, 240), "☂️", font=font_mid, anchor="mm") # 우산
        draw.text((180, 275), "🐦‍⬛", font=font_mid, anchor="mm") # 제비
        name_str = "비 (우산·제비)"

    # 하단 카드 이름 텍스트 출력
    draw.text((150, 385), name_str, fill=(31, 41, 55), anchor="mm", font=font_small)

    # hwatu 폴더에 PNG 파일로 저장
    img.save(f"hwatu/{month}.png")
    print(f"[{month}월] 알맹이 그림이 가득 찬 화투패 생성 완료: hwatu/{month}.png")

# 1월부터 12월까지 순서대로 생성
for m in range(1, 13):
    draw_hwatu_card(m)

print("모든 화투패 그림 생성 작업이 완료되었습니다!")