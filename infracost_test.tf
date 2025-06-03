provider "aws" {
  region = "us-east-1"
  access_key = "mock_access_key"
  secret_key = "mock_secret_key"
  skip_credentials_validation = true
  skip_requesting_account_id = true
}

# ───── ECS Fargate: Navigation App ─────
resource "aws_ecs_task_definition" "navigation_task" {
  family                   = "mysteryisland-navigation"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "512"   # 0.5 vCPU
  memory                   = "1024"  # 1 GB
  network_mode             = "awsvpc"
  execution_role_arn       = "arn:aws:iam::123456789012:role/mock"
  container_definitions    = "[]"
}

resource "aws_ecs_service" "navigation_service" {
  name            = "mysteryislandservice"
  cluster         = "mystery-island-cluster"
  task_definition = aws_ecs_task_definition.navigation_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"
  network_configuration {
    subnets          = ["subnet-12345"]
    assign_public_ip = true
    security_groups  = ["sg-12345"]
  }
}

# ───── ECS Fargate: Chatbot ─────
resource "aws_ecs_task_definition" "chatbot_task" {
  family                   = "mysteryisland-chatbot"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"   # 0.25 vCPU
  memory                   = "512"   # 0.5 GB
  network_mode             = "awsvpc"
  execution_role_arn       = "arn:aws:iam::123456789012:role/mock"
  container_definitions    = "[]"
}

resource "aws_ecs_service" "chatbot_service" {
  name            = "mysteryislandchatbotservice"
  cluster         = "mystery-island-cluster"
  task_definition = aws_ecs_task_definition.chatbot_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"
  network_configuration {
    subnets          = ["subnet-12345"]
    assign_public_ip = true
    security_groups  = ["sg-12345"]
  }
}

# ───── S3 Bucket (Static Assets) ─────
resource "aws_s3_bucket" "mystery_island_assets" {
  bucket = "mystery-island-static"
}

# ───── CloudWatch Log Group ─────
resource "aws_cloudwatch_log_group" "ecs_logs" {
  name              = "/ecs/mysteryisland"
  retention_in_days = 1
}

# ───── ALB (optional - use if included in real setup) ─────
resource "aws_lb" "mystery_alb" {
  name               = "mysteryisland-alb"
  internal           = false
  load_balancer_type = "application"
  subnets            = ["subnet-12345"]
}
