import argparse
import json
import os

from moviepy.editor import VideoFileClip


def add_metadata(video_path: str, metadata: dict[str, str]):
    print(f"Add metadata {metadata} to {video_path}")

    temp_output_video = None

    try:
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Input video file not found: {video_path}")

        print("Loading video...")
        video = VideoFileClip(video_path)
        print(f"Video loaded: {video.fps}fps, {video.duration}s")

        input_dir = os.path.dirname(os.path.abspath(video_path))
        base, ext = os.path.splitext(os.path.basename(video_path))
        temp_output_video = os.path.join(input_dir, f"{base}_temp{ext}")

        print(f"Temporary output file will be: {temp_output_video}")

        # Available metadata keys: https://wiki.multimedia.cx/index.php/FFmpeg_Metadata
        ffmpeg_params = ["-metadata", f"comment={json.dumps(metadata)}"]
        video.write_videofile(
            temp_output_video,
            codec="libx264",
            audio_codec="aac",
            fps=video.fps,
            verbose=True,
            logger=None,
            ffmpeg_params=ffmpeg_params,
        )
        video.close()
        print("Successfully wrote to temporary file.")

        print(f"Removing original file: {video_path}")
        os.remove(video_path)
        print("Original file removed.")

        print(f"Renaming: {temp_output_video} -> {video_path}")
        os.rename(temp_output_video, video_path)
        temp_output_video = None
        print("File successfully renamed.")

        print(f"Metadata addition completed for: {video_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add metadata to a video file.")
    parser.add_argument(
        "--video_path", type=str, required=True, help="Path to the video file."
    )
    parser.add_argument(
        "--metadata",
        type=str,
        required=True,
        help='Metadata as a JSON string (e.g., \'{"title":"My Video", "artist":"Me"}\').',
    )
    args = parser.parse_args()
    add_metadata(args.video_path, json.loads(args.metadata))
