import unreal

def OpenEditor(assetPath):
    assetToOpen = unreal.AssetRegistry.get_asset_by_object_path(assetPath)
    asset_subsystem = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)
    asset_subsystem.open_editor_for_asset(assetToOpen)