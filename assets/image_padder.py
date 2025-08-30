import cv2
import os

images_path = os.listdir('image')

# yoonki_로 시작하는 경우는 제외
images_path = [img for img in images_path if not img.startswith('yoonki_')]
images_path = [img for img in images_path if not img.startswith('padded_')]
print(images_path)


# --- 설정 ---
INPUT_FOLDER = 'image'
OUTPUT_PREFIX = 'padding_img/'
TARGET_WIDTH = 493 # 1200
TARGET_HEIGHT = 288 # 630
# --- 설정 끝 ---

# 목표 비율 계산
target_ratio = TARGET_WIDTH / TARGET_HEIGHT

for img_name in images_path:
    # 이미지 경로 조합
    img_path = os.path.join(INPUT_FOLDER, img_name)
    
    # 이미지 읽기
    image = cv2.imread(img_path)

    # 이미지를 제대로 읽지 못한 경우 건너뛰기
    if image is None:
        print(f"경고: '{img_name}' 파일을 읽을 수 없습니다. 건너뜁니다.")
        continue

    h, w, _ = image.shape
    current_ratio = w / h

    
    # 1. 최종 이미지의 가로, 세로 크기 결정
    if current_ratio > target_ratio:
        # 원본이 목표보다 가로로 넓은 경우 (가로 기준)
        final_w = w
        final_h = int(final_w / target_ratio)
    else:
        # 원본이 목표보다 세로로 길거나 같은 경우 (세로 기준)
        final_h = h
        final_w = int(final_h * target_ratio)

    if img_name == 'anonymizing_at_home_fitness.png':
        final_h=int(final_h*1.1)
        final_w=int(final_w*1.1)

    # 2. 추가해야 할 여백(padding) 계산
    pad_top = (final_h - h) // 2
    pad_bottom = final_h - h - pad_top
    pad_left = (final_w - w) // 2
    pad_right = final_w - w - pad_left

    # 3. cv2.copyMakeBorder 함수로 여백 추가
    #    BORDER_CONSTANT : 상수 값으로 채우는 옵션
    #    value=[255, 255, 255] : 흰색 (BGR 순서)
    padded_image = cv2.copyMakeBorder(
        image, 
        pad_top, 
        pad_bottom, 
        pad_left, 
        pad_right, 
        cv2.BORDER_CONSTANT, 
        value=[255, 255, 255]
    )

    # 4. 결과 이미지 저장
    output_path = os.path.join(INPUT_FOLDER, f'{OUTPUT_PREFIX}{img_name}')
    cv2.imwrite(output_path, padded_image)
    print(f"'{img_name}' ({w}x{h}) -> '{output_path}' ({final_w}x{final_h}) 처리 완료")

print("\n모든 작업이 완료되었습니다.")

# for img in images_path:
#     image = cv2.imread(f'image/{img}')
#     # target ratio 1200:630
#     target_ratio = 1200 / 630
#     h, w, _ = image.shape
#     current_ratio = w / h
#     # 화질 가능한 유지한채 비율을 1200:630으로 만들기
#     if current_ratio > target_ratio:
#         # Resize to fit width
#         new_width = 1200
#         new_height = int(new_width / current_ratio)
#     else:
#         # Resize to fit height
#         new_height = 630
#         new_width = int(new_height * current_ratio)

#     padded_image = cv2.resize(image, (new_width, new_height))
#     cv2.imwrite(f'image/padded_{img}', padded_image)
#     print(f'Padded {img} to {new_width}x{new_height}')
