import sys
import subprocess

def file_download(gid, filename):
    # Install GoogleDriveDownloader to download file from Google Drive
    subprocess.call("pip install googledrivedownloader", shell=True)
    
    # Import necessary package
    from google_drive_downloader import GoogleDriveDownloader as gdd
    
    # Download file
    savepath = "./" + filename
    gdd.download_file_from_google_drive(file_id=gid, dest_path=savepath, unzip=False)

# Main function
def main():   
    # Get id and filename
    if sys.argv[1] == "short":
        gid = '1jxRWFcxBBjQk0v3BHh-obfSjYeunmjJZ'
        filename = "final_short.mp4"
    elif sys.argv[1] == "long":
        gid = '1f8PO1-CLHWBGUC5TcWsCpG6K8amXM0e7'
        filename = "final_long.mp4"
    else:
        print("Wrong argument. Please specify the file to be download")

    # Call function to download
    print("Download the final output video: " + filename)
    file_download(gid, filename)
    print("--------- Download completed -----------")

if __name__ == "__main__":
    main()