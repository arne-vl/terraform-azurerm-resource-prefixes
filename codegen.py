OUTPUTS_FILE = "outputs.tf"

RESOURCE_PREFIXES = {
    # AI + machine learning
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#ai--machine-learning
    "ai_search": "srch",
    "foundry_tools": "ais",
    "foundry_account": "aif",
    "foundry_account_project": "proj",
    "foundry_hub": "hub",
    "foundry_hub_project": "proj",
    "ai_video_indexer": "avi",
    "machine_learning_workspace": "mlw",
    "openai_service": "oai",
    "bot_service": "bot",
    "computer_vision": "cv",
    "content_moderator": "cm",
    "content_safety": "cs",
    "custom_vision_prediction": "cstv",
    "custom_vision_training": "cstvt",
    "document_intelligence": "di",
    "face_api": "face",
    "health_insights": "hi",
    "immersive_reader": "ir",
    "language_service": "lang",
    "speech_service": "spch",
    "translator": "trsl",

    # Analytics and IoT
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#analytics-and-iot
    "analysis_services_server": "as",
    "databricks_access_connector": "dbac",
    "databricks_workspace": "dbw",
    "data_explorer_cluster": "dec",
    "data_explorer_cluster_database": "dedb",
    "data_factory": "adf",
    "digital_twin": "dt",
    "stream_analytics": "asa",
    "synapse_private_link_hub": "synplh",
    "synapse_sql_dedicated_pool": "syndp",
    "synapse_spark_pool": "synsp",
    "synapse_workspace": "synw",
    "data_lake_store_account": "dls",
    "event_hub_namespace": "evhns",
    "event_hub": "evh",
    "event_grid_domain": "evgd",
    "event_grid_namespace": "evgns",
    "event_grid_subscription": "evgs",
    "event_grid_topic": "evgt",
    "event_grid_system_topic": "egst",
    "fabric_capacity": "fc",
    "hdinsight_hadoop_cluster": "hadoop",
    "hdinsight_hbase_cluster": "hbase",
    "hdinsight_kafka_cluster": "kafka",
    "hdinsight_spark_cluster": "spark",
    "hdinsight_storm_cluster": "storm",
    "hdinsight_ml_services_cluster": "mls",
    "iot_hub": "iot",
    "provisioning_services": "provs",
    "provisioning_services_certificate": "pcert",
    "powerbi_embedded": "pbi",
    "time_series_insights_environment": "tsi",

    # Compute and web
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#compute-and-web
    "app_service_environment": "ase",
    "app_service_plan": "asp",
    "load_testing_instance": "lt",
    "availability_set": "avail",
    "arc_enabled_server": "arck",
    "arc_enabled_kubernetes_cluster": "arck",
    "arc_enabled_private_link_scope": "pls",
    "arc_gateway": "arcgw",
    "batch_accounts": "ba",
    "cloud_service": "cld",
    "communication_services": "acs",
    "disk_encryption_set": "des",
    "function_app": "func",
    "gallery": "gal",
    "hosting_evironment": "host",
    "image_template": "it",
    "managed_disk_os": "osdisk",
    "managed_disk_data": "disk",
    "notification_hub": "ntf",
    "notification_hub_namespace": "ntfns",
    "proximity_placement_group": "ppg",
    "restore_point_collection": "rpc",
    "snapshot": "snap",
    "static_web_app": "stapp",
    "virtual_machine": "vm",
    "virtual_machine_scale_set": "vmss",
    "virtual_machine_maintenance_configuration": "mc",
    "virtual_machine_storage_account": "stvm",
    "web_app": "app",

    # Containers
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#containers
    "aks_cluster": "aks",
    "aks_system_node_pool": "npsystem",
    "aks_user_node_pool": "np",
    "container_app": "ca",
    "container_app_environment": "cae",
    "container_app_job": "caj",
    "container_registry": "cr",
    "container_instance": "ci",
    "service_fabric_cluster": "sf",
    "service_fabric_managed_cluster": "sfmc",

    # Databases
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#databases
    "cosmos_database": "cosmos",
    "cosmos_database_apache_cassandra": "coscas",
    "cosmos_database_mongo_db": "cosmon",
    "cosmos_database_nosql": "cosno",
    "cosmos_database_table": "costab",
    "cosmos_database_apache_gremlin": "cosgrm",
    "cosmos_database_postgresql_cluster": "cospos",
    "redis": "redis",
    "managed_redis": "amr",
    "sql_database_server": "sql",
    "sql_database": "sqldb",
    "sql_elastic_job_agent": "sqlja",
    "sql_elastic_pool": "sqlep",
    "mysql_database": "mysql",
    "postgresql_database": "psql",
    "sql_managed_instance": "sqlmi",

    # Developer tools
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#developer-tools
    "app_configuration_store": "appcs",
    "maps_account": "map",
    "signalr": "sigr",
    "web_pub_sub": "wps",

    # DevOps
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#devops
    "managed_grafana": "amg",
    "managed_devops_pools": "mdp",

    # Integration
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#integration
    "api_management_service_instance": "apim",
    "integration_account": "ia",
    "logic_app": "logic",
    "service_bus_namespace": "sbns",
    "service_bus_queue": "sbq",
    "service_bus_topic": "sbt",
    "service_bus_topic_subscription": "sbts",

    # Management and governance
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#management-and-governance
    "automation_account": "aa",
    "application_insights": "appi",
    "monitor_action_group": "ag",
    "monitor_data_collection_rule": "dcr",
    "monitor_alert_processing_rule": "apr",
    "data_collection_endpoint": "dce",
    "deployment_script": "script",
    "log_analytics_workspace": "log",
    "log_analytics_query_pack": "pack",
    "management_group": "mg",
    "purview_instance": "pview",
    "resource_group": "rg",
    "template_specs_name": "ts",

    # Migration
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#migration
    "migrate_project": "migr",
    "database_migration_service_instance": "dms",
    "recovery_services_vault": "rsv",

    # Networking
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#networking
    "application_gateway": "agw",
    "application_security_group": "asg",
    "cdn_profile": "cdnp",
    "cdn_endpoint": "cdne",
    "connections": "con",
    "dns_forwarding_ruleset": "dnsfrs",
    "dns_private_resolver": "dnspr",
    "dns_private_resolver_inbound_endpoint": "in",
    "dns_private_resolver_outbound_endpoint": "out",
    "firewall": "afw",
    "firewall_policy": "afwp",
    "expressroute_circuit": "erc",
    "expressroute_direct": "erd",
    "expressroute_gateway": "ergw",
    "front_door_profile": "afd",
    "front_door_endpoint": "fde",
    "front_door_firewall_policy": "fdfp",
    "front_door": "afd",
    "ip_group": "ipg",
    "load_balancer_internal": "lbi",
    "load_balancer_external": "lbe",
    "load_balancer_rule": "rule",
    "local_network_gateway": "lgw",
    "nat_gateway": "ng",
    "network_interface": "nic",
    "network_security_perimeter": "nsp",
    "network_security_group": "nsg",
    "network_security_group_security_rule": "nsgsr",
    "network_watcher": "nw",
    "private_link": "pl",
    "private_endpoint": "pep",
    "public_ip": "pip",
    "public_ip_prefix": "ippre",
    "route_filter": "rf",
    "route_server": "rtserv",
    "route_table": "rt",
    "service_endpoint_policy": "se",
    "traffic_manager_profile": "traf",
    "user_defined_route": "udf",
    "virtual_network": "vnet",
    "virtual_network_gateway": "vgw",
    "virtual_network_peering": "peer",
    "virtual_network_subnet": "snet",
    "virtual_wan": "vwan",
    "virtual_wan_hub": "vhub",

    # Security
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#security
    "bastion": "bas",
    "key_vault": "kv",
    "key_vault_managed_hsm": "kvmhsm",
    "managed_identity": "id",
    "security_group": "sg",
    "ssh_key": "sshkey",
    "vpn_gateway": "vpng",
    "vpn_connection": "vcn",
    "vpn_site": "vst",
    "web_application_firewall_policy": "waf",
    "web_application_firewall_policy_rule_group": "wafrg",

    # Storage
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#storage
    "backup_vault": "bvault",
    "backup_vault_policy": "bkpol",
    "file_share": "share",
    "storage_account": "st",
    "storage_sync_service": "sss",

    # Virtual desktop infrastructure
    # https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-abbreviations#virtual-desktop-infrastructure
    "virtual_desktop_host_pool": "vdpool",
    "virtual_desktop_application_group": "vdag",
    "virtual_desktop_workspace": "vdws",
    "virtual_desktop_scaling_plan": "vdscaling",
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
