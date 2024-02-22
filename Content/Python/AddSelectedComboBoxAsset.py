import unreal

asset_data = []

def AddAsset(assetName, assetFilePath):
    assetData = unreal.EditorAssetLibrary.find_asset_data(assetFilePath)
    asset = str(assetData)
    unreal.log(asset)
    assetClassStartPos = asset.index('asset_class_path')
    assetClassStartPos = asset.index('asset_name', assetClassStartPos) + 13
    assetClassEndPos = asset.index('"', assetClassStartPos)
    assetClass = asset[assetClassStartPos : assetClassEndPos]
    asset_data.append(assetName)
    asset_data.append(assetClass)
    asset_data.append(assetFilePath)
    return asset_data