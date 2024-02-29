import unreal

accepted_classes = []
exclude_folders = []
combo_box = unreal.ComboBoxString()
file_paths = []

def FillCombo(combo_box, excluded_folders, excluded_classes, excluded_names) -> list[str]:

    assetReg = unreal.AssetRegistryHelpers.get_asset_registry()
    allAssetsData = assetReg.get_assets_by_path("/Game/", True)
    for asset in allAssetsData:
        assetString = unreal.AssetRegistryHelpers.get_full_name(asset)
        filepathStartPos = assetString.index(' ') + 1
        filepathEndPos = assetString.index('.', filepathStartPos)
        filepath = assetString[filepathStartPos : filepathEndPos]
        assetClassStartPos = assetString.index('.') + 1
        assetClassEndPos = assetString.index(' ')
        assetClass = assetString[assetClassStartPos : assetClassEndPos]
        assetName = assetString[assetString.index('.', assetClassEndPos + 1) + 1 : ]
        flag = False

        for folderName in excluded_folders:
            if "/" + folderName + "/"  in filepath:
                flag = True

        if not flag:
            for classFilter in excluded_classes:
                if classFilter in assetClass:
                    flag = True

        if not flag:
            for nameFilter in excluded_names:
                if nameFilter  in assetName:
                    flag = True
                    
        if not flag:
            combo_box.add_option(assetName)
            file_paths.append(filepath)

    return file_paths
