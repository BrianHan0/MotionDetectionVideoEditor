from src.MotionDetection import motion_detector
from src.MotionGraph import GraphMotionPlot
from src.MotionGraph import plot_combined_motion_graph
videos = ["VideoSamples/production_id_4913621 (2160p).mp4","VideoSamples/video.mp4"]
motion_levels = []
video_boundaries = [0]  # Starting index of each video in the combined motion levels list

for i in videos:
    motion = motion_detector(i)
    motion_levels.extend(motion)
    video_boundaries.append(len(motion_levels))

plot_combined_motion_graph(motion_levels, video_boundaries)

