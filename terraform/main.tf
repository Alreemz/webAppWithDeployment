resource "aws_instance" "webapp" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name
  security_groups = [aws_security_group.web_sg.name]
  tags = {
    Name = "WebAppInstance"
  }
}
