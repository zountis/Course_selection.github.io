from conf import settings
import os
import pickle

def save(obj):
    user_dir=os.path.join(settings.DATA_PATH,obj.__class__.__name__)
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    user_path=os.path.join(user_dir,obj.name)
    with open(user_path,'wb') as f:
        pickle.dump(obj,f)

def select(cls,username):
    user_dir=os.path.join(settings.DATA_PATH,cls.__name__)
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    user_path=os.path.join(user_dir,username)
    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            obj=pickle.load(f)
            return obj