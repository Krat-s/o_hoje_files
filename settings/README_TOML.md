# Configurações TOML

Os valores fixos estão divididos por responsabilidade:

- `paths.toml`: caminhos de rede, pastas-modelo e identificadores da barra de tarefas.
- `timings.toml`: tempos de espera.
- `web.toml`: URLs, seletores e limites usados para gerar acessos.
- `quark.toml`: regiões de OCR e coordenadas.
- `ads.toml`: dados dos anúncios.

`settings.py` carrega esses arquivos na inicialização e mantém aliases antigos (`CAMINHO_PRINTS`, `ad_1_pi`, `url_target` etc.) para reduzir a quantidade de alterações nos módulos existentes.

## PI sem anúncio

O campo `pi` é uma string. Use `pi = ""` quando não houver anúncio. No Python, `if cfg.ad_2_pi:` será falso para uma string vazia e verdadeiro quando houver um PI preenchido.

## Acesso direto às configurações novas

```python
from settings.settings import PATHS, ADS

caminho_prints = PATHS["prints"]["output"]
anuncios = ADS["ads"]
```

O projeto usa `tomllib`, disponível a partir do Python 3.11. Para versões anteriores, será necessário instalar `tomli` e ajustar o import.
