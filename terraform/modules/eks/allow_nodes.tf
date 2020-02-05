 ########################################################################################
# setup provider for kubernetes

data "external" "aws_iam_authenticator" {
 # program = ["sh", "-c", "aws-iam-authenticator token -i example | jq -r -c .status.token"]
 # program = ["sh", "-c", "export token=$(aws-iam-authenticator token -i example | jq -r .status.token) && jq -n --arg token $token '{'token': $token}'"]
 program = ["sh", "-c",  "./authenticator.sh"]
}

provider "kubernetes" {
  host                      = "${aws_eks_cluster.tf_eks.endpoint}"
  cluster_ca_certificate    = "${base64decode(aws_eks_cluster.tf_eks.certificate_authority.0.data)}"
  token                    = "${data.external.aws_iam_authenticator.result.token}" 
  load_config_file          = false
  version = "~> 1.5"
}

# Allow worker nodes to join cluster via config map
resource "kubernetes_config_map" "aws_auth" {
  metadata {
    name = "aws-auth"
    namespace = "kube-system"
  }
  data = {
    mapRoles = <<EOF
- rolearn: ${aws_iam_role.tf-eks-node.arn}
  username: system:node:{{EC2PrivateDNSName}}
  groups:
    - system:bootstrappers
    - system:nodes
EOF
  }
  depends_on = [
    "aws_eks_cluster.tf_eks"  ] 
}

resource "kubernetes_pod" "flask" {
  metadata {
    name = "flask-example"
    labels = {
      App = "flask"
    }
  }

  spec {
    container {
      image = "ahmnouira/flask-hello-world:latest"
      name  = "example"

      port {
        container_port = 5000
      }
    }
  }
}

resource "kubernetes_deployment" "flask" {
  metadata {
    name = "scalable-flask-example"
    labels = {
      App = "ScalableFlaskExample"
    }
  }

  spec {
    replicas = 2
    selector {
      match_labels = {
        App = "ScalableFlaskExample"
      }
    }
    template {
      metadata {
        labels = {
          App = "ScalableFlaskExample"
        }
      }
      spec {
        container {
          image = "ahmnouira/flask-hello-world:latest"
          name  = "example"

          port {
            container_port = 5000
          }

          resources {
            limits {
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests {
              cpu    = "250m"
              memory = "50Mi"
            }
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "flask" {
  metadata {
    name = "flask-example"
  }
  spec {
    selector = {
      App = kubernetes_deployment.flask.spec.0.template.0.metadata[0].labels.App
    }
    port {
      port        = 80
      target_port = 5000
    }

    type = "ClusterIP"
  }
}

#output "lb_ip" {
#  value = kubernetes_service.flask.load_balancer_ingress[0].hostname
#}

