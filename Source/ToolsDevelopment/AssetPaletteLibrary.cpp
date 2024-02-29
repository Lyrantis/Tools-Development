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

void UAssetPaletteLibrary::MoveNodeInGrid(UUniformGridSlot* nodeToMove, TMap<UUserWidget*, UUniformGridSlot*> nodeSlots, EDirection directionToMove)
{
	int nodeRow = nodeToMove->GetRow();
	int nodeColumn = nodeToMove->GetColumn();
	
	switch (directionToMove)
	{
	case EDirection::UP:
		if (nodeRow > 0)
		{
			for (TPair<UUserWidget*, UUniformGridSlot*> pair : nodeSlots)
			{
				if (pair.Value->GetColumn() == nodeColumn && pair.Value->GetRow() == nodeRow - 1)
				{
					pair.Value->SetRow(nodeRow);
				}
			}
			nodeToMove->SetRow(nodeRow - 1);
		}
		break;
	case EDirection::DOWN:
		for (TPair<UUserWidget*, UUniformGridSlot*> pair : nodeSlots)
		{
			if (pair.Value->GetColumn() == nodeColumn && pair.Value->GetRow() == nodeRow + 1)
			{
				pair.Value->SetRow(nodeRow);
			}
		}
		nodeToMove->SetRow(nodeRow + 1);
		break;
	case EDirection::LEFT:
		if (nodeColumn > 0)
		{
			for (TPair<UUserWidget*, UUniformGridSlot*> pair : nodeSlots)
			{
				if (pair.Value->GetColumn() == nodeColumn - 1 && pair.Value->GetRow() == nodeRow)
				{
					pair.Value->SetColumn(nodeColumn);
				}
			}
			nodeToMove->SetColumn(nodeColumn - 1);
		}
		break;
	case EDirection::RIGHT:
		for (TPair<UUserWidget*, UUniformGridSlot*> pair : nodeSlots)
		{
			if (pair.Value->GetColumn() == nodeColumn + 1 && pair.Value->GetRow() == nodeRow)
			{
				pair.Value->SetColumn(nodeColumn);
			}
		}
		nodeToMove->SetColumn(nodeColumn + 1);
		break;
	}
}

void UAssetPaletteLibrary::AddNodeToGrid(UUserWidget* nodeToAdd, UUniformGridPanel* grid, TMap<UUserWidget*, UUniformGridSlot*> slotsTaken)
{
	int slotsNum = slotsTaken.Num();
	if (slotsNum == 0)
		slotsTaken.FindOrAdd(nodeToAdd, grid->AddChildToUniformGrid(nodeToAdd, 0, 0));
		
	for (int i = 0; i < slotsNum; ++i)
	{
		int row = i / 8;
		int col = i % 8;

		bool flag = false;
		for (TPair<UUserWidget*, UUniformGridSlot*> pair : slotsTaken)
		{
			if (pair.Value->GetRow() == row && pair.Value->GetColumn() == col)
			{
				flag = true;
			}
		}
		if (!flag)
		{
			slotsTaken.Add(nodeToAdd, grid->AddChildToUniformGrid(nodeToAdd, row, col));
			break;
		}
	}
}
