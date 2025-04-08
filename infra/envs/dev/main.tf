module "artifact_registry" {
  source = "../../modules/artifact_registry"
  location = var.region
  repository_id = var.service_name
  description = "vectorizer-apiのリポジトリ"
}

module "builder_service_account" {
  source = "../../modules/iam"
  project_id = var.project_id
  account_id = var.service_name
  display_name = "vectorizer-api-builder"
  description = "vectorizer-apiのビルダーサービスアカウント"
  roles = [
    "roles/resourcemanager.projectIamAdmin",
    "roles/iam.serviceAccountUser",
    "roles/storage.objectUser",  # gcs backendの読み書きのため
    "roles/cloudbuild.builds.editor",
    "roles/logging.logWriter",
    "roles/run.admin",
    ]
}

module "cloud_build_trigger" {
  source = "../../modules/cloud_build_trigger"
  project_id = var.project_id
  service_account_id = module.builder_service_account.id
  repository_region = var.region
  trigger_name = var.service_name
  service_name = var.service_name
  github_owner = var.github_owner
  github_repo = var.github_repo
  branch_regex = var.branch_regex
  substitutions = {
    _SERVICE_NAME = var.service_name
    _GOOGLE_CLOUD_REGION = var.region
    _ENV = "dev"
  }
  description = "Vectorizer APIのCloud Buildトリガー"
}

