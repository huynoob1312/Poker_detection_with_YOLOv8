from ultralytics import YOLO
import cv2
from poker_rank import poker_rank
import torch
from argparse import ArgumentParser


categories = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']
def get_args():
    parser = ArgumentParser(description="poker test webcam")
    parser.add_argument("--conf_threshold", "-c" ,type= float, default=0.5, help="Confident threshold")


    args = parser.parse_args()
    return args

def test_webcam(args):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = YOLO(model='./poker.pt')
    model.to(device)

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # width
    cap.set(4, 480)   # height
    while cap.isOpened():
        flag, frame = cap.read()
        if not flag:
            break

        results = model(frame, conf = args.conf_threshold)
        cards = []
        bboxes = results[0].boxes

        for bbox in bboxes:
            conf = float(bbox.conf[0])
            cls_id = int(bbox.cls[0])
            x1,y1,x2,y2 = map(int, bbox.xyxy[0])

            label = '{} conf: {:.2f}'.format(categories[cls_id], conf)
            cards.append(categories[cls_id])

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label,(x1, y1 - 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cards = list(set(cards))
        if len(cards) == 7:
            res = poker_rank(cards)
            cv2.putText(frame, "Rank: {}".format(res),
                        (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        cv2.imshow("Poker Detection", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    args = get_args()
    test_webcam(args)