import unreal

def rename_assets(searchPrefix, replacePrifix):
    systemLib = unreal.SystemLibrary()
    edUtil = unreal.EditorUtilityLibrary()
    stringLib = unreal.StringLibrary()
    

    selectedAssets = edUtil.get_selected_assets()
    numAssets = len(selectedAssets)
    replaced = 0

    unreal.log("Selected {} assets".format(numAssets))

    for asset in selectedAssets:
        assetName = systemLib.get_object_name(asset)

        # unreal.log(asset)
        # very simple rename to run on newly created asset that starts "New"
        # replaces with "BP_". Can be changed to deterine the type of asset 
        # & replace with correct prefix
        if stringLib.contains(assetName, searchPrefix, use_case=False):
            replacedName = stringLib.replace(assetName, searchPrefix, replacePrifix)
            edUtil.rename_asset(asset, replacedName)
           
            replaced += 1
            unreal.log("Replaced {} with {}".format(assetName, replacedName))

        else:
            unreal.log("{} was fine.".format(assetName))
           

    unreal.log("Replaced {} of {} assets".format(replaced, numAssets))




rename_assets("New", "BP_")

