variable "credentials" {
  description = "The path to the service account key file"
  default = "./keys/creds.json"
}

variable "project" {
  description = "The project ID"
  default = "regal-cycling-448206-q3"
}

variable "region" {
  description = "The region of the resources"
  default = "us-west1"
}

variable "location" {
  description = "The location of the resources"
  default = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  default = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "The name of the bucket"
  default = "regal-cycling-448206-q3-terra-bucket" 
}

variable "gcs_storage_class" {
  description = "The storage class of the bucket"
  default = "STANDARD"
}
