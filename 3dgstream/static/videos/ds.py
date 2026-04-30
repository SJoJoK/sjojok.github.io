import subprocess
import os

video_files = ['coffee_martini.mp4',
               'cook_spinach.mp4',
               'cut_roasted_beef.mp4',
               'flame_salmon.mp4',
               'flame_steak.mp4',
               'sear_steak.mp4'] 

for video_file in video_files:
    # 检查文件是否存在
    if not os.path.isfile(video_file):
        print(f"File {video_file} does not exist. Skipping.")
        continue

    # 构造新的文件名
    name, ext = os.path.splitext(video_file)
    new_file = f"{name}_low_res{ext}"

    # 使用 ffmpeg 下采样二倍
    cmd = f"ffmpeg -i {video_file} -vf scale=iw/2:-1 {new_file}"
    try:
        # 执行命令
        subprocess.run(cmd, check=True, shell=True)
        print(f"Downsampled video saved as {new_file}")
    except subprocess.CalledProcessError as e:
        # 如果 ffmpeg 执行失败，打印错误信息
        print(f"Failed to downsample video {video_file}: {e}")

# 脚本结束
print("Script completed.")