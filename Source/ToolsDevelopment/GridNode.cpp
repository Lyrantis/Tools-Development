#include "GridNode.h"
#include "Components//Button.h"
#include "Components/TextBlock.h"
#include "Components/Image.h"

void UGridNode::NativeConstruct()
{
	Super::NativeConstruct();

	if (AssetName)
	{
		AssetName->SetText(FText::FromString("ASSET NAME"));
	}
	
}

void UGridNode::UpdateItem(FString newName, FString filePath, FString newClass)
{
	AssetName->SetText(FText::FromString(newName));
	assetFilePath = filePath;
	assetClass = newClass;	//Set Image Based On Class
}
