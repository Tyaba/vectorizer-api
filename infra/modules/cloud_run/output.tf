output "service_url" {
  value       = google_cloud_run_service.service.status[0].url
  description = "Cloud Runサービスのデプロイされたエンドポイント"
}

output "service_name" {
  value       = google_cloud_run_service.service.name
  description = "Cloud Runサービス名"
}

output "service_id" {
  value       = google_cloud_run_service.service.id
  description = "Cloud RunサービスのID"
}
