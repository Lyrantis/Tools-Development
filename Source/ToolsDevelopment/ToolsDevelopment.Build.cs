// Copyright Epic Games, Inc. All Rights Reserved.

using UnrealBuildTool;

public class ToolsDevelopment : ModuleRules
{
	public ToolsDevelopment(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "UMG", "EnhancedInput"});
	}
}
