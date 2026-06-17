from app.main import create_app


app = create_app()

if __name__ == "__main__":
    
    app.run(
        host= "0.0.0.0",
        port=5000,
        debug=True
    )
    
#что бы получить вывод,нужно нажать в run.py кнопку,после зайти в powershell и вбить команду:
#$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/ask" `
  #-Method POST `
  #-ContentType "application/json" `
  #-Body '{"prompt":"ваш промпт"}'

#$response | ConvertTo-Json -Depth 10