import os
import cv2


def extract_frames_from_videos(input_folder, output_folder, frame_rate):
    """
    Extract frames from all videos in subfolders and save them into a single folder for each class.
    Args:
        input_folder: Path to the folder containing videos organized in subfolders.
        output_folder: Path to the folder where frames will be saved.
        frame_rate: Save one frame every `frame_rate` frames.
    """
    for class_folder in os.listdir(input_folder):
        class_folder_path = os.path.join(input_folder, class_folder)
        
        if not os.path.isdir(class_folder_path):  
            continue
        
        output_class_folder = os.path.join(output_folder, class_folder)
        os.makedirs(output_class_folder, exist_ok=True)

        for video_file in os.listdir(class_folder_path):
            if video_file.endswith('.mp4'):
                video_path = os.path.join(class_folder_path, video_file)

                cap = cv2.VideoCapture(video_path)
                frame_count = 0
                success, frame = cap.read()

                while success:
                    if frame_count % frame_rate == 0:  
                        frame_filename = os.path.join(output_class_folder, f"{os.path.splitext(video_file)[0]}_frame_{frame_count}.jpg")
                        cv2.imwrite(frame_filename, frame)
                    success, frame = cap.read()
                    frame_count += 1

                cap.release()
                print(f"Extracted frames from {video_file} into {output_class_folder}")


if __name__ == "__main__":
    input_videos_folder = "data/videos" 
    output_frames_folder = "data/frames"  

    extract_frames_from_videos(input_videos_folder, output_frames_folder, frame_rate=20)