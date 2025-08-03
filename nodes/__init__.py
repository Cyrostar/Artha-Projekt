ncm = {}
ndm = {}

from .prj.project import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

for k, v in NODE_CLASS_MAPPINGS.items():
    
    ncm[k] = v
    
for k, v in NODE_DISPLAY_NAME_MAPPINGS.items():
    
    ndm[k] = v
       
#################################################

NODE_CLASS_MAPPINGS = ncm
NODE_DISPLAY_NAME_MAPPINGS = ndm