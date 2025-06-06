variable "location" {
  description = "リポジトリのロケーション"
  type        = string
}

variable "repository_id" {
  description = "リポジトリのID"
  type        = string
}

variable "description" {
  description = "リポジトリの説明"
  type        = string
  default     = "Dockerイメージ用のリポジトリ"
}