
## importando bibliotecas necessárias
import time
from pathlib import Path

## Gerador de arquivos JSON para o Streaming
pasta = Path("../data/streaming/posts")
posts = [
    {"nome":"Pedro","postagem":"Recomendo, voltarei sempre!", "data":43590},
    {"nome":"João","postagem":"Muita variedade", "data":43590},
    {"nome":"Maria","postagem":"Bom atendimento", "data":43590},
    {"nome":"Ana","postagem":"Produtos caros", "data":43590},
    {"nome":"Lucia","postagem":"Boa localização", "data":43590},
    {"nome":"Paulo","postagem":"Não encontrei o que procurava", "data":43590}
]

## Criação dos arquivos JSON
for i, post in enumerate(posts,start=1):
    arquivo = pasta / f"post_{i}.json"
    with open(arquivo,"w", encoding="utf-8") as f:
        json.dump(post,f, ensure_ascii=False)
    print(f"Arquivo gerado: {arquivo} criado com sucesso!")
    time.sleep(5)  # Aguarda 5 segundos antes de criar o próximo arquivo

    ## Para executar o script, basta rodar o comando: python Gera-Json.py