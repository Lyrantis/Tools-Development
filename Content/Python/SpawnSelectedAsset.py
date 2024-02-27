import unreal 

def SpawnAsset(asset_path):
    obj = unreal.load_asset(asset_path)

    camera_info = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_level_viewport_camera_info()
    unreal.EditorLevelLibrary().spawn_actor_from_object(obj, camera_info[0] + (camera_info[1].get_forward_vector() * 1000))
