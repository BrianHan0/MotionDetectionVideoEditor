from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import concatenate_videoclips


def find_high_motion_segments(motion_levels, video_boundaries, threshold):
    high_motion_segments = []
    start_frame = 0

    for end_frame in video_boundaries[1:]:
        segment_motion = motion_levels[start_frame:end_frame]
        if max(segment_motion) > threshold:
            peak_frame = start_frame + segment_motion.index(max(segment_motion))
            high_motion_segments.append(peak_frame)
        start_frame = end_frame

    return high_motion_segments

def cut_videos_at_segments(video_paths, high_motion_segments, segment_duration):
    clip_filenames = []
    for video_path in video_paths:
        with VideoFileClip(video_path) as video:
            for segment in high_motion_segments:
                start_time = max(segment - segment_duration / 2, 0)
                end_time = min(start_time + segment_duration, video.duration)
                if start_time < end_time:
                    output_filename = f"cut_clip_{start_time:.2f}_to_{end_time:.2f}.mp4"
                    ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=output_filename)
                    clip_filenames.append(output_filename)
    return clip_filenames


def create_final_video(clip_filenames, output_filename="final_video.mp4"):
    clips = [VideoFileClip(filename) for filename in clip_filenames]
    if not clip_filenames:
        print("No clips to concatenate.")
        return
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_filename)