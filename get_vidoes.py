# import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

config ={
    "apiKey": "AIzaSyDL0Bw65Q-aAqR1D9i_Ce-oxZqNHZDOQ0U",
  "authDomain": "ad-venture-72ea9.firebaseapp.com",
  "projectId": "ad-venture-72ea9",
  "storageBucket": "ad-venture-72ea9.appspot.com",
  "messagingSenderId": "440230710576",
  "appId": "1:440230710576:web:eed72dffe985e4f4f58cf5",
  "measurementId": "G-6QL5PC9XHF"
}




cred = credentials.Certificate('cred/account.json')


# Get a reference to the default Firebase Storage bucket
firebase_admin.initialize_app(cred, {
    'storageBucket': 'ad-venture-72ea9.appspot.com'
})

bucket = storage.bucket()



# Upload a file
def upload_file(file_path, destination_path):
    blob = bucket.blob(destination_path)
    blob.upload_from_filename(file_path)
    print('File uploaded successfully.')

# Download a file
def download_file(source_path, destination_path):
    blob = bucket.blob(source_path)
    blob.download_to_filename(destination_path)
    print('File downloaded successfully.')

# Delete a file
def delete_file(file_path):
    blob = bucket.blob(file_path)
    blob.delete()
    print('File deleted successfully.')

# List files in a directory
def list_files(directory_path):
    blobs = bucket.list_blobs(prefix=directory_path)
    for blob in blobs:
        print(blob.name)

# Example usage
file_link = input("Enter file : ")
category = input("Enter cat [ad / vidoe]: ")
file_name = file_link.split('/')[-1]
upload_file( file_link, f'{category}/{file_name}')
# download_file('images/file.jpg', 'path/to/local/downloaded_file.jpg')
# delete_file('images/file.jpg')
# list_files('images/')

# print(file_name)

