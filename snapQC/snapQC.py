import nuke
import os
import string

def snapQC():
    viewer = nuke.activeViewer()
    viewer_node = viewer.node()
    
    active_input_index = viewer.activeInput()
    
    active_input_node = viewer_node.input(active_input_index)
    
    write_node = nuke.createNode("Write", inpanel=False)
    write_node.setInput(0, active_input_node)
    
    if active_input_node:
        top_node = active_input_node
        while top_node.input(0):
            top_node = top_node.input(0)
    
    if top_node.Class() == 'Read':
        shot_path = top_node['file'].getValue()
    
        clean_path = shot_path
        for token in ['%', '#']:
            if token in clean_path:
                clean_path = clean_path.split(token)[0]
        if '.' in os.path.basename(clean_path):
            clean_path = os.path.splitext(clean_path)[0]
        shot_name = os.path.basename(clean_path)
    
    script_path = nuke.root().name()
    frame = nuke.frame()
    script_dir = os.path.dirname(script_path)
    Qc_dir = os.path.join(script_dir, "feedback").replace("\\", "/")
    if not os.path.exists(Qc_dir):
        os.makedirs(Qc_dir)
    
    for suffix in string.ascii_uppercase:
        filename = "{}_frame{}_{}.jpg".format(shot_name, frame, suffix)
        full_path = os.path.join(Qc_dir, filename)
        if not os.path.exists(full_path):
            break
    else:
        raise RuntimeError("Limit exceeded")
    
    fullpath = os.path.join(Qc_dir, filename).replace("\\", "/")
    
    write_node['file_type'].setValue('jpg')
    write_node['file'].setValue(fullpath)
    write_node['use_limit'].setValue(True)
    write_node["_jpeg_quality"].setValue(0.5)
    write_node['first'].setValue(frame)
    write_node['last'].setValue(frame)
    
    nuke.execute(write_node, frame, frame)
    nuke.tprint("Saved at " + Qc_dir)
    nuke.delete(write_node)
