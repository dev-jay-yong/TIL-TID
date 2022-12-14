### Object Detection
- 객체 탐지는 컴퓨터 비전과 이미지 처리와 관련된 컴퓨터 기술
- 디지털 <b>이미지와 비디오</b>로 특정한 계열의 <b>시맨틱 객체 인스턴스</b>를 감지하는 일을 다룸.
- 잘 연구된 객체 탐지 분야로는 얼굴 검출, 보행자 검출이 포함됨.

![image](https://user-images.githubusercontent.com/96015600/202266941-e818bee6-fc99-4bf9-a9de-fdcdaf9ba37b.png)

출처 - [medium.com](https://medium.com/zylapp/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)

Classification - 개, 고양이 분류까지 가능
Classification, Localization - 고양이 분류 이후 그림 안의 고양이 위치 특정 가능
Object Detection - 여러개의 클래스마다 박스로써 대략적인 위치를 라벨링
Instance Segmentaion - 여러개의 클래스마다 픽셀단위로 위치를 라벨링

### Selective search (선택적 탐색) 기법 (IJCV 2013)
오버랩을 허용하지 않고 bottom up 방식으로써 문제해결

<b>방식</b>
1. Performing segmentaion (pixel-level)
2. merging segments
3. localizing boxes

<b>단점</b>
region proposal 과정이 실제 object detection CNN과 별도로 이루어지기 때문에,<b>
selective search를 사용하면 end-to-end로 학습이 불가능하고, 실시간 적용에도 어려움이 있음</b>

![selectedSearch](https://user-images.githubusercontent.com/96015600/202269002-3cc01597-258b-4621-b40d-7d43e7a2943e.png)

출처 - [Selective Search for Object Recognition 논문](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf)

### R-CNN(TPAMI 2016) - CNN에 적용된 Selective Search
- Classification of region proposals
    - Using CNN features for image classification
    - Including background as an additional class
    - Ground truth label augmentation using IoU

![R-CNN](https://user-images.githubusercontent.com/96015600/202271328-fda22dc6-a4f5-4b97-adc4-7b2a47a0bba5.png)

출처 - [Region-base Convolutional Networks for Accurate Object Detection and Segmentation 논문](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf)


### R-CNN의 단점을 3가지 방법으로 개선한 Fast R-CNN (ICCV 2015)
- Fast inference
  - CNN extracts feature maps only once for an image
- End-to-end training
  - Removing SVM for classification
- Multi-task learning
  - Classification and bounding box regression

![image](https://user-images.githubusercontent.com/96015600/202274351-969895d4-0c77-4196-90a1-f8dd33cd13aa.png)
출처 - [Fast R-CNN 논문](https://arxiv.org/pdf/1504.08083.pdf)


### Fast R-CNN에서 사용한 ROI polling layer
- Region of Interest (RoI) polling layer
  - Extracting RoI using selective search
  - Seleteing sub-window for pooling
  - Performing max pooling for each sub-window

---
###Faster R-CNN VS Fast R-CNN
![Fast-Rcnn](assets/Fast-rcnn%20아키텍쳐.png)

Fast R-CNN은 위 이미지에서 RoI projection 부분에서 아직 Selective search를 사용하여 연산이 매우 느림<br>
하지만 Faster R-CNN은 이러한 부분까지 Region Propsal을 딥러닝을 이용하여 구현하였음.

![Faster-Rcnn 메인 피규어](assets/Faster-rcnn%20아키텍쳐.png)

