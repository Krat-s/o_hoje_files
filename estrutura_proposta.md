# Estrutura proposta — o_hoje_files

## Árvore completa

```
o_hoje_files/
│
├── departments/
│   ├── editorial/
│   │   ├── __init__.py
│   │   ├── billhead.py
│   │   ├── billhead_edition.py
│   │   ├── billhead_editions.py
│   │   ├── billhead_new_page_model.py
│   │   ├── boot_assistance.py
│   │   ├── wedding.py
│   │   ├── wedding_exporting_pdf.py
│   │   └── modulos_quark/
│   │       ├── __init__.py
│   │       └── utils_quark.py
│   │
│   │
│   ├── comercial/
│   │   ├── __init__.py
│   │   ├── drive_daily.py
│   │   ├── print_ad.py
│   │   ├── print_ad_by_selector.py
│   │   ├── print_ad_by_link_phone.py
│   │   └── bot_clicking/
│   │       ├── __init__.py
│   │       ├── boost_ad.py
│   │       ├── simple_bot_clicking.py
│   │       └── start_bot_clicking.py / .bat
│   │
│   ├── mail/                            # era Mail/
│   │   ├── __init__.py
│   │   └── gmail.py
│   │
│   └── tasks/                           # era Tasks/
│       ├── __init__.py
│       ├── report.py
│       └── module_tasks/
│           ├── __init__.py
│           └── index_numbers.py
│
├── shared/                              # lib real, hoje espalhada dentro de config/
│   ├── __init__.py
│   ├── automation/
│   │   ├── wait.py                      # era config/wait.py
│   │   ├── waits_checks.py              # era config/waits_checks.py
│   │   ├── waits_tesseract.py           # era config/waits_tesseract.py
│   │   ├── win_manager.py               # era config/settings/win_manager.py
│   │   └── web_driver.py                # era Web/modules/web_diver.py
│   ├── data_sync/
│   │   ├── data_edition_sync.py         # era config/core/data_edition_sync.py
│   │   ├── data_formatter.py            # era config/core/data_formatter.py
│   │   └── edition_formatter.py         # era config/core/edition_formatter.py
│   ├── edition_info.py                  # era config/core/edition_info.py
│   ├── scheduling/
│   │   ├── schedule_manager.py          # era config/core/schedule_manager.py
│   │   └── daily_task_random_time.py    # era config/core/daily_task_random_time.py
│   ├── file_manager.py                  # era config/file_manager.py
│   ├── utils.py                         # era config/utils.py
│   ├── gen_random_numbers.py            # era config/core/gen_randon_numbers.py (corrigir typo "randon"→"random" de passagem)
│   └── logging/
│       └── logs.py                      # era config/storage/Logs/logs.py — é código, fica em shared; os .csv que ele gera vão para storage/ (ver abaixo)
│
├── settings/                            # config de verdade, só declarativa — nada de lógica aqui
│   ├── __init__.py
│   ├── settings.py                      # passa a LER paths.toml em vez de duplicar os valores
│   ├── settings_edition_request.py
│   ├── settings_ocr.py
│   ├── settings_responsivePg.py
│   └── paths.toml
│
├── storage/                             # dado de runtime — NÃO é pacote Python, não versionar no git
│   ├── logs/
│   │   ├── All_in_one.csv
│   │   ├── billhead.csv
│   │   ├── boost_ad.csv
│   │   ├── FileManager.csv
│   │   ├── edition_info.csv
│   │   ├── gmail.csv
│   │   ├── print_ad.csv
│   │   ├── start_daily_schedules.csv
│   │   └── Wedding.csv
│   └── archives/                        # screenshots de referência p/ regiões de OCR
│       └── *.png
│
├── scripts/                             # era tests/ na raiz — renomeado porque não são testes
│   ├── auxiliary.py
│   ├── auxiliary_region.py
│   ├── keeping_on.py
│   ├── new_toys.py
│   └── run_fast.py
│
├── all_in_one.py                        # orquestrador — passa a importar de departments/ e shared/
├── api.py
├── requirements.txt
├── README.md
└── .gitignore                           # remover "*.toml" do ignore, já que paths.toml passa a ser a fonte real de verdade
```

## Notas de aplicação

- **`config/` deixa de existir como pasta única.** Ela vira três coisas com responsabilidades separadas: `settings/` (config declarativa), `shared/` (lib compartilhada) e `storage/` (dado gerado em runtime). Essa é a mudança que mais paga dividendo quando os novos departamentos chegarem, porque ninguém mais vai importar "um pouco de tudo" de um único pacote `config`.
- **`storage/` não deve ter `__init__.py`** nem ser importado como pacote — é só uma pasta de dados. Isso também facilita colocar `storage/` no `.gitignore` (hoje logs e prints de tela estão sendo versionados dentro do código).
- **Migração incremental sugerida:** mover uma pasta por vez (ex.: comece por `storage/`, que é só mover arquivos, sem tocar em import), rodando `all_in_one.py` a cada passo para confirmar que nada quebrou, antes de mexer em `shared/` (que tem mais imports cruzados).
