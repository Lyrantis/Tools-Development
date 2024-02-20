import unreal

def OpenAssetEditor():
    selectedAssets = unreal.EditorUtilityLibrary.get_selected_assets()
    asset_subsystem = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)
    asset_subsystem.open_editor_for_assets(selectedAssets)