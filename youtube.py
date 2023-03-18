import os
import ffmpeg

def Download_Video():
    url = YouTube(str(link.get()))

    # Ask user for the output directory
    output_path = filedialog.asksaveasfilename(defaultextension=".mp4")

    # Check if user wants to download audio only
    if mp3_var.get() == 1:
        audio_stream = url.streams.filter(only_audio=True).first()
        audio_file_path = os.path.splitext(output_path)[0] + ".mp3"
        audio_stream.download(output_path=output_path)
        audio = ffmpeg.input(output_path)
        audio = ffmpeg.output(audio, audio_file_path, format='mp3')
        ffmpeg.run(audio)
        os.remove(output_path)
    else:
        video_stream = url.streams.first()
        video_stream.download(output_path=output_path)

    tk.Label(window, text='Success!', font='arial 15 bold', fg='white', bg='black', padx=2).place(x=485, y=145)
