import unreal

def spawn_asset(assetFilePath, assetClass, location = unreal.Vector(), rotation = unreal.Rotator()):
    
    # Get the system to control the actors
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    # We want to create a StaticMeshActor

    if assetClass == static_mesh:
    
        # Place it in the level
        static_mesh_actor = editor_actor_subs.spawn_actor_from_class(assetClass, location, rotation)

        # Load and add the cube to it
        static_mesh = unreal.EditorAssetLibrary.load_asset(assetFilePath)
        static_mesh_actor.static_mesh_component.set_static_mesh(static_mesh)
    else:
        # Failed
    

    

def run():
    spawn_asset()

run()