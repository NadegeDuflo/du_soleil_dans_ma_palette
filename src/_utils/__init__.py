from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

def has_changed(instance, field, manager='objects'):
        """Returns true if a field has changed in a model

        May be used in a model.save() method.

        """
        print(instance)
        print(field)
        if not instance.pk:
            return True
        manager = getattr(instance.__class__, manager)
        print(manager)
        
        old = getattr(manager.get(pk=instance.pk), field)
        print(old)
        print(not getattr(instance, field) == old)
        return not getattr(instance, field) == old
    
    
def resize_img(image, size):
    """Returns the image resized to fit inside a box of the given size"""
    image.thumbnail(size)
    temp = BytesIO()
    image.save(temp, 'jpeg')
    temp.seek(0)
    return SimpleUploadedFile('temp', temp.read())