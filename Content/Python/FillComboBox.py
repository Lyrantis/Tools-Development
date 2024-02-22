import unreal

accepted_classes = []
exclude_folders = []
combo_box = unreal.ComboBoxString()
file_paths = []

def FillCombo(combo_box, accepted_classes, exclude_folders) -> list[str]:

    assetReg = unreal.AssetRegistryHelpers.get_asset_registry()
    allAssetsData = assetReg.get_assets_by_path("/Game/", True)
    for asset in allAssetsData:
        assetString = unreal.AssetRegistryHelpers.get_full_name(asset)
        filepathStartPos = assetString.index(' ') + 1
        filepathEndPos = assetString.index('.', filepathStartPos)
        filepath = assetString[filepathStartPos : filepathEndPos]
        assetClassStartPos = assetString.index('.') + 1
        assetClassEndPos = assetString.index(' ')
        assetNameStartPos = assetString.index('.', assetClassEndPos + 1) + 1
        unreal.log(assetString[assetNameStartPos : ] + " - " + assetString[assetClassStartPos : assetClassEndPos])
        if assetString[assetClassStartPos : assetClassEndPos] in accepted_classes:
            for folderName in exclude_folders:
                if "/" + folderName + "/" not in assetString:
                    combo_box.add_option(assetString[assetNameStartPos : ])
                    file_paths.append(filepath)
    return file_paths
