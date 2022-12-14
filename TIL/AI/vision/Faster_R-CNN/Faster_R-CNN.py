import torch
import torchvision
import cv2
import numpy as np
import sys
import coco_names
import random


model_path = './result/model_19.pth'
image_path='./imgs/1.jpg'
model_name ='fasterrcnn_resnet50_fpn'
dataset_name ='coco'
score_threshold = 0.8

def random_color():
    b = random.randint(0,255)
    g = random.randint(0,255)
    r = random.randint(0,255)

    return (b,g,r)


def main():
    input = []
    if dataset_name == 'coco':
        num_classes = 91
        names = coco_names.names

    # Model creating
    print("Creating model")
    model = torchvision.models.detection.__dict__[model_name](num_classes=num_classes, pretrained=True)
    model = model.cuda()

    model.eval()

    # save = torch.load(model_path)
    # model.load_state_dict(save['model'])

    # h, w, c
    src_img = cv2.imread(image_path)

    # BGR to RGB
    img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)

    # scale 0~1, shape c,h,w
    img_tensor = torch.from_numpy(img / 255.).permute(2, 0, 1).float().cuda()
    input.append(img_tensor)
    # 1,c,h,w
    out = model(input)
    boxes = out[0]['boxes']
    labels = out[0]['labels']
    scores = out[0]['scores']

    for idx in range(boxes.shape[0]):
        if scores[idx] >= score_threshold:
            x1, y1, x2, y2 = boxes[idx][0], boxes[idx][1], boxes[idx][2], boxes[idx][3]
            name = names.get(str(labels[idx].item()))
            # cv2.rectangle(img,(x1,y1),(x2,y2),colors[labels[idx].item()],thickness=2)
            print(src_img.shape, x1, y1, x2, y2)
            cv2.rectangle(src_img, (int(x1), int(y1)), (int(x2), int(y2)), random_color(), thickness=2)
            cv2.putText(src_img, text=name, org=(int(x1), int(y1) + 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.5, thickness=1, lineType=cv2.LINE_AA, color=(0, 0, 255))

    cv2.imwrite('imgs/output.png', src_img)

main()
