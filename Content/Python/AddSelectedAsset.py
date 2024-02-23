import unreal

accepted_classes = []
asset_data = []

def AddAsset(excluded_classes) -> list[str]:

    selectedAssets = unreal.EditorUtilityLibrary.get_selected_assets()

    for asset in selectedAssets:
        asset = str(asset)
        filePathStartPos = asset.index('/')
        filePathEndPos = asset.index(' ', filePathStartPos + 1) - 1
        assetFilePath = asset[filePathStartPos : filePathEndPos]
        assetName = assetFilePath
        assetName = assetName[assetName.find('.') + 1 : ]
        assetClassStartPos = asset.index('Class') + 7
        assetClassEndPos = asset.index('>', assetClassStartPos) - 1
        assetClass = asset[assetClassStartPos : assetClassEndPos]
        flag = False
        for classFilter in excluded_classes:
            if classFilter in assetClass:
                flag = True
        
        if not flag:
            asset_data.append(assetName)
            asset_data.append(assetClass)
            asset_data.append(assetFilePath) 
    return asset_data


