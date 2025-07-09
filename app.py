services:
  - type: web
    name: wa-webhook
    env: python
    plan: free
    buildCommand: ""
    startCommand: "python app.py"
