terraform {
  backend "gcs" {
    bucket = "vectorizer-api"
    prefix = "terraform/dev/state"
  }
}