OUTPUTS_FILE = "outputs.tf"

RESOURCE_PREFIXES = {
    # AI + machine learning
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#ai--machine-learning
    # Analytics and IoT
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#analytics-and-iot
    "databricks_access_connector": "dbac",
    "databricks_workspace": "dbw",
    "data_factory": "adf",
    "data_lake_store_account": "dls",
    "event_hub_namespace": "evhns",
    "event_hub": "evh",
    "fabric_capacity": "fc",
    # Compute and web
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#compute-and-web
    "app_service_plan": "asp",
    "function_app": "func",
    "virtual_machine": "vm",
    # Containers
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#containers
    "container_app": "ca",
    "container_app_environment": "cae",
    "container_registry": "cr",
    # Databases
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#databases
    "cosmos_database": "cosmos",
    "sql_database_server": "sql",
    "sql_database": "sqldb",
    "postgresql_flexible_server": "psql",
    # Developer tools
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#developer-tools
    # DevOps
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#devops
    "managed_grafana": "amg",
    "managed_devops_pools": "mdp",
    # Integration
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#integration
    # Management and governance
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#management-and-governance
    "application_insights": "appi",
    "log_analytics_workspace": "log",
    "resource_group": "rg",
    # Migration
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#migration
    # Networking
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#networking
    "network_security_group": "nsg",
    "private_endpoint": "pep",
    "virtual_network": "vnet",
    "virtual_network_subnet": "snet",
    # Security
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#security
    "key_vault": "kv",
    "managed_identity": "id",
    # Storage
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#storage
    "storage_account": "st",
    # Virtual desktop infrastructure
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#virtual-desktop-infrastructure
}

def generate_outputs() -> None:
    lines = []

    for resource in RESOURCE_PREFIXES.keys():
        lines.extend(
            [
                f'output "{resource}" {{',
                f'  description = "Prefix for {resource.replace("_", " ")}"',
                f'  value       = "{RESOURCE_PREFIXES[resource]}"',
                "}",
                "",
            ]
        )
    lines.pop()  # remove last empty line

    with open(OUTPUTS_FILE, "w") as f:
        f.write("\n".join(lines))

generate_outputs()
