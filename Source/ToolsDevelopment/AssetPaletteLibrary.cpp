// Fill out your copyright notice in the Description page of Project Settings.


#include "AssetPaletteLibrary.h"
#include "Components/Button.h"
#include "Components/UniformGridSlot.h"
#include "Components/UniformGridPanel.h"


bool UAssetPaletteLibrary::ToggleEditButtonColour(UButton* editButton, bool editMode)
{
	if (editMode)
	{
		editButton->SetColorAndOpacity(FLinearColor(120, 120, 120));
	}
	else
	{
		editButton->SetColorAndOpacity(FLinearColor(255, 255, 255));
	}
	return !editMode;
}

void UAssetPaletteLibrary::MoveNodeInGrid(UUniformGridSlot* nodeToMove, UUniformGridPanel* grid, EDirection directionToMove)
{
	int nodeRow = nodeToMove->GetRow();
	int nodeColumn = nodeToMove->GetColumn();
	
	switch (directionToMove)
	{
	case EDirection::UP:
		if (nodeRow > 0)
		{
			TArray<UWidget*> nodes = grid->GetAllChildren();
			for (UWidget* Node : nodes)
			{
				UUniformGridSlot nodeSlot = Node->Slot;
				if (Node.)
			}
			nodeToMove->SetRow(nodeRow - 1);
		}
		break;
	case EDirection::DOWN:
		nodeToMove->SetRow(nodeRow + 1);
		break;
	case EDirection::LEFT:
		if (nodeColumn > 0)
		{
			nodeToMove->SetColumn(nodeColumn - 1);
		}
		break;
	case EDirection::RIGHT:
		nodeToMove->SetColumn(nodeColumn + 1);
		break;
	}
}
