"""An Azure RM Python Pulumi program"""
import pulumi
from pulumi_azure_native import portal
from pulumi_azure_native import resources

# Create an Azure Resource Group
resource_group = resources.ResourceGroup('resource_group')

dashboard = portal.Dashboard(
    "myDash",
    resource_group_name=resource_group.name,
    lenses=[
        portal.DashboardLensArgs(
            order=1,
            parts=[
                portal.DashboardPartsArgs(
                    position=portal.DashboardPartsPositionArgs(
                        x=0,
                        y=0,
                        col_span=6,
                        row_span=4
                    ),
                    metadata=portal.MarkdownPartMetadataArgs(
                        inputs=[{
                            "name": "scope",
                            "isOptional": True
                        }],
                        type="Extension/HubsExtension/PartType/BrowseResourceGroupPinnedPart"
                    )
                )
            ]
        )
    ],
)

pulumi.export("dashboardId", dashboard.id)
