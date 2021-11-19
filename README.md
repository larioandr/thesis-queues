# thesis-queues

Модели систем массового обслуживания для кандидатской диссертации.


## Запуск ноутбуков

Все ноутбуки с экспериментами и экспериментальные данные лежат в папке
`experiments`. Для работы с ноутбуками нужно дополнительно установить пакеты:

- `matplotlib`
- `seaborn`
- `tarjan`
- `jupyterlab` или `jupyter`
- `pandas`
- `tqdm`
- `click`
- `pebble`
- `ipywidgets`
- `widgetsnbextension`

```bash
$ pip install matplotlib seaborn tarjan jupyterlab pandas tqdm click pebble \
    widgetsnbextension ipywidgets
```

Если используется `jupyter-lab`, то для того, чтобы заработали прогресс-бары,
нужно выполнить:

```bash
$ jupyter nbextension enable --py widgetsnbextension
$ jupyter labextension install @jupyter-widgets/jupyterlab-manager
```
