import * as pulumi from "@pulumi/pulumi";
import * as resources from "@pulumi/azure-native/resources";
import * as portal from "@pulumi/azure-native/portal"

// Create an Azure Resource Group
const resourceGroup = new resources.ResourceGroup("resourceGroup");

const dashboard = new portal.Dashboard("dash", {
    resourceGroupName: resourceGroup.name,
    dashboardName: "my-dash-1",
    lenses: [{
        order: 1,
        parts: [{
            position: {
                x: 0,
                y: 0,
                colSpan: 6,
                rowSpan: 4
            },
            metadata: {
                inputs: [{
                    name: "scope",
                    isOptional: true
                }],
                type: "Extension/HubsExtension/PartType/MarkdownPart"
            }
        }]
    }]
});
