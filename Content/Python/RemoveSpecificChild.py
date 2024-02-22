import unreal

def RemoveChild(assetGrid, childToRemove):
    if assetGrid.has_child(childToRemove):
        assetGrid.remove_child(childToRemove)