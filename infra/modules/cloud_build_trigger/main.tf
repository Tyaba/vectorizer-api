resource "google_cloudbuild_trigger" "github_trigger" {
  name        = var.trigger_name
  description = var.description
  project     = var.project_id
  location    = var.region

  github {
    owner = var.github_owner
    name  = var.github_repo
    push {
      branch = var.branch_regex
    }
  }

  filename = "cloudbuild.yaml"

  substitutions = {
    _SERVICE_NAME        = var.service_name
    _GOOGLE_CLOUD_REGION = var.region
  }


}