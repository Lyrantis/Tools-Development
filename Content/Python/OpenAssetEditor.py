import unreal

def OpenEditor(assetPath):
    if (assetPath == ''):
        unreal.EditorDialog.show_message("Failed To Open Editor", "No Asset Selected", unreal.AppMsgType.OK)
    else:
        assetToOpen = unreal.EditorAssetLibrary.find_asset_data(assetPath)
        asset_subsystem = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)
        asset_subsystem.open_editor_for_assets([assetToOpen.get_asset()])