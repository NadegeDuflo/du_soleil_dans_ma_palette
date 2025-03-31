from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import random

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


def antispam():
    spam_questions = (('La nuit, tous les chats sont ', 'gris'), ('Un zèbre est noir et ', 'blanc'), ('La couleur du coquelicot est ', 'rouge')) 
    i = random.randint(0, len(spam_questions)-1)
    spam_question  = spam_questions[i][0]
    spam_response = spam_questions[i][1]
    return (spam_question, spam_response )