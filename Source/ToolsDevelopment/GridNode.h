#pragma once

#include "CoreMinimal.h"
#include "Blueprint/UserWidget.h"
#include "GridNode.generated.h"

class UButton;
class UTextBlock;
class UImage;

UCLASS()
class TOOLSDEVELOPMENT_API UGridNode : public UUserWidget
{
	GENERATED_BODY()

public:

	virtual void NativeConstruct() override;
	void UpdateItem(FString newName, FString filePath, FString newClass);
	
private:

	UPROPERTY(meta = (BindWidget))
	TObjectPtr<UButton> ActionButton;

	UPROPERTY(meta = (BindWidget))
	TObjectPtr<UTextBlock> AssetName;

	UPROPERTY(meta = (BindWidget))
	TObjectPtr<UImage> AssetImage;

	FString assetClass;
	FString assetFilePath;
};
