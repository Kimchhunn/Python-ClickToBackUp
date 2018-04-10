import os
import zipfile
import shutil

# copy files and folder and compress into a zip file
# def doprocess(source_folder, target_zip):
#     zipf = zipfile.ZipFile(target_zip, "w")
#     for subdir, dirs, files in os.walk(source_folder):
#         for file in files:
#             print os.path.join(subdir, file)
#             zipf.write(os.path.join(subdir, file))
#
#     print "Created ", target_zip
#
# #copy files to a target folder
# def docopy(source_folder, target_folder):
#     for subdir, dirs, files in os.walk(source_folder):
#         for file in files:
#             print os.path.join(subdir, file)
#             shutil.copy2(os.path.join(subdir, file), target_folder)


if __name__ == '__main__':

    src_path = 'C:\Users\GM\Documents\Rockstar Games\GTA V\Profiles\A044D82B'
    trg_path = 'D:\Entertainment\Rockstar Games\BackupGameSaved\Rockstar Games\GTA V\Profiles\A044D82B'

    print("File is being backed up.....")
    for root, dirs, files in os.walk(src_path, topdown=False):
        for file in files:
            print("#")
            with open('{}\{}'.format(src_path, file), 'rb') as text:
                aa = text.read()
            with open('{}\{}'.format(trg_path, file), 'wb') as f:
                f.write(aa)

            f.close()
            text.close()

    print("File is backed up.")

        # with open('C:\Users\GM\Documents\Rockstar Games\GTA V\Profiles\A044D82B\{}.bak'.format("SGTA50000"), 'wb') as output:
        #     print(output)

        # output.close()
        # for name in files:
        #     print(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))

    # print("Backup execution is starting")
    #
    # #zip the file
    # src_folder = "C:\Users\GM\Documents\Rockstar Games\GTA V\Profiles\A044D82B"
    # trg_folder = "D:\Entertainment"
    # doprocess(src_folder, trg_folder)
    #
    # # copy to backup folder
    # source_folder = 'C:\Users\GM\Documents\Rockstar Games\GTA V\Profiles\A044D82B'
    # target_folder = 'D:\Entertainment'
    # docopy(source_folder, target_folder)
    #
    # print 'Ending execution'


