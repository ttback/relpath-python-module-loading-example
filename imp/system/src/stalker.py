def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
 
load_src("meme", "../../service/src/meme.py")
import meme
load_src("config", "./config.py")
import config