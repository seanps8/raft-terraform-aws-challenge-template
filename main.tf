module "vpc" {
  source = "./modules/vpc"
}

module "storage" {
  source       = "./modules/storage"
}

module "lambda" {
  source           = "./modules/lambda"
}

module "api-gw" {
  source = "./modules/api-gw"
}