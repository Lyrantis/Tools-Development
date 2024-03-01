// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/UniformGridPanel.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "AssetPaletteLibrary.generated.h"

class UButton;
class UUserWidget;
class UUniformGridSlot;
class UUniformGridPanel;

UENUM(BlueprintType)
enum class EDirection : uint8
{
	UP,
	DOWN,
	LEFT,
	RIGHT
};
UCLASS()
class TOOLSDEVELOPMENT_API UAssetPaletteLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

public:
	 
	UFUNCTION(BlueprintCallable)
	static bool ToggleEditButtonColour(UButton* editButton, bool editMode);

	UFUNCTION(BlueprintCallable)
	static void MoveNodeInGrid(UUniformGridSlot* nodeToMove, TMap<UUserWidget*, UUniformGridSlot*> nodeSlots, EDirection directionToMove);

	UFUNCTION(BlueprintCallable)
	static UUniformGridSlot* AddNodeToGrid(UUserWidget* nodeToAdd, UUniformGridPanel* grid, TMap<UUserWidget*, UUniformGridSlot*> slotsTaken);

	UFUNCTION(BlueprintCallable)
	static TArray<int> FindNextAvailableGridLocation(TMap<UUserWidget*, UUniformGridSlot*> slotsTaken);
};
