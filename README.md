# Drowsiness Detection System

## Overview
YOLOv5 model detecting driver drowsiness by classifying eye closure and yawning states using computer vision techniques.

## Performance Metrics
- Precision: 95.9%
- Recall: 94.4%
- mAP50: 99.5%
- mAP50-95: 73.7%

### Class-specific Performance
- Eyes Closed: 
  - Precision: 100%
  - Recall: 87.9%
- Eyes Open: 
  - Precision: 87.8%
  - Recall: 100%
- Yawning: 
  - Precision: 100%
  - Recall: 95.2%

## Dataset
- 3 classes: Eyes Closed, Eyes Open, Yawning
- Training data consisted of 74 images of eyes closed, 77 images of eyes open and 56 images of yawning. 
- Balanced multi-class dataset
- The images were frames extracted from video clips of a subject in both low lighting & bright lighting, wearing spectables and without them and with hair tied back and hair open and facing in different angles.
- The frames were labelled using labelImg.

