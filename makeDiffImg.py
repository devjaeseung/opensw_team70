import cv2
import numpy as np

def makeImage():
    img = cv2.imread("images/cow2.jpg")
    cat = cv2.imread("images/cat.png", cv2.IMREAD_UNCHANGED)
    dog = cv2.imread("images/dog.png", cv2.IMREAD_UNCHANGED)
    eagle = cv2.imread("images/eagle.png", cv2.IMREAD_UNCHANGED)

    # 선택한 이미지 크기 조절
    img = cv2.resize(img, dsize=(600, 360))
    cat = cv2.resize(cat, dsize=(115, 77))
    dog = cv2.resize(dog, dsize=(104, 61))
    eagle = cv2.resize(eagle, dsize=(85, 57))

    insert_images = [cat, dog, eagle]

    inserted = []

    for insert_image in insert_images:
        h, w = insert_image.shape[:2]
        x, y = (0, 0)
        x = np.random.randint(0, img.shape[1] - w)
        y = np.random.randint(0, img.shape[0] - h)
        if len(inserted)==0:
          value = False
        else:
          value = True
        while value:
            x = np.random.randint(0, img.shape[1] - w)
            y = np.random.randint(0, img.shape[0] - h)
            for i in inserted:
                x1, y1 , x2, y2= i
                if x1<=x<=x2 or y1<=y<=y2:
                    value = True
                    break
                else:
                    value = False

        inserted.append((x, y, x+w, y+h))
        alpha_channel = insert_image[:, :, 3]
        insert_bgr = insert_image[:, :, :3]
        mask = alpha_channel[:, :, np.newaxis] / 255.0

        insert_bgr_resized = insert_bgr * mask
        background_roi = img[y:y + insert_image.shape[0], x:x + insert_image.shape[1]]
        background_roi_resized = background_roi * (1 - mask)

        img[y:y + insert_image.shape[0], x:x + insert_image.shape[1]] = insert_bgr_resized + background_roi_resized

    # 결과 이미지 표시
    cv2.imshow("result", img)
    cv2.imwrite("images/result_makeDiffImg.jpg", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

makeImage()