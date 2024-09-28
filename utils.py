# Check if the file extension is allowed
def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'dicom', 'dcm'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
