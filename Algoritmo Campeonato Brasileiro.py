tabela= ("Flamengo"," Internacional","AtléticoMG","São Paulo","Fluminense","Grêmio","Palmeiras","Santos","Athletico Paranaense","Red Bull Bragantino ","Ceará ","Corinthians"," Atlético - GO"," Bahia","Sport","Fortaleza ","Vasco","Goiás"," Coritiba "," Botafogo " )
print(f"Os Top 5 da tabela são {tabela[0:5]}")
print("-------")
print(f"OS 4 últimos colocados da tabela são {tabela[16:20]}")
print("-------")
print(f"Lista com os times em ordem Alfabética: {sorted(tabela)}")
print("-------")
print("O Corinthians está na posição: ", end=" ")
print(tabela.index("Corinthians"))
