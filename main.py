from src.MotionProcessing.MotionDetection import motion_detector
from src.MotionProcessing.MotionGraph import plot_combined_motion_graph
from src.VideoEditing.VideoCutting import find_high_motion_segments, cut_videos_at_segments, create_final_video

def calculate_segment_duration(desired_total_duration, num_segments):
    if num_segments == 0:
        return 0
    return desired_total_duration / num_segments

videos = ["SampleVideos/video1.mp4","SampleVideos/video2.mp4","SampleVideos/video3.mp4","SampleVideos/video4.mp4","SampleVideos/video5.mp4","SampleVideos/video6.mp4","SampleVideos/video7.mp4","SampleVideos/video8.mp4"]
desired_total_duration = 6  # Desired total duration in seconds
motion,video = motion_detector(videos,True)
plot_combined_motion_graph(motion,video)
threshold = 1000  # Set a threshold for motion level
high_motion_segments = find_high_motion_segments(motion, video, threshold)

segment_duration = calculate_segment_duration(desired_total_duration, len(high_motion_segments))
clip_filenames = cut_videos_at_segments(videos, high_motion_segments, segment_duration)
create_final_video(clip_filenames)


