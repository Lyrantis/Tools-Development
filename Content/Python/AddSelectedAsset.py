import unreal

accepted_classes = []
asset_data = []

def AddAsset(accepted_classes) -> str:

    selectedAssets = unreal.EditorUtilityLibrary.get_selected_assets()

    for asset in selectedAssets:
        asset = str(asset)
        unreal.log(asset)
        filePathStartPos = asset.index('/')
        filePathEndPos = asset.index(' ', filePathStartPos + 1) - 1
        assetFilePath = asset[filePathStartPos : filePathEndPos]
        assetName = assetFilePath
        assetName = assetName[assetName.find('.') + 1 : ]
        assetClassStartPos = asset.index('Class') + 7
        assetClassEndPos = asset.index('>', assetClassStartPos) - 1
        assetClass = asset[assetClassStartPos : assetClassEndPos]
        if assetClass in accepted_classes:
            asset_data.append(assetName)
            asset_data.append(assetClass)
            asset_data.append(assetFilePath)
    return asset_data


