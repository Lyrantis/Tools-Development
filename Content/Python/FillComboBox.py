import unreal

accepted_classes = []
combo_box = unreal.ComboBoxString()

def FillCombo(combo_box, accepted_classes):

    assetReg = unreal.AssetRegistryHelpers.get_asset_registry()
    allAssets = assetReg.get_assets_by_path("/Game/", True)
    allAssetString = ''.join(str(i) for i in allAssets)
    allAssetStringSplit = allAssetString.split(",")

    for i in range(2, len(allAssetStringSplit), 4):
        classNameStartPos = allAssetStringSplit[i + 2].index('"') + 1
        classNameEndPos = allAssetStringSplit[i + 2].index('"', classNameStartPos)
        if allAssetStringSplit[i + 2][classNameStartPos : classNameEndPos] in accepted_classes:
            assetNameStartPos = allAssetStringSplit[i].index('"') + 1
            assetNameEndPos = allAssetStringSplit[i].index('"', classNameStartPos)
            combo_box.add_option(allAssetStringSplit[i][assetNameStartPos : assetNameEndPos])
    unreal.AssetToolsHelpers.get_asset_tools().open_editor_for_assets(unreal.load_asset('/Game/Folder/Spaff'))
