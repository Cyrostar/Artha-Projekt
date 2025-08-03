from datetime import datetime
from ...core.node import node_prefix, main_cetegory
from ...core.helpers import filename_format
import folder_paths

ARTHA_PROJECT_SHARED_DICT = {}

class ProjectSetup:
    
    CATEGORY = main_cetegory() + "/PRJ"
    
    @classmethod
    def INPUT_TYPES(cls):
        
        return {
            "required": {
                "project_name": ("STRING", {"default": "Youtube"}),
                "project_category": ("STRING", {"default": "Shorts", "placeholder": "Leave empty if not needed"}),
                "project_type": ("STRING", {"default": "Fun", "placeholder": "Leave empty if not needed"}),               
            },
        }
          
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("project_folder",)
    FUNCTION = "artha_main"
    
    @classmethod
    def IS_CHANGED(cls, project_name, project_category, project_type, **kwargs):
    
        ARTHA_PROJECT_SHARED_DICT['project_name'] = project_name
        ARTHA_PROJECT_SHARED_DICT['project_category'] = project_category
        ARTHA_PROJECT_SHARED_DICT['project_type'] = project_type

        return float("nan")
    
    def artha_main(self, project_name, project_category, project_type, **kwargs):
        
        project_folder = ""
        
        output_dir = folder_paths.get_output_directory()
        
        project_folder = project_folder + output_dir + "\\"
        
        if(project_name):
            
            project_folder = project_folder + filename_format(project_name) + "\\"
            
        if(project_category):
            
            project_folder = project_folder + filename_format(project_category) + "\\"

        if(project_type):
            
            project_folder = project_folder + filename_format(project_type) + "\\"
        
        return (project_folder,)
        
    
class ProjectPrefix:
    
    CATEGORY = main_cetegory() + "/PRJ"
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {

                "file_title": ("STRING", {"default": "Artha", "placeholder": "Leave empty if not needed"}),
                "file_model": ("STRING", {"default": "Flux", "placeholder": "Leave empty if not needed"}),
                "file_media": (["image", "video", "none"], {"default": "image"}),
                "file_seed": ("INT", {"default": 42, "min": 0, "max": 0xffffffffffffffff}),
            }
        }
          
    RETURN_TYPES = ("STRING","INT","STRING")
    RETURN_NAMES = ("prefix","seed","datetime")
    FUNCTION = "artha_main"
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):  

        return float("nan")
       
    def artha_main(self, file_title, file_model, file_media, file_seed):
        
        prefix = ""
              
        project_name = ARTHA_PROJECT_SHARED_DICT.get('project_name')
        project_category = ARTHA_PROJECT_SHARED_DICT.get('project_category')
        project_type = ARTHA_PROJECT_SHARED_DICT.get('project_type')
              
        now = datetime.now()
        now = now.strftime("%Y-%m-%d-%H-%M-%S")
        
        if(project_name):
            prefix = prefix + filename_format(project_name) + "/"
            
        if(project_category):
            prefix = prefix + filename_format(project_category) + "/"
            
        if(project_type):
            prefix = prefix + filename_format(project_type) + "/"
            
        if(file_title):
            prefix = prefix + filename_format(file_title) + "-"
            
        prefix = prefix + "DATE-" + str(now) + "-SEED-" + str(file_seed)
        
        if(file_model):
            prefix = prefix + "-MODEL-" + filename_format(file_model)
            
        if(file_media == "image"):
            prefix = prefix + "-IMG"
            
        if(file_media == "video"):
            prefix = prefix + "-VID"
            
        if(file_media == "none"):
            prefix = prefix + "-"
            
        return (prefix, file_seed, now)
        
class ProjectSeed:
    
    CATEGORY = main_cetegory() + "/PRJ"
    
    def __init__(self):

        self.seed_dict = {}

    @classmethod
    def INPUT_TYPES(cls):
             
        return {
            "required": {
                "seed": ("INT", {"default": 42, "min": 0, "max": 0xffffffffffffffff}),
            }
        }
                 
    @classmethod
    def IS_CHANGED(cls, **kwargs):

        return float("nan") 
          
    RETURN_TYPES = ("INT","STRING")
    RETURN_NAMES = ("seed","history")
    FUNCTION = "artha_main"
       
    def artha_main(self, seed):
        
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        
        self.seed_dict[now] = seed
        
        history = ""
        
        for key, value in self.seed_dict.items():
            
            history += "TIME " + str(key) + " SEED " + str(value) + "\n"
 
        return (seed,history,)

NODE_CLASS_MAPPINGS = {
    "Project Setup": ProjectSetup,
    "Project Prefix": ProjectPrefix,
    "Project Seed": ProjectSeed,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Project Setup": node_prefix() + " PROJECT SETUP",
    "Project Prefix": node_prefix() + " PROJECT PREFIX",
    "Project Seed": node_prefix() + " PROJECT SEED",
}