terraform {
 backend "s3" {
   bucket         = "flugelmxtst"
   key            = "terraform.tfstate"
   encrypt        = "true"
   dynamodb_table = "flugelmxtst-statelock"
 }
}
