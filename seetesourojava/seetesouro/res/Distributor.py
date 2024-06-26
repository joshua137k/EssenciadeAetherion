import os
import re

def add_ids_to_png_files(base_paths):
    current_id = 0
    id_pattern = re.compile(r'^\d+_')
    log_lines = []

    for base_path in base_paths:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.endswith('.png'):
                    path = root.replace("\\","/") +"/" + file
                    if id_pattern.match(file):
                        print(f"Ignorado (já tem ID): {file}")
                        capitalized_file_name,_ = os.path.splitext(file)
                        capitalized_file_name = capitalized_file_name.split("_")
                        
                        capitalized_file_name = capitalized_file_name[1].capitalize()
                        

                        log_lines.append((capitalized_file_name,path))
                        continue
                    file_name, file_ext = os.path.splitext(file)
                    capitalized_file_name = file_name.capitalize()
                    
                    
                    new_file_name = f"{current_id}_{file_name}{file_ext}"
                    old_file_path = os.path.join(root, file)
                    new_file_path = os.path.join(root, new_file_name)
                    
                    
                    os.rename(old_file_path, new_file_path)
                    print(f"Renomeado: {old_file_path} -> {new_file_path}")
                    log_lines.append((capitalized_file_name,path))

                    
                    current_id += 1
    return log_lines

def create_a_new_Enum_UID(log_lines):
    file = "src/com/data/UID.java"
    f = open(file,"w")
    f.write("package com.data;\n\n")
    f.write("public enum UID {\n\n")
    #SET UID
    #-----
    '''
    GRASS("/path/to/grass.png"),
    SAND("/path/to/sand.png");
    '''
    enums = ""
    for name,path in log_lines:
        enums += f'    {name}("{path}"),\n'

    enums = enums[:-2]+";\n\n"
    f.write(enums)


    #----
    f.write("    private final String path;\n\n")
    f.write("    UID(String path) {\n")
    f.write("        this.path = path;\n")
    f.write("    }\n\n")
    f.write("    public String getPath() {\n")
    f.write("        return path;\n")
    f.write("    }\n\n")
    f.write("}")
    f.close()


def create_a_new_Suplier(log_lines):
    file = "src/com/data/Suplier.java"
    f = open(file,"w")
    start = """
package com.data;

import com.object.SuperObject;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Supplier;


public class Suplier {

    public Map<UID, Supplier<SuperObject>> objectSuppliers;

    public Suplier(){
        objectSuppliers = new HashMap<>();
"""
    end = """
    }
                
}
"""


    f.write(start)

    #SET OBJ
    #----
    #objectSuppliers.put(UID.Boot, OBJ_Boot::new);
    objs = ""
    for name,path in log_lines:
        if ("opened" not  in name) and ("tiles" not in path):
            f.write(f"        objectSuppliers.put(UID.{name}, OBJ_{name}::new);\n")
        #print(path)
    #----
    f.write(end)
    f.close



base_paths = ["res/objects", "res/tiles"]

log_lines = add_ids_to_png_files(base_paths)
create_a_new_Enum_UID(log_lines)
create_a_new_Suplier(log_lines)