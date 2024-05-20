from google.oauth2 import service_account

scope = ["https://www.googleapis.com/auth/cloud-platform"]
credentials = service_account.Credentials.from_service_account_info(
{
  "type": "service_account",
  "project_id": "project-scrapy-news",
  "private_key_id": "fd14fb9118ded90bdade8e1c88a4e3ed7e80f40d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDdqdFTchdJ+TeM\nYvWJC+wpD8mk/MprPspM5QRPoHAbEyLMn1VIqzjkMsxgM7IfGeDLagx8iBAFiwiA\nlkIpunVaqtVVz3EZCbqe/UWsv2PJ8N5veRNEKY+wYsgakkBLRGz81FBxQXdGK5Zh\nQXFG+QntbI8XWnn5PG79xZHQwMoHd2HaeDRvs6Z9WH2AXPnIU3Y0uk3MxNiUrVJr\neYbTwcGjjX9KcmkBc0U0EMKV3PCCeCmB4ihn7E3FlZ58a0Ep0L1h/KAOaco9M8eN\nFDS6rZnIi2asd8YQzjxUC6x1/y9e8pjd2s/2VBQkjQWTjY5ZCFHy0eMqaoXaE8wj\ngBVidQShAgMBAAECggEAPrlcG4HQZ0VXW6lxE3vFMwVdqQtDeD+HXWT86E9dCbxL\nf52is3KIIcLiJGLch4J6IvV6XQ7fgcILAOAEDuzNYn+u6J5PwacIIQ9IVQ6/fRhk\nySR4uDQOjfoV57b07JeLQ6wMq0+8IaYZ4qFzHYNBNOcgQpp+o3Ffcv4iOfEj+iJe\nQqt4CHVYah7lvGszob22YqNoXF9fKAsYxulh7Hlp0UKuOqBjYqpEsy353F1P4B72\n7zioXEWSUU+2pPeVGOxOacM0P2IFXFqnzIx3DF4TM4eI3gu/Gpy4hGqI3sE5rOk/\ng0ZAodbJ5KlYgztUbar6nqSVSlDvI0u9Gg6dgfYU1QKBgQDwdICwGhr+Q/cRZCC9\nMnNyeGCqu9WF5X4ppSTxl6wuXanWhgLxW6qUG2Sh0WZgqq8w89Mgoroy6s2zBLZx\nndDdeXteROhy/Pxt22Dh85pphzPENuhiqJrsgjrUISNWjrbHrv7409E36Ss96m4k\nDmt2la7v+pFp7skYp/2pekVB4wKBgQDr/lB9TxpkLS/lBHcY6oEUuVRyU4tKPoKm\nYSurXWq60Bq+y3CApbEtlz+D+VTAfzgYLYuCVtv1S3p+CCajx8e6YyWxdJr3Dr3U\nUIdVsVFXWrfbztLjmiydbN1R9PIJyf7E0i4g/ICSjWrYz7UyNGx0hvz9OVeh9I5g\nvhdgH72WqwKBgCE8yWkOQrrw5B8ISyo75g9lql8PVcWLYnQZOtEWWRuToN1hati4\nBg0w+CkSC+fC0DKhEYcKV1igckyTkzCDUxK6Lx5pwgPbCn2Y/HxfMvHxWWt+94Jj\nsf6NRdp6tirJ0WQqwV3d0aa72VlWpWDgiWQ77pGHfkA5XJzG495gY2BnAoGAShte\nYztH6lVWSPCSBbz+M+fO4OfjQblHhb/V2sZHEcrv2yI/feaKMOriAyt0tc49azpC\nKPflsq21FYaxu5Ss35bq60LWtuZmLhnrpbk89dWDDv9vshFkGTtqdKYaq4BHBL+L\nxMgGB/9oohT3rYBQ3nbVUx+CqVUGsNKAvKq6+mkCgYEA3QFe+cLQyEVHU4/lJOs9\naf7dibtKCM2SaQW9mA8CcjtT8E83NvcHn5aTfMlQjeO0vaEJacmJeEVUeB9D6GOg\nZulbSsKnPYdVWlftLC/dqq/FYp2x0tkLM9yGCdqMXZvOz0mri+Vxs/MKnRPjzIz+\nVm8UgfYnCZ6qasTy7WEcayo=\n-----END PRIVATE KEY-----\n",
  "client_email": "appoutside@project-scrapy-news.iam.gserviceaccount.com",
  "client_id": "111312142188829819559",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/appoutside%40project-scrapy-news.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}, 
scopes=scope)