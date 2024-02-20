import unreal

accepted_classes = []
exclude_folders = []
combo_box = unreal.ComboBoxString()

def FillCombo(combo_box, accepted_classes, exclude_folders):

    assetReg = unreal.AssetRegistryHelpers.get_asset_registry()
    allAssetsData = assetReg.get_assets_by_path("/Game/", True)
    for asset in allAssetsData:
        assetString = unreal.AssetRegistryHelpers.get_full_name(asset)
        assetClassStartPos = assetString.index('.') + 1
        assetClassEndPos = assetString.index(' ')
        assetNameStartPos = assetString.index('.', assetClassEndPos + 1) + 1
        if assetString[assetClassStartPos : assetClassEndPos] in accepted_classes:
            for folderName in exclude_folders:
                if "/" + folderName + "/" not in assetString:
                    combo_box.add_option(assetString[assetNameStartPos : ])
