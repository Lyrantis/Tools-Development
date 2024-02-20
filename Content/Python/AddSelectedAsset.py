import unreal

accepted_classes = []
asset_grid = unreal.UniformGridPanel()
grid_node = unreal.GridNode()

def AddAsset(asset_grid, accepted_classes):

    selectedAssets = unreal.EditorUtilityLibrary.get_selected_assets()
    asset_subsystem = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)
    asset_subsystem.open_editor_for_assets(selectedAssets)
    #selectedAssetString = ''.join(str(i) for i in selectedAssets)
    #selectedAssetStringSplit = selectedAssetString.split(",")

    #for i in range(2, len(selectedAssetStringSplit), 4):
    #    classNameStartPos = selectedAssetStringSplit[i + 2].index('"') + 1
     #   classNameEndPos = selectedAssetStringSplit[i + 2].index('"', classNameStartPos)
      #  if selectedAssetStringSplit[i + 2][classNameStartPos : classNameEndPos] in accepted_classes:
       #     assetNameStartPos = selectedAssetStringSplit[i].index('"') + 1
        #    assetNameEndPos = selectedAssetStringSplit[i].index('"', classNameStartPos)
         #   grid_node.UpdateInformation(selectedAssetStringSplit[i][assetNameStartPos : assetNameEndPos], selectedAssetStringSplit[i + 2][classNameStartPos : classNameEndPos], selectedAssetStringSplit[i + 1])
          #  asset_grid.add_child_to_uniform_grid(grid_node)
            
