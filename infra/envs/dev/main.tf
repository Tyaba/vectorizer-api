module "artifact_registry" {
  source = "../../modules/artifact_registry"
  location = var.region
  repository_id = var.service_name
  description = "vectorizer-apiのリポジトリ"
}

module "cloud_build_trigger" {
  source = "../../modules/cloud_build_trigger"
  project_id = var.project_id
  service_name = var.service_name
  region = var.region
}
