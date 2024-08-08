import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import yt_dlp
import threading

def list_resolutions():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Hata", "Lütfen bir YouTube video linki girin.")
        return

    progress_var.set("Çözünürlükler alınıyor, lütfen bekleyin...")
    root.update_idletasks()

    def fetch_resolutions():
        try:
            ydl_opts = {'noplaylist': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                formats = info_dict.get('formats', [])

                unwanted_resolutions = ["storyboard", "Default", "low", "medium"]

                resolution_listbox.delete(0, tk.END)
                resolutions = []
                for fmt in formats:
                    resolution = fmt.get('format_note', None)
                    if resolution and resolution not in unwanted_resolutions and resolution not in resolutions:
                        resolutions.append(resolution)
                        resolution_listbox.insert(tk.END, resolution)

                if resolutions:
                    download_button.config(state=tk.NORMAL)
                else:
                    resolution_listbox.insert(tk.END, "Mevcut çözünürlük bulunamadı.")
                    download_button.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror("Hata", f"Hata: {e}")

        progress_var.set("")  # Clear progress message
        root.update_idletasks()

    threading.Thread(target=fetch_resolutions, daemon=True).start()

def download_video():
    selected_indices = resolution_listbox.curselection()
    url = url_entry.get()
    download_format = format_var.get()
    
    if download_format == "mp4" and not selected_indices:
        messagebox.showerror("Hata", "Lütfen bir çözünürlük seçin.")
        return

    progress_var.set("İndiriliyor, lütfen bekleyin...")
    root.update_idletasks()

    def download_process():
        try:
            if download_format == "mp4":
                selected_resolution = resolution_listbox.get(selected_indices[0])
                ydl_opts = {
                    'format': f'bestvideo[format_note={selected_resolution}]+bestaudio/best',
                    'outtmpl': '%(title)s.%(ext)s',
                    'merge_output_format': 'mp4',
                    'progress_hooks': [progress_bar],
                }
            elif download_format == "mp3":
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(title)s.%(ext)s',
                    'progress_hooks': [progress_bar],
                    'postprocessors': [
                        {
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        },
                        {
                            'key': 'FFmpegMetadata',
                        }
                    ],
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                if download_format == "mp3":
                    title = info_dict.get('title', 'Unknown Title')
                    artist = info_dict.get('uploader', 'Unknown Artist')
                    album = info_dict.get('album', 'Unknown Album')

                    ydl_opts['postprocessors'].append({
                        'key': 'FFmpegMetadata',
                        'add_metadata': True,
                        'metadata': {
                            'title': title,
                            'artist': artist,
                            'album': album
                        }
                    })

            messagebox.showinfo("Bilgi", "İndirme tamamlandı!")
        except Exception as e:
            messagebox.showerror("Hata", f"Hata: {e}")

        progress_var.set("")
        root.update_idletasks()

    threading.Thread(target=download_process, daemon=True).start()

def progress_bar(d):
    if d['status'] == 'downloading':
        downloaded_bytes = d.get('downloaded_bytes', 0)
        total_bytes = d.get('total_bytes', 1)  # Avoid division by zero
        percent = (downloaded_bytes / total_bytes * 100) if total_bytes else 0
        speed = d.get('speed', 0)
        eta = d.get('eta', 0)

        progress_var.set(f"İlerleme: {percent:.2f}% | Hız: {speed/1024:.2f} KB/s | Kalan Süre: {eta} sn")
        root.update_idletasks()
    elif d['status'] == 'finished':
        progress_var.set("İndirme tamamlandı, dosya işleniyor...")
        root.update_idletasks()

# GUI
root = tk.Tk()
root.title("YouTube Video İndirici")
root.geometry("500x600")
root.resizable(False, False)

# Stil Ayarları
style = ttk.Style()
style.theme_use('clam')

# Ana Çerçeve
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.pack(fill=tk.BOTH, expand=True)

# URL girişi
url_label = ttk.Label(main_frame, text="YouTube video linkini girin:")
url_label.pack(anchor=tk.W, pady=5)

url_entry = ttk.Entry(main_frame, width=60)
url_entry.pack(fill=tk.X, pady=5)

# Format seçimi
format_frame = ttk.LabelFrame(main_frame, text="İndirme Formatı", padding="10 10 10 10")
format_frame.pack(fill=tk.X, pady=10)

format_var = tk.StringVar(value="mp4")
mp4_radio = ttk.Radiobutton(format_frame, text="MP4 (Video)", variable=format_var, value="mp4", command=lambda: download_button.config(state=tk.DISABLED))
mp3_radio = ttk.Radiobutton(format_frame, text="MP3 (Ses)", variable=format_var, value="mp3", command=lambda: download_button.config(state=tk.NORMAL))
mp4_radio.pack(side=tk.LEFT, padx=5)
mp3_radio.pack(side=tk.LEFT, padx=5)

# Listeleme butonu
list_button = ttk.Button(main_frame, text="Çözünürlükleri Listele", command=list_resolutions)
list_button.pack(fill=tk.X, pady=5)

# Çözünürlük listesi
resolution_label = ttk.Label(main_frame, text="Mevcut çözünürlükler (MP4 için):")
resolution_label.pack(anchor=tk.W, pady=5)

resolution_listbox = tk.Listbox(main_frame, height=10)
resolution_listbox.pack(fill=tk.BOTH, expand=True, pady=5)

# İndirme butonu
download_button = ttk.Button(main_frame, text="İndir", command=download_video, state=tk.DISABLED)
download_button.pack(fill=tk.X, pady=10)

# İlerleme çubuğu
progress_var = tk.StringVar()
progress_bar_label = ttk.Label(main_frame, textvariable=progress_var)
progress_bar_label.pack(anchor=tk.W, pady=5)

# Kapatma işlemi
root.protocol("WM_DELETE_WINDOW", root.quit)

root.mainloop()
