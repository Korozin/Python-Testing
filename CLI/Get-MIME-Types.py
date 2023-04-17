import mimetypes

def get_mime_type(filename):
    mime_type, _ = mimetypes.guess_type(filename)
    return mime_type

filename = input("Enter the filename: ")
mime_type = get_mime_type(filename)

if mime_type is None:
    print("Unknown MIME type")
else:
    print("MIME type:", mime_type)
