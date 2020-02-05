data "aws_acm_certificate" "example" {
  domain   = "*.flugel-dev.cf"
  statuses = ["ISSUED"]
  #types       = ["AMAZON_ISSUED"]
  #most_recent = true
}
