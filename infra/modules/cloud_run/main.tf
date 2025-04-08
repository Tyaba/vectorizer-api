resource "google_cloud_run_service" "service" {
  name     = var.service_name
  location = var.region
  project  = var.project_id
  template {
    spec {
      containers {
        ports {
          container_port = var.port
        }
        image = var.image

        resources {
          limits = {
            cpu    = var.cpu
            memory = var.memory
          }
        }

        dynamic "env" {
          for_each = var.env_vars
          content {
            name  = env.key
            value = env.value
          }
        }

        dynamic "env" {
          for_each = var.secrets
          content {
            name = env.key
            value_from {
              secret_key_ref {
                name  = env.value.secret_id
                key = env.value.version
              }
            }
          }
        }
      }
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/minScale" = var.min_instances
        "autoscaling.knative.dev/maxScale" = var.max_instances
        "run.googleapis.com/client-name"   = "terraform"
        "client.knative.dev/user-image"    = var.image
        "run.googleapis.com/launch-stage"  = "BETA"
      }
      labels = {
        "commit-sha" = var.short_sha != "" ? var.short_sha : "latest"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  autogenerate_revision_name = true
}

