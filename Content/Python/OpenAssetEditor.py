import unreal

def OpenEditor(assetPath):
    assetToOpen = unreal.EditorAssetLibrary.find_asset_data(assetPath)
    asset_subsystem = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)
    asset_subsystem.open_editor_for_assets([assetToOpen.get_asset()])