class config:
    BOT_TOKEN = ""
    APP_ID = ""
    API_HASH = ""
    DATABASE_URL = ""
    SUDO_USERS = "" # Sepearted by space.
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = ""
    G_DRIVE_CLIENT_SECRET = ""
    SUPPORT_CHAT_LINK = ""


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**{}.**\n__Halo .__\n__Kamu bisa lebih tau dengan mengirim /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\n__Aku bisa mengupload file kamu ke Google Drive. Kamu harus memberi aku izin sebelum memulai  nya.__\n\nAku punya fitur baru... ! Mau tau ? Silahkan baca dengan cermat ya.",
        
        f"**Memberi izin aku**\n__Send the /{BotCommands.Authorize[0]} commmand and you will receive a URL, visit URL and follow the steps and send the received code here. Use /{BotCommands.Revoke[0]} to revoke your currently logged Google Drive Account.__\n\n**Note: I will not listen to any command or message (except /{BotCommands.Authorize[0]} command) until you authorize me.\nSo, Authorization is mandatory !**",
        
        f"**Direct Links**\n__Send me a direct download link for a file and i will download it on my server and Upload it to your Google Drive Account. You can rename files before uploading to GDrive Account. Just send me the URL and new filename separated by ' | '.__\n\n**__Examples:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**Telegram Files**\n__To Upload telegram files in your Google drive Account just send me the file and i will download and upload it to your Google Drive Account. Note: Telegram Files Downloading are slow. it may take longer for big files.__\n\n**YouTube-DL Support**\n__Download files via youtube-dl.\nUse /{BotCommands.YtDl[0]} (YouTube Link/YouTube-DL Supported site link)__",
        
        f"**Custom Folder for Upload**\n__Want to upload in custom folder or in__ **TeamDrive** __ ?\nUse /{BotCommands.SetFolder[0]} (Folder URL) to set custom upload folder.\nAll the files are uploaded in the custom folder you provide.__",
        
        f"**Delete Google Drive Files**\n__Delete google drive files. Use /{BotCommands.Delete[0]} (File/Folder URL) to delete file or reply /{BotCommands.Delete[0]} to bot message.\nYou can also empty trash files use /{BotCommands.EmptyTrash[0]}\nNote: Files are deleted permanently. This process cannot be undone.\n\n**Copy Google Drive Files**\n__Yes, Clone or Copy Google Drive Files.\n__Use /{BotCommands.Clone[0]} (File id / Folder id or URL) to copy Google Drive Files in your Google Drive Account.__",
        
        "**Rules & Precautions**\n__1. Don't copy BIG Google Drive Files/Folders. It may hang the bot and your files maybe damaged.\n2. Send One request at a time unless bot will stop all processes.\n3. Don't send slow links @transload it first.\n4. Don't misuse, overload or abuse this free service.__",
        
        # Dont remove this ↓ if you respect developer.
         
        "**Dibuat dengan ❤ oleh @lhaituyandicari**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Oopss!.**\n__Kamu mencapai batas maksimum, coba lagi setelah 24 jam yaa.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File atau Folder tdk dapat ditemukan.**\n__File id - {} Not found. Pastikan itu dapat diakses oleh akun yang kamu gunakan.__"
    
    INVALID_GDRIVE_URL = "❗ **Upss ada yang salah!**\nPeriksa lagi url nya ya."
    
    COPIED_SUCCESSFULLY = "✅ **Salin sukses!!.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **Kamu belum memberikan izin apapun untuk ku.**\n__Klik /{BotCommands.Authorize[0]} untuk memberiku izin.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Sedang di unggah**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Mengunggah selesai...**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Yah, gagal nih**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Mendownload file\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Terima kasih sudah memberiku izin**\n__Gunakan /revoke untuk mencabut izin.__\n__Beri aku url agar dapat memproses ke Drive kamu__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Yeeeyyy berhasil meng otentikasi.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__Yah kode mu salah nih, coba periksa lagi ya__'
    
    AUTH_TEXT = "⛓️ **Untuk Mengotorisasi akun Google Drive Anda, kunjungi [URL]({}) ini dan kirim kode yang dihasilkan di sini.**\n__Kunjungi URL > Izinkan izin > Anda akan mendapatkan kode > salin > Kirim di sini__"
    
    DOWNLOAD_TG_FILE = "📥 **Mengunduh File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder selesai di atur.**\n__ID folder kamu - {}\nUse__ ```/{} clear``` __Untuk  menghapus.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder berhasil dibuat.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **Your Current Custom Folder ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **Log out berhasil.**\n__Use /{BotCommands.Authorize[0]} Untuk mengizinkan ulang bot.__"
    
    NOT_FOLDER_LINK = "❗ **Ups url folder nya salah.**\n__Url yang kamu kirim tidak dapat ditemukan.__"
    
    CLONING = "🗂️ **Menggadakan google drive**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **Maaf, kamu tidak memilikin untuk mengakses file ini**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File Deleted Successfully.**\n__File deleted permanently !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"
    
    EMPTY_TRASH = "🗑️🚮**Trash Emptied Successfully !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
