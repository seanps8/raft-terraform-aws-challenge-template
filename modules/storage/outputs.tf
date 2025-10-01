output "rds_host" {
  description = "Address of RDS instance"
  value = aws_db_instance.db.address
}

output "db_name" {
  description = "Database name"
  value = aws_db_instance.db.db_name
}