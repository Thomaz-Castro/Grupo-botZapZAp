from selenium import webdriver


drive = webdriver.Edge(executable_path=r'.\msedgedriver.exe',)

drive.get("https://api.whatsapp.com/send?phone=5512982768155")

#NÃO FUNCIONAAAAA
