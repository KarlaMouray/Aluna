def inicio():
  print("Iniciando a execucao")
  print("Vou continuar")
  hello()

def hello():
  valores = ["sol","chuva","vento","noite","lua"]
  print("Oi")
  loop(valores)
  wFile('/dev/null')

def loop(var1):
  for i in var1:
    print(i)

def wFile(fname):
  content = "TWVuc2FnZW0gc2VjcmV0YSwgdm9jZSBjb25zZWd1aXUuIE8gY29kaWdvIMOpIDIwMjIuCg==\n"
  f = open(fname, 'w')
  f.write(content)
  f.close()

inicio()
