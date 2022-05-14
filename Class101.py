import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BHkTGhOM1tod4zmk73dYQNiAldD7NQb_wAit0drDMaZl4eYwW1Opto5E3YCJd9wSTlWYj8LnkfBB2qKin7kjfZbw0dQGUdInByiEHaYLIwRosWgZTF0y-F1OjRQt1palej_piAs'
    transferData = TransferData(access_token)

    file_from = input("What file? ")
    file_to  = input("To where? ")

    transferData.upload_file(file_from, file_to)

    print("File has been moved successfully.")

main()