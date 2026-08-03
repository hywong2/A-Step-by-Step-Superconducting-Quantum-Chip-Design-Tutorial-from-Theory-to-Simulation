# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2026.1.2
# 10:33:55  Aug 03, 2026
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project28b")
oDesign = oProject.SetActiveDesign("Full_Chip_Eigenmode")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-2.3mm",
		"YStart:="		, "-1.198mm",
		"ZStart:="		, "0mm",
		"Width:="		, "0.0580000000000003mm",
		"Height:="		, "0.196mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "NonModel#",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"IsSurfaceMaterialEditable:=", True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rectangle1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Model",
					"Value:="		, True
				]
			]
		]
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignLumpedRLC(
	[
		"NAME:LumpRLC1",
		"Objects:="		, ["Rectangle1"],
		[
			"NAME:CurrentLine",
			"Coordinate System:="	, "Global",
			"Start:="		, ["-2.3mm","-1.08mm","0mm"],
			"End:="			, ["-2.242mm","-1.086mm","0mm"]
		],
		"RLC Type:="		, "Parallel",
		"UseResist:="		, True,
		"Resistance:="		, "50ohm",
		"UseInduct:="		, False,
		"UseCap:="		, False
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "2.3mm",
		"YStart:="		, "-1.002mm",
		"ZStart:="		, "0mm",
		"Width:="		, "-0.0580000000000003mm",
		"Height:="		, "-0.196mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"IsSurfaceMaterialEditable:=", True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oModule.AssignLumpedRLC(
	[
		"NAME:LumpRLC2",
		"Objects:="		, ["Rectangle2"],
		[
			"NAME:CurrentLine",
			"Coordinate System:="	, "Global",
			"Start:="		, ["2.3mm","-1.102mm","0mm"],
			"End:="			, ["2.242mm","-1.098mm","0mm"]
		],
		"RLC Type:="		, "Parallel",
		"UseResist:="		, True,
		"Resistance:="		, "50ohm",
		"UseInduct:="		, False,
		"UseCap:="		, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-0.938mm",
		"YStart:="		, "-2.41mm",
		"ZStart:="		, "0mm",
		"Width:="		, "0.196mm",
		"Height:="		, "0.0580000000000003mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle3",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"IsSurfaceMaterialEditable:=", True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oModule.AssignLumpedRLC(
	[
		"NAME:LumpRLC3",
		"Objects:="		, ["Rectangle3"],
		[
			"NAME:CurrentLine",
			"Coordinate System:="	, "Global",
			"Start:="		, ["-0.835mm","-2.41mm","0mm"],
			"End:="			, ["-0.834mm","-2.352mm","0mm"]
		],
		"RLC Type:="		, "Parallel",
		"UseResist:="		, True,
		"Resistance:="		, "50ohm",
		"UseInduct:="		, False,
		"UseCap:="		, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "2.3mm",
		"YStart:="		, "1.002mm",
		"ZStart:="		, "0mm",
		"Width:="		, "-0.0580000000000003mm",
		"Height:="		, "0.196mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle4",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"IsSurfaceMaterialEditable:=", True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oModule.AssignLumpedRLC(
	[
		"NAME:LumpRLC4",
		"Objects:="		, ["Rectangle4"],
		[
			"NAME:CurrentLine",
			"Coordinate System:="	, "Global",
			"Start:="		, ["2.3mm","1.09mm","0mm"],
			"End:="			, ["2.242mm","1.094mm","0mm"]
		],
		"RLC Type:="		, "Parallel",
		"UseResist:="		, True,
		"Resistance:="		, "50ohm",
		"UseInduct:="		, False,
		"UseCap:="		, False
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-2.3mm",
		"YStart:="		, "1.002mm",
		"ZStart:="		, "0mm",
		"Width:="		, "0.0580000000000003mm",
		"Height:="		, "0.196mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle5",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"ReferenceTemperature:=", "20cel",
		"IsMaterialEditable:="	, True,
		"IsSurfaceMaterialEditable:=", True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oModule.AssignLumpedRLC(
	[
		"NAME:LumpRLC5",
		"Objects:="		, ["Rectangle5"],
		[
			"NAME:CurrentLine",
			"Coordinate System:="	, "Global",
			"Start:="		, ["-2.3mm","1.12mm","0mm"],
			"End:="			, ["-2.242mm","1.116mm","0mm"]
		],
		"RLC Type:="		, "Parallel",
		"UseResist:="		, True,
		"Resistance:="		, "50ohm",
		"UseInduct:="		, False,
		"UseCap:="		, False
	])
