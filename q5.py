from google.cloud import storage

gs = storage.Client()
src_bkt = gs.get_bucket("av-a1-q5-src")
dest_bkt = gs.get_bucket("av-a1-q5-dest")


#copy
src_blob = src_bkt.blob("gcp-1.png")
dest_blob = src_bkt.copy_blob(src_blob, dest_bkt, "gcp-1-copy.png")

print()
print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(src_blob.name, src_bkt.name, dest_blob.name, dest_bkt.name))
print()


#move

# ..copy to destination
dest_blob = src_bkt.copy_blob(src_blob, dest_bkt, "gcp-1-mv.png")
print("..copied")

# ..delete from source
src_blob.delete()
print("..deleted")

print('Blob {} in bucket {} moved to blob {} in bucket {}.'.format(src_blob.name, src_bkt.name, dest_blob.name, dest_bkt.name))
print()


#upload
blob = src_bkt.blob("img.png")
with open("/home/avinash/Pictures/img.png", "rb") as f:
    blob.upload_from_file(f)
print('File {} uploaded to {}.'.format("img.png", src_bkt.name + "/img.png"))
print()


#download
blob = src_bkt.blob("img.png")
blob.download_to_filename("/home/avinash/Pictures/img-dl.png")

print('Blob {} downloaded to {}.'.format("img.png", "/home/avinash/Pictures/img-dl.png"))
print()


#delete
blob = src_bkt.blob("img.png")
blob.delete()
print('Blob {} deleted.'.format("img.png"))
