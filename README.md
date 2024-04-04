# GitOps | Amazon Web Services - Ec2

O projeto GitOps é um template para provisionamento do Ec2 com isntalação e ngnix pare test na AWS.

## Como usar

Após ser realizado o clone do repositório é necessário a configuração de três variável de ambiente no repositório, sendo elas: `AWS_ACCESS_KEY`, `AWS_SECRET_KEY` e `AWS_REGION`. Essas variável são o Access Key ID, Secret Access Key e a Região da AWS. Para saber como criar as chaves acesse a [documentação oficial](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey).

Com as variáveis de ambiente definida no repositório já é possível executar a pipeline para provisionamento do EC2, porém há uma configuração padrão de provisionamento localizada em [config/defaults.yml](config/defaults.yml) que pode ser alterada de acordo com a necessidade do usuário.

OBS: foi configurado na conta um S3 para backend do terraform e um keypair para execução da pipeline configure o secret `KEYPAIR` para acesso ec2 que será solicitado ao no deploy do script terraform e app.

### Pipeline

A pipeline de infra é dividia em 2 workflows, sendo eles:
  - **Deploy (execução manual):** Provisiona a infraestrutura via Terraform.
  - **Destroy (execução manual):** Destrói a infraestrutura.

Deploy da API em python é nescessario rodar o job deploy_app p mesmo ira subir um api simples em flash e restartar o ngnix:
  - **Deploy_app (execução manual):** sube e atualiza a api alem de realizar um restart no nginx.
