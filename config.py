from pathlib import Path

data_dir = (Path().cwd().parents[0] / 'data').absolute()
data_raw = data_dir / 'raw'
data_mask = data_dir / 'masks'
data_cluster = data_dir / 'clusters'
data_cell_mask = data_dir / 'cell_masks'

data_figure = (Path().cwd().parents[0] / 'figures').absolute()
